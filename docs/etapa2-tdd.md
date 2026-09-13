# Etapa 2 — TDD como Guard-Rail

## Ciclo Red-Green-Refactor (evidência)

Tarefa: limite máximo de tamanho de upload no `POST /predict` (8MB).

1. **RED** — commit `98bbe50`: `tests/test_predict_size_limit.py` escrito **antes** da implementação, com 3 casos (arquivo acima do limite → 413, arquivo no limite → 200, arquivo vazio → 400, este último cobrindo comportamento já existente como guarda de regressão). Rodar `pytest` nesse ponto falha na coleta (`ImportError: cannot import name 'MAX_UPLOAD_BYTES'`) — a feature simplesmente não existe ainda.
2. **GREEN** — commit `fa2f604`: implementação mínima em `src/inference_service/main.py` (uma constante + uma checagem de tamanho antes da decodificação da imagem). Os 3 testes passam, e a suíte inteira (52 testes) continua verde.
3. **Refactor** — não foi necessário: a implementação já nasceu mínima (uma constante + uma guarda, seguindo o padrão da checagem de `content_type` logo acima no mesmo arquivo).

## Investigação de ferramenta de enforcement: tdd-guard

**Não foi possível instalar** neste ambiente: a instalação oficial (`/plugin marketplace add nizos/tdd-guard` → `/plugin install tdd-guard@tdd-guard` → `/tdd-guard:setup`) depende do binário `claude` (CLI standalone) para gerenciar plugins/marketplaces; esta sessão roda dentro do harness de uma extensão de IDE, sem esse binário disponível (`claude: command not found`). Documentando como se comportaria, a partir da documentação oficial (`docs/installation.md`, `docs/configuration.md` do repositório `nizos/tdd-guard`):

- **O que é**: um hook do Claude Code que bloqueia (a) implementação sem um teste falhando primeiro, (b) código que vai além do que os testes atuais exigem ("over-implementation"), e (c) violações de regras de lint durante o refactor.
- **Como se integraria neste projeto (Python/pytest)**:
  1. Instalar globalmente (`npm install -g tdd-guard`, requer Node 22+ — disponível nesta máquina) e o reporter Python: `pip install tdd-guard-pytest`.
  2. Registrar hooks `PreToolUse`, `UserPromptSubmit` e `SessionStart` no `.claude/settings.json`, cada um invocando o comando `tdd-guard`.
  3. Configurar `pyproject.toml` com `tdd_guard_project_root = "C:/Fitec/harness-arquitetura-na-pratica"` (necessário porque os testes rodam a partir da raiz do repo).
  4. O reporter grava resultados de teste em `.claude/tdd-guard/data/test.json` a cada execução do `pytest`; o hook `PreToolUse` lê esse arquivo antes de permitir uma edição de código, decidindo se há um teste falhando que justifique a mudança.
- **Como se comportaria no nosso cenário**: ao tentar o passo GREEN desta etapa (adicionar `MAX_UPLOAD_BYTES` e a checagem em `main.py`), o hook consultaria `test.json`, veria os 3 testes de `test_predict_size_limit.py` falhando (fase RED já registrada), e permitiria a edição. Se eu tentasse pular direto para a implementação sem antes rodar os testes falhando (ou sem tê-los escrito), o hook bloquearia a edição, exigindo o teste primeiro. Também bloquearia se eu tentasse implementar mais do que os testes pedem (ex.: adicionar um limite configurável por variável de ambiente sem teste cobrindo isso).
- **Limitação notável da própria ferramenta**: a documentação menciona que o projeto está evoluindo para um sucessor ("Probity"), com o TDD Guard original ainda mantido mas não mais o foco de novos recursos.

## Comparação: tarefa com TDD × tarefa sem TDD

| | Com TDD (limite de upload) | Sem TDD (validação de `prediction_id`) |
|---|---|---|
| Ordem | Teste escrito e falhando (RED) antes de qualquer código | Código escrito e verificado manualmente (script solto), testes só depois |
| Casos de borda cobertos **antes** de considerar a tarefa pronta | 3, pensados durante a escrita do teste: acima do limite, no limite exato, arquivo vazio (regressão) | 0 — a implementação foi considerada "pronta" após só um teste manual ad-hoc (`prediction_id=0` e `-5`) |
| Casos de borda cobertos **no total**, incluindo os testes escritos depois | 3 | 2 (zero, negativo) |
| O que ficou de fora | — | Nenhum teste garante que um `prediction_id` positivo válido continua funcionando após a mudança (regressão); nenhum teste cobre a interação entre a nova checagem e os erros 404/409 já existentes (ordem das validações) |
| Qualidade percebida | Mais alta: a lista de casos de teste *é* a especificação do comportamento esperado, escrita antes de qualquer viés de "já sei como implementei" | Mais baixa: os dois testes escritos depois só confirmam o que o código já fazia, sem forçar a pensar no que ele *deveria* fazer nos limites |

**O que a comparação revelou**: escrever o teste primeiro obriga a enumerar os casos de borda como parte do próprio ato de especificar a tarefa — antes de existir qualquer código para "confirmar". Sem TDD, os testes (quando escritos) tendem a apenas validar o caminho que o código já percorre, e é fácil esquecer o caso de regressão (o comportamento anterior continua correto?) porque a atenção já está em outro lugar. A diferença não apareceu tanto no tempo total (as duas rodadas ficaram na mesma ordem de grandeza, alguns minutos), mas na cobertura: 3 casos pensados de propósito vs. 2 casos lembrados depois, faltando o de regressão.
