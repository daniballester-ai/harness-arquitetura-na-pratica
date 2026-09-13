# 0001-manter-monolito-modular

## Contexto

O serviço de inferência (`src/inference_service/`) cresceu ao longo desta atividade (endpoint `/version`, limite de upload, validação de feedback) e hoje tem 6 módulos e 10 rotas HTTP, todos rodando como um único processo/deploy. A revisão arquitetural da Etapa 4 identificou dois pontos de acoplamento reais: `main.py` como um "controlador gordo" que concentra todas as rotas, e `auth.py` que acessa diretamente constantes privadas de `history.py` (mesmo arquivo SQLite) em vez de passar por uma API pública. Isso levanta a pergunta: o projeto deveria virar múltiplos serviços, ficar mais modular internamente, ou está no tamanho certo?

## Decisão

Manter o projeto como um **monolito modular único** (um processo, um deploy), sem extrair `auth` ou `history` como serviços separados. Em vez disso, aplicar duas refatorações leves dentro do próprio monolito:
1. Dividir `main.py` em roteadores por domínio (`APIRouter` do FastAPI), mantendo `main.py` só como ponto de montagem.
2. Expor uma função pública em `history.py` (ex.: `get_connection()`) para que `auth.py` deixe de importar `HISTORY_DIR`/`DB_PATH` diretamente.

## Consequências

**Ganhos:**
- Sem custo operacional de múltiplos serviços (rede, contrato entre serviços, consistência de dados distribuída) — apropriado para um time pequeno e um único ciclo de deploy.
- O acoplamento real identificado (`auth` lendo o "por dentro" de `history`) é corrigido na raiz, sem introduzir infraestrutura nova.
- `main.py` deixa de crescer indefinidamente a cada endpoint novo, sem precisar de um novo serviço para isso.

**Perdas / riscos aceitos:**
- Não há isolamento de falha entre autenticação, histórico e inferência: um bug ou pico de carga em qualquer parte afeta o processo inteiro. Aceitável no volume atual (uso didático/demonstração), mas precisaria ser revisitado se o tráfego ou o time crescerem.
- A divisão em roteadores por domínio ainda não resolve acoplamento de dados (todos continuam no mesmo SQLite) — é uma melhoria de organização de código, não de arquitetura de dados. Se no futuro `history` precisar de um banco diferente de `auth`, a decisão precisará ser revisitada.
