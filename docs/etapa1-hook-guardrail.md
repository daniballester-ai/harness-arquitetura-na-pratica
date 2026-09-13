# Etapa 1 — Hook de guardrail: proteção do artefato do modelo

## Risco escolhido

Diferente do exemplo de aula ("bloquear merge na main"), este hook protege **`models/cacao_leaf_classifier.pt`**, o artefato do modelo treinado (EfficientNet-B0, ~16MB). O risco real: este repositório não tem o dataset nem o notebook de treino completo — só a API que consome o modelo. Se o arquivo for apagado, movido ou sobrescrito por um comando do agente, não há como recriá-lo sem voltar ao projeto CacauFito original e rodar o treino de novo (que leva ~1h de GPU no Kaggle).

## Implementação

- `.claude/hooks/guard-model-artifact.py`: lê o JSON do `PreToolUse` (matcher `Bash`) via stdin, extrai `tool_input.command`, e verifica se o comando contém `rm`, `mv`, `truncate`, `cp` (como destino), redirecionamento (`>`/`>>`) ou `sed -i` mirando `models/cacao_leaf_classifier.pt`. Se bater, devolve `{"hookSpecificOutput": {"permissionDecision": "deny", ...}}`, bloqueando a ação de verdade (não é só um aviso).
- `.claude/settings.json`: registra o hook no evento `PreToolUse`, matcher `Bash`.

## Testes unitários do hook (pipe-test, fora do harness)

Executados diretamente, simulando o JSON que o Claude Code manda para o hook:

```
$ echo '{"tool_name":"Bash","tool_input":{"command":"rm models/cacao_leaf_classifier.pt"}}' | python .claude/hooks/guard-model-artifact.py
{"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny", "permissionDecisionReason": "Bloqueado pelo hook guard-model-artifact: ..."}}

$ echo '{"tool_name":"Bash","tool_input":{"command":"mv models/cacao_leaf_classifier.pt /tmp/old.pt"}}' | python .claude/hooks/guard-model-artifact.py
{"hookSpecificOutput": {..., "permissionDecision": "deny", ...}}

$ echo '{"tool_name":"Bash","tool_input":{"command":"echo oops > models/cacao_leaf_classifier.pt"}}' | python .claude/hooks/guard-model-artifact.py
{"hookSpecificOutput": {..., "permissionDecision": "deny", ...}}

$ echo '{"tool_name":"Bash","tool_input":{"command":"ls -la models/cacao_leaf_classifier.pt"}}' | python .claude/hooks/guard-model-artifact.py
(sem saída — não bloqueado, como esperado para leitura)
```

Todos os 4 casos se comportaram como esperado: os 3 comandos destrutivos foram sinalizados para bloqueio, o comando de leitura não.

## Limitação encontrada ao tentar provar o bloqueio ao vivo

A sessão do agente usada para escrever este hook está vinculada ao projeto `CacauFito` (é onde a sessão do Claude Code foi aberta), não a este repositório. Hooks do Claude Code são carregados a partir do `.claude/settings.json` do **projeto em que a sessão está rodando** — então, mesmo operando nos arquivos deste repositório por caminho absoluto, o hook daqui não é consultado por aquela sessão.

Prova disso: tentei `mv models/cacao_leaf_classifier.pt models/cacao_leaf_classifier.pt.bak` a partir da sessão vinculada ao CacauFito — o comando **passou sem bloqueio** (o hook deste repositório não é carregado ali). O arquivo foi renomeado de volta manualmente na sequência, sem perda.

**Ação pendente para fechar a evidência do deliverable**: abrir uma sessão do Claude Code (ou do editor com a extensão) com a raiz em `C:\Fitec\harness-arquitetura-na-pratica` e, de dentro dela, disparar de propósito um comando como `rm models/cacao_leaf_classifier.pt` — aí sim o `.claude/settings.json` deste repositório é carregado e o bloqueio real (com o diálogo de permissão negada) deve aparecer. O print/log dessa tentativa é a evidência final pedida pela Etapa 1.
