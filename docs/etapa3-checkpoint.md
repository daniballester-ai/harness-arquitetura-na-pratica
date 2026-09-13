# Etapa 3 — Checkpoint humano obrigatório

## Checkpoint definido

**Antes de expor um novo endpoint HTTP publicamente** (ou seja, antes de commitar/mesclar uma rota nova para `main`), um humano do grupo revisa o diff gerado pelo agente e decide explicitamente: **aprovar como está / editar / rejeitar**. Nenhum endpoint novo entra no repositório só porque os testes automatizados passaram — a aprovação humana é obrigatória e separada da execução dos testes.

## Simulação do checkpoint

**Caso usado**: implementação do endpoint `GET /version`, retomando a proposta OpenSpec `add-version-endpoint` criada na Etapa 1 (que havia ficado só como planejamento, sem código).

**Sequência**:
1. O agente implementou as duas tarefas da proposta: expor `LeafClassifier.architecture` e adicionar a rota `GET /version`.
2. Adicionou 1 teste (`tests/test_version_api.py`) e rodou a suíte completa: **55/55 testes passaram**.
3. **O agente parou aqui**, sem commitar, e apresentou o diff pendente (3 arquivos) explicitamente como um checkpoint bloqueado, esperando decisão humana antes de prosseguir.
4. A decisão foi solicitada com as três opções previstas (aprovar / editar / rejeitar).

## Decisão tomada

**Aprovar como está**, sem edições. O commit `83dddea` só foi criado depois dessa aprovação explícita.

## Papel humano assumido

Papel de **revisora/aprovadora técnica** (Danielle, autora do projeto): avaliar se o endpoint proposto é seguro para expor publicamente (rota sem autenticação, mas só expõe metadados não sensíveis — versão da API e nome da arquitetura do modelo, nada de dados de usuário ou de infraestrutura) e se o teste automatizado cobre o comportamento esperado, antes de autorizar a entrada do código em `main`.

**Justificativa da aprovação**: o endpoint não expõe informação sensível, os testes passam, e o comportamento bate exatamente com o que foi especificado na proposta OpenSpec da Etapa 1 — não havia motivo para editar ou rejeitar.
