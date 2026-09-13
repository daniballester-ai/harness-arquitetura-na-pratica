# Etapa 4 — Revisão Arquitetural com Apoio de IA

## Resumo da arquitetura atual (gerado a partir do código real)

O projeto é um monolito pequeno de 6 módulos Python (881 linhas no total) dentro de `src/inference_service/`:

| Módulo | Linhas | Depende de (interno) | Responsabilidade |
|---|---|---|---|
| `main.py` | 302 | `auth`, `history`, `model`, `schemas` | Todas as rotas HTTP (10 endpoints: predict, history, stats, auth, feedback, export CSV, frontend estático) |
| `history.py` | 246 | — (nenhum) | Persistência de predições em SQLite; contagens/estatísticas |
| `auth.py` | 125 | `history` (só para reutilizar `HISTORY_DIR`/`DB_PATH`) | Registro/login/sessão de usuário, hashing de senha (bcrypt) |
| `model.py` | 102 | — (nenhum) | Carregamento do modelo EfficientNet-B0, pré-processamento, inferência |
| `schemas.py` | 50 | — (nenhum) | DTOs Pydantic das respostas da API |
| `verify_api.py` | 56 | `main` | Script de smoke-test manual (não faz parte do runtime) |

**Diagrama de dependências:**

```
main.py ──► auth.py ──► history.py
   │                       ▲
   ├──────────────────────►│
   ├──► model.py
   └──► schemas.py
```

`model.py` e `schemas.py` são completamente isolados (zero dependências internas) — o núcleo de ML e os contratos de dados não conhecem nada do resto do sistema. `history.py` também é isolado, com seu próprio SQLite.

## Pontos de acoplamento identificados

1. **`main.py` é um "controlador gordo"**: as 10 rotas HTTP, mais validação de entrada, mapeamento de erros e formatação de CSV, tudo em um único arquivo de 302 linhas. Funciona bem no tamanho atual, mas cresce a cada endpoint novo (já cresceu de ~190 para 302 linhas ao longo desta atividade, com `/version` e a checagem de tamanho de upload).
2. **`auth.py` acopla-se a `history.py` por armazenamento compartilhado, não por API explícita**: `auth.py` lê diretamente `history.HISTORY_DIR` e `history.DB_PATH` para montar sua própria conexão SQLite, em vez de passar por uma função pública de `history.py`. Isso significa que uma mudança no esquema de armazenamento de `history.py` (ex: trocar de SQLite para outro storage) quebraria `auth.py` silenciosamente, sem estar explícito em nenhum contrato entre os dois módulos.
3. **Nenhuma camada de serviço separada do HTTP**: a lógica de negócio (regras de validação, decisão de incerteza, formatação de export) mora dentro das próprias funções de rota do FastAPI, em vez de ser delegada a uma camada intermediária testável independentemente do framework HTTP.

## Decisão arquitetural

**O projeto está no tamanho certo para sua fase atual — não extrair serviço(s), não aumentar modularidade agora.**

**Critérios usados**:
- **Tamanho e taxa de mudança conjunta**: 881 linhas, um único desenvolvedor (mais um colega, ocasionalmente), e todos os módulos evoluem juntos (cada feature nova, como a sinalização de incerteza ou o histórico, toca `main.py` + `history.py` ou `model.py` na mesma mudança). Não há sinal de que módulos diferentes evoluam em ritmos ou por motivos diferentes o suficiente para justificar deploys independentes.
- **Custo operacional de extrair um serviço**: separar `auth` ou `history` em um serviço próprio (rede, contrato de API, consistência de dados entre serviços) adicionaria complexidade operacional real (mais um processo, mais uma superfície de falha, latência de rede) sem nenhum ganho concreto no estágio atual (um único time pequeno, sem necessidade de escalar cada parte de forma independente).
- **Acoplamento é real, mas é de encapsulamento, não de tamanho**: o problema em `auth.py`/`history.py` não é "o sistema é grande demais para um serviço só" — é que um módulo está lendo o "por dentro" do outro. Isso se resolve com refatoração leve (expor uma função pública em `history.py` para abrir a conexão, em vez de `auth.py` importar as constantes privadas), não com extração de serviço.

**Recomendação concreta, sem extrair serviço**:
1. Dividir `main.py` em roteadores por domínio (`APIRouter` do FastAPI): `auth_routes.py`, `predict_routes.py`, `history_routes.py`, `stats_routes.py`, mantendo `main.py` só como o ponto de montagem da aplicação. Isso ataca o ponto 1 sem introduzir um novo processo/serviço.
2. Substituir o acesso direto de `auth.py` às constantes de `history.py` por uma função pública (`history.get_connection()`), fechando o ponto 2.

Esses dois ajustes reduzem o acoplamento real encontrado, mantendo o sistema como um monolito modular — a decisão certa para o tamanho e o estágio atual do projeto, evitando o custo de uma extração de serviço prematura.
