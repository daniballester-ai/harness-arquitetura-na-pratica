# Etapa 1 — Comparação entre dois modos de autonomia

Tarefa usada nas duas rodadas: adicionar um endpoint `GET /version` na API de inferência, retornando a versão da API e a arquitetura do modelo carregado (`classifier.architecture`, que precisava ser exposto em `LeafClassifier.__init__`).

## Rodada 1 — modo direto (auto-accept edits)

O agente implementou a mudança direto: leu `main.py`, editou o endpoint, percebeu no meio do caminho que `LeafClassifier` não expunha `architecture` (só lia o valor localmente para validação), corrigiu isso também, e testou com `TestClient`. Nenhuma pausa para aprovação em nenhum momento.

- **Tempo gasto:** ~2min38s (158s).
- **Sensação de controle:** baixa. Só vi o resultado pronto (diff completo) depois de tudo feito; não tive chance de intervir no meio.
- **Risco percebido:** maior. Um bug real (atributo faltando) só apareceu porque o agente seguiu direto e teve que se autocorrigir; se a correção passasse despercebida ou fosse feita de um jeito que eu não concordasse, eu só descobriria revisando o diff final.

## Rodada 2 — modo de plano (plan mode)

O agente entrou em modo de plano, escreveu um plano de implementação (arquivo de plano dedicado) e pediu aprovação explícita antes de tocar em qualquer código.

- **Tempo gasto:** ~28min35s (1715s) — bem mais longo, mas boa parte desse tempo foi o próprio processo de formalização (ver abaixo), não "espera passiva".
- **Sensação de controle:** alta. Ao ver o plano, rejeitei a aprovação direta e redirecionei a tarefa inteira: em vez de implementar a partir do plano, pedi para formalizar como uma proposta OpenSpec (`proposal.md` + spec delta + `tasks.md`) antes de qualquer código ser escrito. O modo de plano deu exatamente a abertura para isso — não é só "aprovar ou rejeitar o mesmo plano", é poder trocar o processo inteiro antes que qualquer coisa aconteça.
- **Risco percebido:** menor. Nada foi tocado no código-fonte ainda nesta rodada; o risco fica represado inteiramente na camada de planejamento/especificação, revisável por escrito, antes de qualquer execução.

## O que a comparação revelou

O modo direto é rápido e funciona bem quando a tarefa é pequena e bem entendida — mas o único ponto de controle humano é a revisão do diff *depois* de pronto, o que significa que decisões de processo (como "isso deveria virar uma spec formal antes?") só podem ser tomadas tarde demais, quando o código já existe. O modo de plano é mais lento, mas o ganho não é só "revisar o código antes" — é poder mudar a forma de resolver o problema (aqui, add-hoc → processo formal com OpenSpec) sem custo de retrabalho, porque nada foi implementado ainda. Para uma tarefa isolada e de baixo risco, o modo direto compensa; para decisões que podem mudar de forma (não só de conteúdo), o modo de plano paga o tempo extra.
