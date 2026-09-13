# Relatório Final — Harness e Arquitetura na Prática

**Autora**: Danielle Magalhães Ballester. **Repositório**: [github.com/daniballester-ai/harness-arquitetura-na-pratica](https://github.com/daniballester-ai/harness-arquitetura-na-pratica)

## 1. Autonomia e guardrail (Etapa 1)

Comparei modo direto (auto-accept) × modo de plano na mesma tarefa (endpoint `/version`). Direto: ~2min38s, controle baixo (só revisão do diff pronto), mas um bug real (atributo faltando) foi corrigido no meio sem pausa. Plano: ~28min35s, controle alto — ao ver o plano, redirecionei a tarefa inteira para virar uma proposta OpenSpec antes de qualquer código, algo que só é possível *antes* da implementação. **Guardrail**: hook `PreToolUse` que bloqueia `rm`/`mv`/`cp`/`>`/`sed -i` sobre `models/cacao_leaf_classifier.pt` (o modelo treinado, sem dataset local para retreinar). Testado por pipe-test (4 casos, comportamento correto) e depois confirmado ao vivo: numa sessão aberta com raiz neste repositório, o comando `rm models/cacao_leaf_classifier.pt` foi de fato negado pelo hook (print em `docs/etapa1-hook-bloqueio-evidencia.png`), com uma cópia de segurança feita antes como precaução.

## 2. TDD e enforcement (Etapa 2)

Ciclo Red-Green-Refactor real: teste escrito e falhando (`98bbe50`) antes da implementação do limite de upload (`fa2f604`). Investiguei o `tdd-guard` (hook que bloqueia implementação sem teste falhando ou além do escopo do teste) — não instalável neste ambiente (sem binário `claude` CLI), documentado a partir da documentação oficial. Comparação com/sem TDD: a tarefa com TDD chegou a 3 casos de borda pensados *antes* de codificar; a tarefa sem TDD (validação de `prediction_id`) teve só 2 casos lembrados *depois*, faltando justamente o caso de regressão.

## 3. Checkpoint humano (Etapa 3)

Defini: antes de expor um novo endpoint HTTP publicamente, um humano revisa o diff e decide aprovar/editar/rejeitar. Simulado com a implementação do `/version`: o agente parou antes de commitar, apresentou o diff, e eu, no papel de revisora técnica, aprovei como estava (endpoint sem dado sensível, testes passando).

## 4. Decisão arquitetural (Etapas 4 e 5)

Pedi ao agente um resumo da arquitetura real (6 módulos, 881 linhas): identificamos dois acoplamentos concretos — `main.py` como controlador gordo, e `auth.py` lendo diretamente constantes privadas de `history.py` em vez de uma API pública. Decisão: manter monolito modular (não extrair serviço — custo operacional não se justifica no tamanho/time atual), aplicando refatorações leves em vez disso. Documentado em ADR 0001 (formato MADR) e em dois diagramas Mermaid: um C4 genérico (bom para visão rápida) e outro regenerado com o contexto da Etapa 4, destacando visualmente o acoplamento problemático (melhor para justificar a decisão).

## 5. Vá Além (Etapa 6)

Rodei `ruff` e `bandit` sobre o código real. Achado relevante: `torch.load` sem `weights_only=True` em `model.py` (bandit B614, CWE-502) — risco real de execução de código arbitrário se o artefato do modelo fosse adulterado. Corrigido e verificado (mesmos pesos carregados, 55/55 testes passando). Aprendizado principal: ferramentas de análise estática pegam problemas de segurança que passam despercebidos numa revisão manual de código focada em lógica de negócio.

## 6. Dificuldade real enfrentada

Ao tentar provar o hook da Etapa 1 funcionando de verdade, descobri que **a sessão do agente estava vinculada ao projeto de origem (CacauFito)**, não a este repositório — hooks do Claude Code são carregados a partir do projeto em que a sessão roda, não do caminho absoluto dos arquivos manipulados. Testei isso com segurança (um `mv` reversível, sem perda de dados) em vez de assumir que funcionaria, documentei a limitação, e só depois resolvi de verdade: abri uma sessão nova com raiz no repositório certo, fiz um backup de segurança do artefato antes de arriscar, e só então disparei o `rm` real — que foi bloqueado como esperado. A lição prática: harness e hooks não são só configuração de arquivo, são também sobre *onde* o agente está rodando; e antes de testar uma ação destrutiva de propósito, vale a pena ter uma rede de segurança, mesmo confiando no hook.
