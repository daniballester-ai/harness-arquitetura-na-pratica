# Etapa 5 — Diagrama de arquitetura (duas versões)

## Versão 1 — prompt simples ("gere um diagrama C4 de contêiner da arquitetura atual")

```mermaid
C4Container
    title Diagrama de Contêiner — Harness Arquitetura na Prática

    Person(user, "Cliente da API", "Usuário ou frontend que consome a API")

    System_Boundary(system, "Serviço de Inferência") {
        Container(api, "API FastAPI", "Python/FastAPI", "Expõe predict, history, stats, auth, feedback")
        Container(model, "Modelo ML", "PyTorch", "EfficientNet-B0 carregado em memória")
        ContainerDb(db, "SQLite", "Arquivo .db", "Histórico de predições e usuários")
        Container(frontend, "Frontend estático", "HTML/JS", "Upload de imagem e visualização")
    }

    Rel(user, api, "Chama via HTTP")
    Rel(api, model, "Usa para inferência")
    Rel(api, db, "Lê/grava")
    Rel(api, frontend, "Serve arquivos estáticos")
```

**O que essa versão comunica bem**: a visão de alto nível de "quem fala com quem" e que existe um único serviço com 4 contêineres lógicos. Boa para alguém de fora do time entender o sistema em 10 segundos.

**O que ela não comunica**: não mostra os módulos internos da API (`main`, `auth`, `history`, `model`, `schemas`) nem o ponto de acoplamento real identificado na Etapa 4 (auth acessando o armazenamento de history diretamente). Para quem já conhece o sistema e quer decidir sobre refatoração, essa versão é rasa demais.

## Versão 2 — prompt com mais contexto (alimentado com o resultado real da Etapa 4) + ajuste manual

```mermaid
flowchart TB
    user["Cliente da API<br/>(browser / script)"]

    subgraph api["API FastAPI (main.py) — 302 linhas, 10 rotas"]
        direction TB
        auth["auth.py<br/>login/registro/sessão"]
        history["history.py<br/>predições + stats<br/>(dono do SQLite)"]
        model["model.py<br/>EfficientNet-B0<br/>(isolado, 0 deps internas)"]
        schemas["schemas.py<br/>DTOs Pydantic<br/>(isolado)"]
    end

    db[("SQLite<br/>history.db")]

    user -->|"HTTP"| api
    api --> model
    api --> schemas
    api --> auth
    api --> history
    auth -.->|"⚠ lê HISTORY_DIR/DB_PATH\ndiretamente (acoplamento\nde armazenamento, não de API)"| history
    history --> db
    auth --> db

    style auth fill:#3E8E4E22,stroke:#3E8E4E
    style history fill:#3E8E4E22,stroke:#3E8E4E
    style model fill:#ffffff11,stroke:#888
    style schemas fill:#ffffff11,stroke:#888
```

**O que mudou**: pedi o diagrama de novo citando explicitamente os dois pontos de acoplamento da Etapa 4 (o "controlador gordo" e o acesso direto de `auth` ao armazenamento de `history`) e ajustei manualmente o resultado gerado para: (a) mostrar os módulos internos da API, não só a caixa "API" genérica; (b) destacar visualmente (linha tracejada + aviso) a aresta problemática `auth → history` que motivou a decisão do ADR 0001; (c) anotar tamanho/isolamento de cada módulo, que é exatamente o dado usado na decisão arquitetural.

**Comparação — qual comunica melhor**: para uma visão gerencial ou de onboarding rápido, a **Versão 1** (C4 clássico) é melhor: menos elementos, mensagem clara em poucos segundos. Para justificar e documentar a decisão arquitetural desta atividade (ADR 0001), a **Versão 2** comunica muito melhor, porque o próprio diagrama já aponta o problema que motivou a decisão — sem ele, o leitor do ADR precisaria confiar só no texto. A lição prática: o nível de detalhe certo do diagrama depende de para quem e para quê ele é feito; um diagrama "correto" genérico não necessariamente serve ao propósito de documentar uma decisão específica.
