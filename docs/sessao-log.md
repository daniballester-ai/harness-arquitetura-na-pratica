# Log da sessão do agente — Harness e Arquitetura na Prática

Transcript resumido (extraído do JSONL bruto da sessão do Claude Code), do início desta atividade (Etapa 1) até o Relatório Final (Etapa 8). Mensagens de usuário e do agente na íntegra (respostas do agente truncadas em ~2000 caracteres); chamadas de ferramenta aparecem só pelo nome. Não editado além disso.

---



### [2026-09-13T20:31:15.139Z] USUÁRIO
agora temos a atividade @"/g:/Meu Drive/Doutorado_PPGTI/AULAS/sem_02_202602/02_Topicos_Avancados_Eng_Software_2/atividade_assincrona_03/Aula6_Pratica_Assincrona_Harness_Arquitetura.docx.pdf" para fazer.

como já fizemos o projeto final, o que acha de eu fazer um novo repositorio no github para esta atividade.


_[2026-09-13T20:31:42.921Z] ferramenta usada: `Read`_

### [2026-09-13T20:32:18.799Z] AGENTE
Acho uma boa ideia, sim — com uma ressalva. O enunciado até permite reaproveitar um projeto existente, e o `cacau-fito` te daria código real (API, specs, testes) pra Etapa 4 (revisão arquitetural) ficar mais rica desde o início. Mas esse repositório já está com um histórico bem carregado e misturado (duas disciplinas, várias mudanças OpenSpec não relacionadas rolando em paralelo), e boa parte desta atividade (hooks, TDD, worktrees, ADR) é prática de harness genérica, não específica do CacauFito — um repositório novo te dá um histórico de commits limpo e fácil de avaliar (que é literalmente um dos entregáveis da Etapa 7), sem arriscar bagunçar o projeto real com hooks de teste e experimentos de paralelismo.

Meu palpite: repositório novo, mas eu importaria/copiaria uma fatia pequena e real de código (por exemplo, só a API do CacauFito) pra dentro dele, pra Etapa 4 ter algo de arquitetura de verdade pra analisar, em vez de partir de um projeto vazio.

Quer que eu já crie a estrutura desse novo repositório?


### [2026-09-13T20:32:51.508Z] USUÁRIO
quero sim


_[2026-09-13T20:33:18.438Z] ferramenta usada: `AskUserQuestion`_

_[2026-09-13T20:34:18.395Z] ferramenta usada: `Read`_

_[2026-09-13T20:34:39.966Z] ferramenta usada: `Bash`_

_[2026-09-13T20:34:57.950Z] ferramenta usada: `Bash`_

_[2026-09-13T20:35:17.257Z] ferramenta usada: `Bash`_

_[2026-09-13T20:35:44.140Z] ferramenta usada: `Bash`_

_[2026-09-13T20:36:00.735Z] ferramenta usada: `Bash`_

_[2026-09-13T20:36:19.285Z] ferramenta usada: `Bash`_

### [2026-09-13T20:36:35.354Z] AGENTE
Bom, tudo autocontido (cria os diretórios sozinho). Vou montar o novo repositório agora.


_[2026-09-13T20:36:35.849Z] ferramenta usada: `Bash`_

_[2026-09-13T20:36:52.141Z] ferramenta usada: `Bash`_

_[2026-09-13T20:37:08.438Z] ferramenta usada: `Bash`_

_[2026-09-13T20:37:25.053Z] ferramenta usada: `Bash`_

_[2026-09-13T20:37:40.231Z] ferramenta usada: `Bash`_

_[2026-09-13T20:39:00.395Z] ferramenta usada: `Bash`_

_[2026-09-13T20:39:17.601Z] ferramenta usada: `Bash`_

_[2026-09-13T20:39:33.455Z] ferramenta usada: `Bash`_

_[2026-09-13T20:39:48.623Z] ferramenta usada: `Bash`_

_[2026-09-13T20:40:08.535Z] ferramenta usada: `Bash`_

_[2026-09-13T20:40:22.248Z] ferramenta usada: `Bash`_

### [2026-09-13T20:40:36.879Z] AGENTE
Ótimo, código copiado. Vou verificar que a API sobe e os testes passam antes de criar o repositório git.


_[2026-09-13T20:40:37.400Z] ferramenta usada: `Bash`_

### [2026-09-13T20:41:17.784Z] AGENTE
Só falta `samples/`, usado por alguns testes. Vou copiar.


_[2026-09-13T20:41:18.431Z] ferramenta usada: `Bash`_

_[2026-09-13T20:41:33.735Z] ferramenta usada: `Bash`_

### [2026-09-13T20:42:09.963Z] AGENTE
Todos os 49 testes passam. Vou também conferir que a API sobe de verdade.


_[2026-09-13T20:42:11.052Z] ferramenta usada: `Bash`_

_[2026-09-13T20:42:24.717Z] ferramenta usada: `Bash`_

### [2026-09-13T20:42:44.621Z] AGENTE
API confirmada rodando. Vou parar esse processo de teste e seguir com a estrutura do repositório.


_[2026-09-13T20:42:45.632Z] ferramenta usada: `Bash`_

### [2026-09-13T20:43:06.234Z] AGENTE
Parado. Agora vou criar os arquivos de suporte (README, .gitignore, requirements) e iniciar o repositório git.


_[2026-09-13T20:43:07.368Z] ferramenta usada: `Bash`_

_[2026-09-13T20:43:23.616Z] ferramenta usada: `Write`_

_[2026-09-13T20:43:40.605Z] ferramenta usada: `Write`_

_[2026-09-13T20:44:10.906Z] ferramenta usada: `Write`_

_[2026-09-13T20:44:30.569Z] ferramenta usada: `Write`_

_[2026-09-13T20:44:48.657Z] ferramenta usada: `Write`_

_[2026-09-13T20:45:06.446Z] ferramenta usada: `Bash`_

### [2026-09-13T20:45:22.103Z] AGENTE
Agora inicio o git e faço o primeiro commit.


_[2026-09-13T20:45:22.744Z] ferramenta usada: `Bash`_

_[2026-09-13T20:45:38.482Z] ferramenta usada: `Bash`_

_[2026-09-13T20:45:55.065Z] ferramenta usada: `Bash`_

### [2026-09-13T20:46:13.217Z] AGENTE
Config é local por repositório. Vou aplicar o mesmo no novo repo.


_[2026-09-13T20:46:13.887Z] ferramenta usada: `Bash`_

### [2026-09-13T20:46:30.574Z] AGENTE
Tudo certo, staged. Vou fazer o primeiro commit.


_[2026-09-13T20:46:33.419Z] ferramenta usada: `Bash`_

### [2026-09-13T20:46:51.898Z] AGENTE
Vou renomear a branch para `main` e criar o repositório no GitHub (público, via `gh`).


_[2026-09-13T20:46:52.820Z] ferramenta usada: `Bash`_

### [2026-09-13T20:47:09.660Z] AGENTE
Autenticado. Vou criar o repositório no GitHub e já enviar o primeiro commit.


_[2026-09-13T20:47:10.855Z] ferramenta usada: `Bash`_

_[2026-09-13T20:47:29.034Z] ferramenta usada: `Bash`_

### [2026-09-13T20:47:58.647Z] AGENTE
## Repositório criado e publicado

**https://github.com/daniballester-ai/harness-arquitetura-na-pratica** (público)

**O que já está lá:**
- `src/inference_service/` — a API completa de inferência do CacauFito (predict, history, stats, auth, feedback, export CSV), copiada como base de código real.
- `tests/` — os 49 testes, **todos passando** nesta cópia isolada.
- `models/`, `frontend/static/`, `samples/` — o necessário pra API subir e os testes rodarem de verdade (validei com `pytest` e subindo o servidor).
- `README.md` com checklist das 8 etapas da atividade.
- `docs/sessao-log.md` (placeholder pra Etapa 3) e `docs/adr/` (placeholder pra Etapa 5).
- Primeiro commit real, não um "commit gigante único" — a partir de agora, cada etapa que fizermos vira commit(s) separados, construindo o histórico que a Etapa 7 pede.

**Pronto para começar a Etapa 1** (harness mínimo: dois modos de autonomia + 1 hook de risco específico do projeto) quando você quiser seguir.


### [2026-09-13T20:48:35.374Z] USUÁRIO
pode começar


### [2026-09-13T20:49:23.258Z] AGENTE
Vou começar pela Etapa 1. Primeiro, a comparação entre dois modos de autonomia, usando uma tarefa pequena e real: **adicionar um endpoint `GET /version`** que retorna a versão da API e a arquitetura do modelo.

**Rodada 1 — modo direto (auto-accept, sem plano prévio)**: vou implementar direto, cronometrando.


_[2026-09-13T20:49:23.460Z] ferramenta usada: `Bash`_

_[2026-09-13T20:49:38.017Z] ferramenta usada: `Read`_

_[2026-09-13T20:49:56.110Z] ferramenta usada: `Edit`_

_[2026-09-13T20:50:43.935Z] ferramenta usada: `Bash`_

_[2026-09-13T20:51:03.439Z] ferramenta usada: `Bash`_

_[2026-09-13T20:51:22.262Z] ferramenta usada: `Edit`_

### [2026-09-13T20:51:38.964Z] AGENTE
Agora testo rapidamente:


_[2026-09-13T20:51:39.767Z] ferramenta usada: `Bash`_

_[2026-09-13T20:52:01.580Z] ferramenta usada: `Bash`_

### [2026-09-13T20:52:20.004Z] AGENTE
Rodada 1 concluída: **~2min38s** (158s), incluindo achar e corrigir um bug no meio do caminho (o `LeafClassifier` não expunha `architecture`) sem parar para confirmar nada comigo. Vou reverter e repetir em modo de plano.


_[2026-09-13T20:52:20.579Z] ferramenta usada: `Bash`_

### [2026-09-13T20:52:36.840Z] AGENTE
Reverto confirmado. Agora **Rodada 2 — modo de planejamento** (apresento o plano antes de tocar no código).


_[2026-09-13T20:52:37.258Z] ferramenta usada: `ToolSearch`_

_[2026-09-13T20:52:51.525Z] ferramenta usada: `Bash`_

_[2026-09-13T20:53:57.928Z] ferramenta usada: `EnterPlanMode`_

_[2026-09-13T20:54:18.651Z] ferramenta usada: `Write`_

_[2026-09-13T20:54:33.800Z] ferramenta usada: `ExitPlanMode`_

### [2026-09-13T20:58:24.870Z] AGENTE
Entendido — em vez de eu implementar direto a partir do plano, vamos formalizar como uma proposta OpenSpec primeiro. Isso já é, em si, um dado interessante pra comparação do Etapa 1: o modo de plano deu espaço pra você redirecionar a tarefa inteira antes de qualquer código ser tocado.


_[2026-09-13T20:58:26.699Z] ferramenta usada: `Skill`_

### [2026-09-13T20:58:28.560Z] USUÁRIO
Base directory for this skill: c:\Fitec\CacauFito\.claude\skills\openspec-propose

Propose a new change - create the change and generate all artifacts in one step.

**Planning boundary**: This workflow creates planning artifacts only. The user request that selected or triggered this workflow authorizes planning only, even if it asks to build or fix something. Do not edit project code. After the planning artifacts are complete, stop. Do not start implementation in the same response, even if the initial request asks for it. Wait for a new user request after the artifacts are presented; then start the apply workflow.

I'll create a change with the artifacts your schema defines. With the default spec-driven schema that is:
- proposal.md (what & why)
- `specs/<capability-path>/spec.md` (what the system must do - a delta, not the main spec)
- design.md (how)
- tasks.md (implementation steps)

`<capability-path>` is the spec directory relative to `specs/` (for example, `user-auth` or `identity/user-auth`). Preserve an existing capability's full path and follow the project's established organization for new capabilities.

When the user is ready to implement, they must start the apply workflow explicitly.

---

**Store selection:** If the user names a store (a store is a standalone OpenSpec repo registered on this machine) or the work lives in one, run `openspec store list --json` to discover registered store ids, then pass `--store <id>` on the commands that read or write specs and changes (`new change`, `status`, `instructions`, `list`, `show`, `validate`, `archive`, `doctor`, `context`, `schemas`, `view`). Once selected, treat `--store <id>` as sticky for the rest of the workflow. Every unscoped example of those commands below is shorthand: before running it, append the flag. For example, run `openspec status --change "<name>" --json --store "<id>"`, not the unscoped form shown below. Other commands do not take the flag. Hints printed by commands already carry the flag; keep it on follow-ups. Without a store, commands act on the nearest local `openspec/` root.

**Input**: The user's request should include a change name (kebab-case) OR a description of what they want to build.

**Steps**

1. **Understand the request and clarify material ambiguity**

   If no clear input is provided, ask the user (open-ended, no preset options):
   > "What change do you want to work on? Describe what you want to build or fix."

   From their description, derive a kebab-case name (e.g., "add user authentication" → `add-user-auth`).

   **IMPORTANT**: Do NOT proceed without understanding what the user wants to build.

   If the request contains ambiguity that would materially affect scope, externally observable behavior, compatibility, or acceptance criteria, ask the user before creating the change. For minor details, make a reasonable assumption and record it in the planning artifacts.

2. **Determine the workflow schema**

   Use the configured default schema unless the user explicitly requests a different workflow.

   **Use a different schema only if the user:**
   - Explicitly requests a specific schema by name → use `--schema <schema-name>`
   - Asks to "show workflows" or asks "what workflows" exist → resolve the authoritative root by running `openspec context --json` from the current working directory. If the user explicitly selected a registered store, use `openspec context --json --store "<store-id>"`. Then run `openspec schemas --json` with its working directory set to the returned `root.path` and let them choose. This preserves roots selected by a local `store:` pointer or the global `defaultStore`; when a registered store was explicitly selected, append `--store "<store-id>"` to `openspec schemas --json` as well. If context reports only `no_openspec_root`, run `openspec schemas --json` from the current working directory instead. Do not use this fallback for invalid or unavailable stores.

   Otherwise, omit `--schema` to preserve the configured default.

3. **Create the change directory**

   Choose one schema form below. If a registered store is selected, append `--store "<store-id>"` to that command and each later OpenSpec command shown below that accepts `--store`.

   Using the configured default:
   ```bash
   openspec new change "<name>"
   ```

   Using an explicitly requested schema:
   ```bash
   openspec new change "<name>" --schema "<schema-name>"
   ```
   This creates a scaffolded change in the planning home resolved by the CLI with `.openspec.yaml`.

4. **Get the artifact build order**
   ```bash
   openspec status --change "<name>" --json
   ```
   Parse the JSON to get:
   - `applyRequires`: array of artifact IDs needed before implementation (e.g., `["tasks"]`)
   - `artifacts`: list of all artifacts, each with its `status` and its `requires` edges (the artifact IDs it directly depends on)
   - `planningHome`, `changeRoot`, `artifactPaths`, and `actionContext`: path and scope context. Use these instead of assuming repo-local paths.

5. **Create every artifact in the required set**

   Use a todo list to track progress through the artifacts.

   Loop through artifacts in dependency order (artifacts with no pending dependencies first):

   a. **For each artifact that is `ready` (dependencies satisfied)**:
      - Get instructions:
        ```bash
        openspec instructions <artifact-id> --change "<name>" --json
        ```
      - The instructions JSON includes:
        - `context`: Project background (constraints for you - do NOT include in output)
        - `rules`: Artifact-specific rules (constraints for you - do NOT include in output)
        - `template`: The structure to use for your output file
        - `instruction`: Schema-specific guidance for this artifact type
        - `skipped`/`warning`: present when the change declares skip_specs and this artifact must NOT be created - stop and pick another artifact
        - `resolvedOutputPath`: Resolved path or pattern to write the artifact
        - `dependencies`: Completed artifacts to read for context
      - Read any completed dependency files for context - always re-read them from disk, even if you saw them earlier in the conversation (the user may have edited them)
      - If the `instruction` field delegates creation to a specific skill or command, invoke it to produce the artifact instead of writing the file yourself, then verify the artifact file exists at `resolvedOutputPath`
      - Otherwise create the artifact file using `template` as the structure and write it to `resolvedOutputPath`. If `resolvedOutputPath` is a glob, follow `instruction` to choose the concrete file path
      - Apply `context` and `rules` as constraints - but do NOT copy them into the file
      - Show brief progress: "Created <artifact-id>"

   b. **Continue until every artifact in the required set exists (not just `apply.requires`)**
      - After creating each artifact, re-run `openspec status --change "<name>" --json`
      - The required set is `applyRequires` plus every artifact reachable from those by following the `requires` edges in `status --json` - walk them transitively (spec-driven closes over proposal, specs, design, tasks). Leave artifacts outside that set alone
      - `status` is file-existence only, so an `applyRequires` artifact reading `done` does NOT mean its dependencies exist - writing `tasks.md` early marks `tasks` done while `specs` was never written. Use each artifact's `requires` edges, not its `status`, to build the required set: a `done` artifact still lists what it depends on
      - An artifact already reading `status: "skipped"` is satisfied: the change declares `skip_specs` in `.openspec.yaml`, so its files must NOT exist. Never try to create one
      - Create every artifact in the required set that is missing, then re-check - creating one can unblock others
      - Skip one only when `status` already reports it `skipped`, or when its own `instruction` says it is conditional: run `openspec instructions <artifact-id> --change "<name>" --json` and skip only if its `instruction` field marks it optional (e.g. "create only if..."). Spec-driven's `design.md` qualifies; `specs` qualifies only via the `skipped` status above, never by your own judgment. Tell the user, and do not reconsider it
      - Dependencies are enablers, not gates: if a required artifact is still `blocked` only because you skipped a conditional dependency, write it anyway
      - Stop when every artifact in the required set is `done`, `skipped`, or was deliberately skipped

   c. **If an artifact requires user input** (unclear context):
      - Ask the user to clarify
      - Then continue with creation

6. **Show final status**
   ```bash
   openspec status --change "<name>"
   ```

**Output**

After completing all artifacts, summarize:
- Change name and location
- List of artifacts created with brief descriptions, plus any conditional artifact you skipped and why
- What's ready: "All artifacts needed for implementation are ready."
- Prompt: "The artifacts are ready for review. When you are ready, run `/opsx:apply` or ask me to apply this change."

**Artifact Creation Guidelines**

- Follow the `instruction` field from `openspec instructions` for each artifact type - it is the authoritative guidance, even for familiar artifact names
- If the `instruction` field directs you to use a specific skill or command to create the artifact, invoke it instead of writing the artifact directly
- The schema defines what each artifact should contain - follow it
- Read dependency artifacts for context before creating new ones
- Use `template` as the structure for your output file - fill in its sections
- **IMPORTANT**: `context` and `rules` are constraints for YOU, not content for the file
  - Do NOT copy `<context>`, `<rules>`, `<project_context>` blocks into the artifact
  - These guide what you write, but should never appear in the output

**Guardrails**
- The request that invoked this workflow authorizes planning only. Any implementation or apply instruction in that request does not carry forward. Do NOT implement the change, start the apply workflow, or edit project code during this workflow. After presenting the artifacts, stop and wait for a new user request to start the apply workflow
- Create every artifact the apply phase transitively depends on, not just the ids listed in `apply.requires`
- Always read dependency artifacts before creating a new one - re-read from disk, not from conversation memory (files may have changed since you last saw them)
- Ask about ambiguities that would materially change scope, externally observable behavior, compatibility, or acceptance criteria; for minor details, make reasonable assumptions and record them
- If a change with that name already exists, ask if user wants to continue it or create a new one
- Verify each artifact file exists after writing before proceeding to next


ARGUMENTS: No repositório C:\Fitec\harness-arquitetura-na-pratica (ainda sem OpenSpec inicializado), crie a proposta para adicionar um endpoint GET /version na API de inferência (src/inference_service/main.py), que retorna a versão da API e a arquitetura do modelo carregado (classifier.architecture, hoje não exposto em LeafClassifier — precisa expor mapping["architecture"] como self.architecture no __init__ de model.py). Nome da mudança: add-version-endpoint.


_[2026-09-13T20:58:44.239Z] ferramenta usada: `Bash`_

_[2026-09-13T20:59:02.927Z] ferramenta usada: `Bash`_

_[2026-09-13T20:59:25.235Z] ferramenta usada: `Bash`_

_[2026-09-13T20:59:46.226Z] ferramenta usada: `Write`_

_[2026-09-13T21:12:21.666Z] ferramenta usada: `Bash`_

_[2026-09-13T21:12:40.805Z] ferramenta usada: `Write`_

_[2026-09-13T21:16:01.807Z] ferramenta usada: `Bash`_

### [2026-09-13T21:16:19.558Z] AGENTE
None of those apply here — skipping `design.md` deliberately (trivial, single-file, no new deps/architecture decisions). Moving to `tasks.md`.


_[2026-09-13T21:16:20.297Z] ferramenta usada: `Bash`_

_[2026-09-13T21:16:42.315Z] ferramenta usada: `Bash`_

_[2026-09-13T21:17:03.738Z] ferramenta usada: `Write`_

_[2026-09-13T21:20:41.772Z] ferramenta usada: `Bash`_

_[2026-09-13T21:21:26.444Z] ferramenta usada: `Bash`_

### [2026-09-13T21:22:11.784Z] AGENTE
## Proposta OpenSpec criada

`openspec/changes/add-version-endpoint/` no repositório `harness-arquitetura-na-pratica`, com:
- **proposal.md** — por que e o quê (endpoint `/version` somático, sem dependências novas)
- **specs/leaf-inference-service-version/spec.md** — requisito formal com cenário de aceite
- **tasks.md** — 2 tarefas (expor `architecture` no `LeafClassifier`, adicionar a rota)
- **design.md** deliberadamente pulado (mudança trivial, sem decisão arquitetural real)

Conforme a fronteira do workflow de proposta: parei aqui, sem implementar. Quando você quiser seguir, é só pedir.

## Registro para a Etapa 1 (comparação de autonomia)

| | Rodada 1 — modo direto (auto-accept) | Rodada 2 — modo de plano |
|---|---|---|
| **Tempo** | ~2min38s (158s) | ~28min35s (1715s) |
| **O que aconteceu** | Implementei direto; no meio do caminho descobri que `LeafClassifier` não expunha `architecture` e corrigi sozinho, sem pausa | Escrevi um plano, pedi aprovação (`ExitPlanMode`) — você rejeitou e redirecionou a tarefa inteira pra virar uma proposta OpenSpec formal antes de qualquer código |
| **Sensação de controle** | Baixa: só vi o resultado pronto (diff) depois de feito | Alta: você interceptou *antes* da implementação e mudou o processo inteiro, não só o conteúdo |
| **Risco percebido** | Maior: um bug real (atributo faltando) só apareceu porque eu segui direto; se eu não tivesse notado, teria "funcionado" com um detalhe quebrado sem ninguém revisar antes | Menor: nada foi tocado no código ainda; o risco fica represado na camada de planejamento, não no código rodando |

Essa foi a primeira etapa registrada. Quer que eu escreva isso em `docs/` do repositório (junto com o restante da Etapa 1: o hook de guardrail) antes de avançar, ou já parto pra criar o hook?


### [2026-09-13T21:23:00.437Z] USUÁRIO
escreva em docs e depois prossiga


_[2026-09-13T21:23:29.710Z] ferramenta usada: `Write`_

### [2026-09-13T21:42:01.341Z] AGENTE
Agora commito isso e a proposta OpenSpec, e sigo para o hook.


_[2026-09-13T21:42:01.766Z] ferramenta usada: `Bash`_

_[2026-09-13T21:42:23.072Z] ferramenta usada: `Bash`_

### [2026-09-13T21:42:45.198Z] AGENTE
Agora a parte 2 da Etapa 1: um hook que bloqueia um risco real e específico deste projeto — **apagar ou sobrescrever o artefato do modelo treinado** (`models/cacao_leaf_classifier.pt`), que não tem como ser recriado sem os dados/notebook originais do CacauFito.


_[2026-09-13T21:42:47.509Z] ferramenta usada: `Skill`_

### [2026-09-13T21:42:49.464Z] USUÁRIO
# Update Config Skill

Modify Claude Code configuration by updating settings.json files.

## When Hooks Are Required (Not Memory)

If the user wants something to happen automatically in response to an EVENT, they need a **hook** configured in settings.json. Memory/preferences cannot trigger automated actions.

**These require hooks:**
- "Before compacting, ask me what to preserve" → PreCompact hook
- "After writing files, run prettier" → PostToolUse hook with Write|Edit matcher
- "When I run bash commands, log them" → PreToolUse hook with Bash matcher
- "Always run tests after code changes" → PostToolUse hook

**Hook events:** PreToolUse, PostToolUse, PreCompact, PostCompact, Stop, Notification, SessionStart

## CRITICAL: Read Before Write

**Always read the existing settings file before making changes.** Merge new settings with existing ones - never replace the entire file.

## CRITICAL: Use AskUserQuestion for Ambiguity

When the user's request is ambiguous, use AskUserQuestion to clarify:
- Which settings file to modify (user/project/local)
- Whether to add to existing arrays or replace them
- Specific values when multiple options exist

## Decision: /config command vs Direct Edit

**Suggest the `/config` slash command** for these simple settings:
- `theme`, `editorMode`, `verbose`, `model`
- `language`, `alwaysThinkingEnabled`
- `permissions.defaultMode`

**Edit settings.json directly** for:
- Hooks (PreToolUse, PostToolUse, etc.)
- Complex permission rules (allow/deny arrays)
- Environment variables
- MCP server configuration
- Plugin configuration

## Workflow

1. **Clarify intent** - Ask if the request is ambiguous
2. **Read existing file** - Use Read tool on the target settings file
3. **Merge carefully** - Preserve existing settings, especially arrays
4. **Edit file** - Use Edit tool (if file doesn't exist, ask user to create it first)
5. **Confirm** - Tell user what was changed

## Merging Arrays (Important!)

When adding to permission arrays or hook arrays, **merge with existing**, don't replace:

**WRONG** (replaces existing permissions):
```json
{ "permissions": { "allow": ["Bash(npm *)"] } }
```

**RIGHT** (preserves existing + adds new):
```json
{
  "permissions": {
    "allow": [
      "Bash(git *)",      // existing
      "Edit(.claude)",    // existing
      "Bash(npm *)"       // new
    ]
  }
}
```

## Settings File Locations

Choose the appropriate file based on scope:

| File | Scope | Git | Use For |
|------|-------|-----|---------|
| `~/.claude/settings.json` | Global | N/A | Personal preferences for all projects |
| `.claude/settings.json` | Project | Commit | Team-wide hooks, permissions, plugins |
| `.claude/settings.local.json` | Project | Gitignore | Personal overrides for this project |

Settings load in order: user → project → local (later overrides earlier).

## Settings Schema Reference

### Permissions
```json
{
  "permissions": {
    "allow": ["Bash(npm *)", "Edit(.claude)", "Read"],
    "deny": ["Bash(rm -rf *)"],
    "ask": ["Edit(//etc/*)"],
    "defaultMode": "default" | "plan" | "acceptEdits" | "dontAsk",
    "additionalDirectories": ["/extra/dir"]
  }
}
```

**Permission Rule Syntax:**
- Exact match: `"Bash(npm run test)"`
- Prefix wildcard: `"Bash(git *)"` - matches `git`, `git status`, `git commit`, etc.
- Tool only: `"Read"` - allows all Read operations

### Environment Variables
```json
{
  "env": {
    "DEBUG": "true",
    "MY_API_KEY": "value"
  }
}
```

### Model & Agent
```json
{
  "model": "sonnet",  // or "fable", "opus", "haiku", full model ID
  "agent": "agent-name",
  "alwaysThinkingEnabled": true
}
```

### Attribution (Commits & PRs)
```json
{
  "attribution": {
    "commit": "Custom commit trailer text",
    "pr": "Custom PR description text"
  }
}
```
Set `commit` or `pr` to empty string `""` to hide that attribution.

### MCP Server Management
```json
{
  "enableAllProjectMcpServers": true,
  "enabledMcpjsonServers": ["server1", "server2"],
  "disabledMcpjsonServers": ["blocked-server"]
}
```

### Plugins
```json
{
  "enabledPlugins": {
    "formatter@anthropic-tools": true
  }
}
```
Plugin syntax: `plugin-name@source` where source is `claude-code-marketplace`, `claude-plugins-official`, or `builtin`.

### Other Settings
- `language`: Preferred response language (e.g., "japanese")
- `cleanupPeriodDays`: Days to keep transcripts before automatic cleanup (default: 30; minimum 1)
- `respectGitignore`: Whether to respect .gitignore (default: true)
- `spinnerTipsEnabled`: Show tips in spinner
- `timeFormat`: Clock format for times shown in the UI: "auto" (default), "12-hour", "24-hour", "24-hour-utc", or a strftime pattern such as "%H:%M"
- `timeZone`: IANA time zone for times shown in the UI, e.g. "UTC" (default: system time zone)
- `spinnerVerbs`: Customize spinner verbs (`{ "mode": "append" | "replace", "verbs": [...] }`)
- `spinnerTipsOverride`: Override spinner tips (`{ "excludeDefault": true, "tips": ["Custom tip"] }`)
- `syntaxHighlightingDisabled`: Disable diff highlighting


## Hooks Configuration

Hooks run commands at specific points in Claude Code's lifecycle.

### Hook Structure
```json
{
  "hooks": {
    "EVENT_NAME": [
      {
        "matcher": "ToolName|OtherTool",
        "hooks": [
          {
            "type": "command",
            "command": "your-command-here",
            "timeout": 60,
            "statusMessage": "Running..."
          }
        ]
      }
    ]
  }
}
```

### Hook Events

| Event | Matcher | Purpose |
|-------|---------|---------|
| PermissionRequest | Tool name | Run before permission prompt |
| PreToolUse | Tool name | Run before tool, can block |
| PostToolUse | Tool name | Run after successful tool |
| PostToolUseFailure | Tool name | Run after tool fails |
| Notification | Notification type | Run on notifications |
| Stop | - | Run when Claude stops (including clear, resume, compact) |
| PreCompact | "manual"/"auto" | Before compaction |
| PostCompact | "manual"/"auto" | After compaction (receives summary) |
| UserPromptSubmit | - | When user submits |
| SessionStart | - | When session starts |

**Common tool matchers:** `Bash`, `Write`, `Edit`, `Read`, `Glob`, `Grep`

### Hook Types

**1. Command Hook** - Runs a shell command:
```json
{ "type": "command", "command": "prettier --write $FILE", "timeout": 30 }
```

**2. Prompt Hook** - Evaluates a condition with LLM:
```json
{ "type": "prompt", "prompt": "Is this safe? $ARGUMENTS" }
```
Only available for tool events: PreToolUse, PostToolUse, PermissionRequest.

**3. Agent Hook** - Runs an agent with tools:
```json
{ "type": "agent", "prompt": "Verify tests pass: $ARGUMENTS" }
```
Only available for tool events: PreToolUse, PostToolUse, PermissionRequest.

### Hook Input (stdin JSON)
```json
{
  "session_id": "abc123",
  "tool_name": "Write",
  "tool_input": { "file_path": "/path/to/file.txt", "content": "..." },
  "tool_response": { "success": true }  // PostToolUse only
}
```

### Hook JSON Output

Hooks can return JSON to control behavior:

```json
{
  "systemMessage": "Warning shown to user in UI",
  "continue": false,
  "stopReason": "Message shown when blocking",
  "suppressOutput": false,
  "decision": "block",
  "reason": "Explanation for decision",
  "hookSpecificOutput": {
    "hookEventName": "PostToolUse",
    "additionalContext": "Context injected back to model"
  }
}
```

**Fields:**
- `systemMessage` - Display a message to the user (all hooks)
- `continue` - Set to `false` to block/stop (default: true)
- `stopReason` - Message shown when `continue` is false
- `suppressOutput` - Hide stdout from transcript (default: false)
- `decision` - "block" for PostToolUse/Stop/UserPromptSubmit hooks (deprecated for PreToolUse, use hookSpecificOutput.permissionDecision instead)
- `reason` - Explanation for decision
- `hookSpecificOutput` - Event-specific output (must include `hookEventName`):
  - `additionalContext` - Text injected into model context
  - `permissionDecision` - "allow", "deny", or "ask" (PreToolUse only)
  - `permissionDecisionReason` - Reason for the permission decision (PreToolUse only)
  - `updatedInput` - Modified tool input (PreToolUse only)

### Common Patterns

**Auto-format after writes:**
```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "jq -r '.tool_response.filePath // .tool_input.file_path' | { read -r f; prettier --write \"$f\"; } 2>/dev/null || true"
      }]
    }]
  }
}
```

**Log all bash commands:**
```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{
        "type": "command",
        "command": "jq -r '.tool_input.command' >> ~/.claude/bash-log.txt"
      }]
    }]
  }
}
```

**Stop hook that displays message to user:**

Command must output JSON with `systemMessage` field:
```bash
# Example command that outputs: {"systemMessage": "Session complete!"}
echo '{"systemMessage": "Session complete!"}'
```

**Run tests after code changes:**
```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "jq -r '.tool_input.file_path // .tool_response.filePath' | grep -E '\\.(ts|js)$' && npm test || true"
      }]
    }]
  }
}
```


## Constructing a Hook (with verification)

Given an event, matcher, target file, and desired behavior, follow this flow. Each step catches a different failure class — a hook that silently does nothing is worse than no hook.

1. **Dedup check.** Read the target file. If a hook already exists on the same event+matcher, show the existing command and ask: keep it, replace it, or add alongside.

2. **Construct the command for THIS project — don't assume.** The hook receives JSON on stdin. Build a command that:
   - Extracts any needed payload safely — use `jq -r` into a quoted variable or `{ read -r f; ... "$f"; }`, NOT unquoted `| xargs` (splits on spaces)
   - Invokes the underlying tool the way this project runs it (npx/bunx/yarn/pnpm? Makefile target? globally-installed?)
   - Skips inputs the tool doesn't handle (formatters often have `--ignore-unknown`; if not, guard by extension)
   - Stays RAW for now — no `|| true`, no stderr suppression. You'll wrap it after the pipe-test passes.

3. **Pipe-test the raw command.** Synthesize the stdin payload the hook will receive and pipe it directly:
   - `Pre|PostToolUse` on `Write|Edit`: `echo '{"tool_name":"Edit","tool_input":{"file_path":"<a real file from this repo>"}}' | <cmd>`
   - `Pre|PostToolUse` on `Bash`: `echo '{"tool_name":"Bash","tool_input":{"command":"ls"}}' | <cmd>`
   - `Stop`/`UserPromptSubmit`/`SessionStart`: most commands don't read stdin, so `echo '{}' | <cmd>` suffices

   Check exit code AND side effect (file actually formatted, test actually ran). If it fails you get a real error — fix (wrong package manager? tool not installed? jq path wrong?) and retest. Once it works, wrap with `2>/dev/null || true` (unless the user wants a blocking check).

4. **Write the JSON.** Merge into the target file (schema shape in the "Hook Structure" section above). If this creates `.claude/settings.local.json` for the first time, add it to .gitignore — the Write tool doesn't auto-gitignore it.

5. **Validate syntax + schema in one shot:**

   `jq -e '.hooks.<event>[] | select(.matcher == "<matcher>") | .hooks[] | select(.type == "command") | .command' <target-file>`

   Exit 0 + prints your command = correct. Exit 4 = matcher doesn't match. Exit 5 = malformed JSON or wrong nesting. A broken settings.json silently disables ALL settings from that file — fix any pre-existing malformation too.

6. **Prove the hook fires** — only for `Pre|PostToolUse` on a matcher you can trigger in-turn (`Write|Edit` via Edit, `Bash` via Bash). `Stop`/`UserPromptSubmit`/`SessionStart` fire outside this turn — skip to step 7.

   For a **formatter** on `PostToolUse`/`Write|Edit`: introduce a detectable violation via Edit (two consecutive blank lines, bad indentation, missing semicolon — something this formatter corrects; NOT trailing whitespace, Edit strips that before writing), re-read, confirm the hook **fixed** it. For **anything else**: temporarily prefix the command in settings.json with `echo "$(date) hook fired" >> /tmp/claude-hook-check.txt; `, trigger the matching tool (Edit for `Write|Edit`, a harmless `true` for `Bash`), read the sentinel file.

   **Always clean up** — revert the violation, strip the sentinel prefix — whether the proof passed or failed.

   **If proof fails but pipe-test passed and `jq -e` passed**: the settings watcher isn't watching `.claude/` — it only watches directories that had a settings file when this session started. The hook is written correctly. Tell the user to open `/hooks` once (reloads config) or restart — you can't do this yourself; `/hooks` is a user UI menu and opening it ends this turn.

7. **Handoff.** Tell the user the hook is live (or needs `/hooks`/restart per the watcher caveat). Point them at `/hooks` to review, edit, or disable it later. The UI only shows "Ran N hooks" if a hook errors or is slow — silent success is invisible by design.


## Example Workflows

### Adding a Hook

User: "Format my code after Claude writes it"

1. **Clarify**: Which formatter? (prettier, gofmt, etc.)
2. **Read**: `.claude/settings.json` (or create if missing)
3. **Merge**: Add to existing hooks, don't replace
4. **Result**:
```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "jq -r '.tool_response.filePath // .tool_input.file_path' | { read -r f; prettier --write \"$f\"; } 2>/dev/null || true"
      }]
    }]
  }
}
```

### Adding Permissions

User: "Allow npm commands without prompting"

1. **Read**: Existing permissions
2. **Merge**: Add `Bash(npm *)` to allow array
3. **Result**: Combined with existing allows

### Environment Variables

User: "Set DEBUG=true"

1. **Decide**: User settings (global) or project settings?
2. **Read**: Target file
3. **Merge**: Add to env object
```json
{ "env": { "DEBUG": "true" } }
```

## Common Mistakes to Avoid

1. **Replacing instead of merging** - Always preserve existing settings
2. **Wrong file** - Ask user if scope is unclear
3. **Invalid JSON** - Validate syntax after changes
4. **Forgetting to read first** - Always read before write

## Troubleshooting Hooks

If a hook isn't running:
1. **Check the settings file** - Read ~/.claude/settings.json or .claude/settings.json
2. **Verify JSON syntax** - Invalid JSON silently fails
3. **Check the matcher** - Does it match the tool name? (e.g., "Bash", "Write", "Edit")
4. **Check hook type** - Is it "command", "prompt", or "agent"?
5. **Test the command** - Run the hook command manually to see if it works
6. **Use --debug** - Run `claude --debug` to see hook execution logs


## Full Settings JSON Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "$schema": {
      "description": "JSON Schema reference for Claude Code settings",
      "type": "string"
    },
    "apiKeyHelper": {
      "description": "Path to a script that outputs authentication values",
      "type": "string"
    },
    "proxyAuthHelper": {
      "description": "Shell command that outputs a Proxy-Authorization header value (EAP)",
      "type": "string"
    },
    "awsCredentialExport": {
      "description": "Path to a script that exports AWS credentials",
      "type": "string"
    },
    "awsAuthRefresh": {
      "description": "Path to a script that refreshes AWS authentication",
      "type": "string"
    },
    "gcpAuthRefresh": {
      "description": "Command to refresh GCP authentication (e.g., gcloud auth application-default login)",
      "type": "string"
    },
    "processWrapper": {
      "description": "Corporate launcher argv prefix for the background-agent supervisor, the sessions and workers it hosts, and the other covered background processes listed in the Claude Code corporate-launcher documentation. Equivalent to the CLAUDE_CODE_PROCESS_WRAPPER environment variable, which takes precedence when set. Honored from managed settings, a --settings/SDK-supplied settings file, and user settings, in that precedence order; project and local settings are ignored.",
      "type": "string"
    },
    "policyHelper": {
      "description": "Executable that computes managed settings at startup. Honored only from admin-controlled policy sources.",
      "type": "object",
      "properties": {
        "path": {
          "description": "Absolute path to the helper executable",
          "type": "string"
        },
        "timeoutMs": {
          "type": "integer",
          "minimum": 1000,
          "maximum": 9007199254740991
        },
        "refreshIntervalMs": {
          "anyOf": [
            {
              "type": "number",
              "const": 0
            },
            {
              "type": "integer",
              "minimum": 60000,
              "maximum": 9007199254740991
            }
          ]
        }
      },
      "required": [
        "path"
      ]
    },
    "fileSuggestion": {
      "description": "Custom file suggestion configuration for @ mentions",
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "const": "command"
        },
        "command": {
          "type": "string"
        }
      },
      "required": [
        "type",
        "command"
      ]
    },
    "respectGitignore": {
      "description": "Whether file picker should respect .gitignore files (default: true). Note: .ignore files are always respected.",
      "type": "boolean"
    },
    "cleanupPeriodDays": {
      "description": "Number of days to retain chat transcripts before automatic cleanup (default: 30). Minimum 1. Use a large value for long retention; use --no-session-persistence to disable transcript writes entirely.",
      "type": "integer",
      "exclusiveMinimum": 0,
      "maximum": 9007199254740991
    },
    "desktopSessionCleanupPeriodDays": {
      "description": "Retention ceiling in days for session transcripts created or last written by a desktop-host surface (Claude Desktop, Cowork), which are otherwise exempt from the cleanupPeriodDays sweep. 0 (the default) means no ceiling: such transcripts are kept until deleted another way. Unlike cleanupPeriodDays, 0 is allowed because this setting never disables writes — it only bounds an exemption from deletion. The ceiling is a hard cap: it also bounds an active archive grace, so the grace window of a release marker never keeps files past the ceiling. Ignored when cleanupPeriodDays is managed by org policy. A ceiling at or below cleanupPeriodDays effectively disables the exemption: those transcripts age out on the regular cleanupPeriodDays schedule, so the effective retention is whichever of the two periods is longer.",
      "type": "integer",
      "minimum": 0,
      "maximum": 9007199254740991
    },
    "syncClaudeAiSkills": {
      "description": "Set to false to turn off syncing of the skills you have enabled on claude.ai. In your user settings (or managed settings): nothing more is downloaded, previously synced skills (~/.claude/skills/synced) can no longer be run, are hidden from every session started afterwards, and are moved to ~/.claude/skills/.trash at the next launch (deleted after cleanupPeriodDays; re-downloaded, not restored, if you re-enable). In .claude/settings.local.json or --settings: downloads stop and synced skills are blocked and hidden for sessions in that workspace or invocation only (nothing is moved). Not read from project settings (.claude/settings.json). Only false is honored — the feature is enabled server-side for your account, so setting true does not turn it on early. While it is on, synced skills are available in every session, re-synced every 10 minutes, and removed when you disable them on claude.ai. Only applies when signed in with your Claude account.",
      "type": "boolean"
    },
    "syncClaudeAiPlugins": {
      "description": "Set to false to turn off syncing of the plugins you have enabled on claude.ai. In your user settings (or managed settings): nothing more is downloaded, previously synced plugins (~/.claude/plugins/synced) are hidden from every session started afterwards and moved to ~/.claude/plugins/.trash at the next launch (deleted after cleanupPeriodDays; re-downloaded, not restored, if you re-enable). In .claude/settings.local.json or --settings: downloads stop and synced plugins are hidden for sessions in that workspace or invocation only (nothing is moved). Not read from project settings (.claude/settings.json). Only false is honored — the feature is enabled server-side for your account, so setting true does not turn it on early. While it is on, synced plugins load in every session like plugins you installed yourself (a plugin you installed with the same name takes precedence), are re-synced at each launch, and are removed when you disable them on claude.ai. Only applies when signed in with your Claude account.",
      "type": "boolean"
    },
    "skillListingMaxDescChars": {
      "description": "Per-skill description character cap in the skill listing sent to Claude (default: 1536). Descriptions longer than this are truncated. Raise to opt in to higher per-turn context cost.",
      "type": "integer",
      "exclusiveMinimum": 0,
      "maximum": 9007199254740991
    },
    "skillListingBudgetFraction": {
      "description": "Fraction of the context window (in characters) reserved for the skill listing sent to Claude (default: 0.01 = 1%). When the listing exceeds this, descriptions are shortened to fit. Raise to opt in to higher per-turn context cost.",
      "type": "number",
      "exclusiveMinimum": 0,
      "maximum": 1
    },
    "wslInheritsWindowsSettings": {
      "description": "When set to true in either admin-only Windows source — the HKLM SOFTWARE/Policies/ClaudeCode registry key or C:/Program Files/ClaudeCode/managed-settings.json — WSL reads managed settings from the full Windows policy chain (HKLM, C:/Program Files/ClaudeCode via DrvFs, HKCU) in addition to /etc/claude-code. Windows sources take priority. The flag is also required in HKCU itself for HKCU policy to apply on WSL (double opt-in: admin enables the chain, user confirms HKCU). On native Windows the flag has no effect.",
      "type": "boolean"
    },
    "env": {
      "description": "Environment variables to set for Claude Code sessions",
      "type": "object",
      "propertyNames": {
        "type": "string"
      },
      "additionalProperties": {
        "type": "string"
      }
    },
    "attribution": {
      "description": "Customize attribution text for commits and PRs. Each field defaults to the standard Claude Code attribution if not set.",
      "type": "object",
      "properties": {
        "commit": {
          "description": "Attribution text for git commits, including any trailers. Empty string hides attribution.",
          "type": "string"
        },
        "pr": {
          "description": "Attribution text for pull request descriptions. Empty string hides attribution.",
          "type": "string"
        },
        "sessionUrl": {
          "description": "Whether to append the claude.ai session link to commits and PRs created from web or Remote Control sessions (default: true). Set to false to omit the Claude-Session trailer and PR-body link.",
          "type": "boolean"
        }
      },
      "additionalProperties": {}
    },
    "includeCoAuthoredBy": {
      "description": "Deprecated: Use attribution instead. Whether to include Claude's co-authored by attribution in commits and PRs (defaults to true)",
      "type": "boolean"
    },
    "includeGitInstructions": {
      "description": "Include built-in commit and PR workflow instructions in Claude's system prompt (default: true)",
      "type": "boolean"
    },
    "permissions": {
      "description": "Tool usage permissions configuration",
      "type": "object",
      "properties": {
        "allow": {
          "description": "List of permission rules for allowed operations",
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "deny": {
          "description": "List of permission rules for denied operations",
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "ask": {
          "description": "List of permission rules that should always prompt for confirmation",
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "defaultMode": {
          "description": "Default permission mode when Claude Code needs access ('manual' is accepted as an alias for 'default')",
          "type": "string",
          "enum": [
            "acceptEdits",
            "auto",
            "bypassPermissions",
            "default",
            "dontAsk",
            "plan"
          ]
        },
        "disableBypassPermissionsMode": {
          "description": "Disable the ability to bypass permission prompts",
          "type": "string",
          "enum": [
            "disable"
          ]
        },
        "blockReadsOutsideWorkingDirectories": {
          "description": "Refuse file-tool reads (Read, Grep, Glob, LSP) outside the working directories in every permission mode; true in any settings source wins. Also set when the user picks \"block\" on the one-time auto-mode prompt for a read outside the working directories.",
          "type": "boolean"
        },
        "disableAutoMode": {
          "description": "Disable auto mode",
          "type": "string",
          "enum": [
            "disable"
          ]
        },
        "additionalDirectories": {
          "description": "Additional directories to include in the permission scope",
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "additionalProperties": {}
    },
    "model": {
      "description": "Override the default model used by Claude Code",
      "type": "string"
    },
    "fallbackModel": {
      "description": "Fallback model(s) tried in order when the primary model is overloaded or unavailable. Each element accepts a model name or alias; \"default\" expands to the default model. CLI --fallback-model takes precedence.",
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "availableModels": {
      "description": "Allowlist of models that users can select. Accepts family aliases (\"opus\" allows any opus version), version prefixes (\"opus-4-5\" allows only that version), and full model IDs. If undefined, all models are available. If empty array, only the default model is available. Typically set in managed settings by enterprise administrators.",
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "enforceAvailableModels": {
      "description": "When true and availableModels is a non-empty array, the Default model selection is also constrained: if the default model for the user tier is not in availableModels, Default resolves to the first allowed availableModels entry instead. Has no effect when availableModels is unset or an empty array. Typically set in managed settings by enterprise administrators.",
      "type": "boolean"
    },
    "modelOverrides": {
      "description": "Override mapping from Anthropic model ID (e.g. \"claude-opus-4-6\") to provider-specific model ID (e.g. a Bedrock inference profile ARN). Typically set in managed settings by enterprise administrators.",
      "type": "object",
      "propertyNames": {
        "type": "string"
      },
      "additionalProperties": {
        "type": "string"
      }
    },
    "modelPicker": {
      "description": "Curate the /model picker: an ordered list of models with your own labels, independent of the built-in lineup and of Claude Code releases. availableModels still applies to these rows. Honored from managed, --settings/SDK, and user settings only (not from a project checkout); the highest-precedence of those that defines modelPicker wins outright (no merging across sources). Typically set in managed settings by enterprise administrators.",
      "type": "object",
      "properties": {
        "options": {
          "description": "Rows to show in the /model picker, in order.",
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "model": {
                "description": "Model to select, taken verbatim: an alias (\"opus\"), an Anthropic model ID, or a provider-format ID (Vertex, Bedrock, gateway). Same values --model accepts.",
                "type": "string"
              },
              "label": {
                "description": "Row title. Defaults to the model name.",
                "type": "string"
              },
              "description": {
                "description": "Row subtitle. Defaults to a generic description.",
                "type": "string"
              },
              "behavesAs": {
                "description": "For a model this version of Claude Code does not know: the ID of a model it does know (e.g. \"claude-opus-4-8\") whose client-side handling — prompt profile, capability and effort defaults — applies to it. Changes neither the row's label nor the model ID sent. Without it, a model-catalog row for a model this version does not know is not offered until Claude Code is updated.",
                "type": "string"
              }
            },
            "required": [
              "model"
            ]
          }
        },
        "replaceBuiltInOptions": {
          "description": "When true, the picker shows only the Default row and these options — the built-in lineup, gateway-discovered models and ANTHROPIC_CUSTOM_MODEL_OPTION are hidden. When false or unset, these options are added after the built-in lineup.",
          "type": "boolean"
        }
      },
      "required": [
        "options"
      ]
    },
    "modelPricing": {
      "description": "Price usage at your organization's contracted rates instead of list price. Affects every spend figure Claude Code reports — /cost, the status line, the SDK total_cost_usd, --max-budget-usd, and the OpenTelemetry cost metric and events — which remain USD estimates, not an invoice (the per-Mtok price labels in /model stay at list). \"overrides\" maps a model ID to its USD-per-million-token rates (input, output, cacheRead, cacheWrite — all four required, each 0 to 10000; cacheWrite prices both 5-minute and 1-hour cache writes). A matching row is charged exactly as written; fast-mode and US-data-residency surcharges are not added on top. A key Claude Code itself uses for a built-in model — its ID such as \"claude-sonnet-4-6\", or its first-party, Bedrock (any or no region prefix), Vertex or Foundry ID — covers every dated and provider form of that model; any other key — a gateway model alias, or a spelling Claude Code does not itself use — matches that model ID only (case-insensitive), and such an exact match wins over a built-in row. On Bedrock an application inference profile is matched by its backing model. An invalid row or multiplier is reported and skipped; the rest still apply. \"multiplier\" in (0, 1] scales every computed cost, overridden or not (0.85 = 85% of the price). Only honored from managed settings (server-managed, MDM / OS policy, or managed-settings.json), or — when none of those sets it — when supplied by a host application that manages the model provider; ignored in user, project, local and --settings sources.",
      "type": "object",
      "properties": {
        "multiplier": {
          "type": "number",
          "exclusiveMinimum": 0,
          "maximum": 1
        },
        "overrides": {
          "type": "object",
          "propertyNames": {
            "type": "string"
          },
          "additionalProperties": {
            "type": "object",
            "properties": {
              "input": {
                "type": "number",
                "minimum": 0,
                "maximum": 10000
              },
              "output": {
                "type": "number",
                "minimum": 0,
                "maximum": 10000
              },
              "cacheRead": {
                "type": "number",
                "minimum": 0,
                "maximum": 10000
              },
              "cacheWrite": {
                "type": "number",
                "minimum": 0,
                "maximum": 10000
              }
            },
            "required": [
              "input",
              "output",
              "cacheRead",
              "cacheWrite"
            ]
          }
        }
      }
    },
    "enableAllProjectMcpServers": {
      "description": "Whether to automatically approve all MCP servers in the project",
      "type": "boolean"
    },
    "enabledMcpjsonServers": {
      "description": "List of approved MCP servers from .mcp.json",
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "disabledMcpjsonServers": {
      "description": "List of rejected MCP servers from .mcp.json",
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "disableClaudeAiConnectors": {
      "description": "When true in any settings source, claude.ai MCP cloud connectors are not auto-fetched or connected. Only gates auto-fetched connectors — a claudeai-proxy server passed explicitly (e.g. via --mcp-config or the SDK mcpServers option) still follows the normal MCP config trust flow. Any-source-true wins: a project can opt out, but a project-level false cannot override a user-level true.",
      "type": "boolean"
    },
    "skillOverrides": {
      "description": "Per-skill listing overrides keyed by skill name. \"name-only\" lists the skill without its description; \"user-invocable-only\" hides it from the model but keeps /name; \"off\" hides it from both. Absent = on.",
      "type": "object",
      "propertyNames": {
        "type": "string"
      },
      "additionalProperties": {
        "type": "string",
        "enum": [
          "on",
          "name-only",
          "user-invocable-only",
          "off"
        ]
      }
    },
    "disableBundledSkills": {
      "description": "Disable the skills and workflows that ship with Claude Code: bundled skills and workflows are removed entirely; built-in slash commands stay typable but are hidden from the model. Plugins, .claude/skills/, and .claude/commands/ are unaffected. Equivalent to CLAUDE_CODE_DISABLE_BUNDLED_SKILLS=1.",
      "type": "boolean"
    },
    "managedMcpServers": {
      "description": "MCP servers the organization provides to every user, keyed by server name, each with the .mcp.json entry shape; only \"http\" and \"sse\" servers are accepted (nothing that names a program to run, no ${VAR} references). Honored from managed settings only; users cannot remove them, deniedMcpServers still applies, and they need no allowedMcpServers entry. Not read in Claude Desktop's Code tab on a third-party deployment or in Cowork sessions, where Claude Desktop supplies and locks the session's MCP servers itself.",
      "type": "object",
      "propertyNames": {
        "type": "string"
      },
      "additionalProperties": {
        "type": "object",
        "propertyNames": {
          "type": "string"
        },
        "additionalProperties": {}
      }
    },
    "allowedMcpServers": {
      "description": "Enterprise allowlist of the MCP servers users may use. Governs servers users add (user, project and local config, --mcp-config, agent frontmatter, plugins, claude.ai connectors); servers the organization itself delivers (managedMcpServers, and managed-mcp.json entries that use no ${VAR} expansion) are allowed without being listed; a managed-mcp.json entry that uses ${VAR} expansion is still checked against this list. If undefined, all servers are allowed. If empty array, users can use no servers of their own. Denylist takes precedence - if a server is on both lists, it is denied.",
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "serverName": {
            "description": "Name of the MCP server that users are allowed to configure",
            "type": "string",
            "pattern": "^[a-zA-Z0-9_-]+$"
          },
          "serverCommand": {
            "description": "Command array [command, ...args] to match exactly for allowed stdio servers",
            "minItems": 1,
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "serverUrl": {
            "description": "URL pattern with wildcard support (e.g., \"https://*.example.com/*\") for allowed remote MCP servers",
            "type": "string"
          }
        }
      }
    },
    "deniedMcpServers": {
      "description": "Enterprise denylist of MCP servers that are explicitly blocked. If a server is on the denylist, it will be blocked across all scopes including enterprise. Denylist takes precedence over allowlist - if a server is on both lists, it is denied.",
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "serverName": {
            "description": "Name of the MCP server that is explicitly blocked",
            "type": "string",
            "minLength": 1
          },
          "serverCommand": {
            "description": "Command array [command, ...args] to match exactly for blocked stdio servers",
            "minItems": 1,
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "serverUrl": {
            "description": "URL pattern with wildcard support (e.g., \"https://*.example.com/*\") for blocked remote MCP servers",
            "type": "string"
          }
        }
      }
    },
    "hooks": {
      "description": "Custom commands to run before/after tool executions",
      "type": "object",
      "propertyNames": {
        "type": "string",
        "enum": [
          "PreToolUse",
          "PostToolUse",
          "PostToolUseFailure",
          "PostToolBatch",
          "Notification",
          "UserPromptSubmit",
          "UserPromptExpansion",
          "SessionStart",
          "SessionEnd",
          "Stop",
          "StopFailure",
          "SubagentStart",
          "SubagentStop",
          "PreCompact",
          "PostCompact",
          "PreModelSwitch",
          "PostModelSwitch",
          "PermissionRequest",
          "PermissionDenied",
          "Setup",
          "TeammateIdle",
          "TaskCreated",
          "TaskCompleted",
          "Elicitation",
          "ElicitationResult",
          "ConfigChange",
          "WorktreeCreate",
          "WorktreeRemove",
          "InstructionsLoaded",
          "CwdChanged",
          "FileChanged",
          "DirectoryAdded",
          "MessageDisplay"
        ]
      },
      "additionalProperties": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "matcher": {
              "description": "String pattern to match (e.g. tool names like \"Write\")",
              "type": "string"
            },
            "hooks": {
              "description": "List of hooks to execute when the matcher matches",
              "type": "array",
              "items": {
                "anyOf": [
                  {
                    "type": "object",
                    "properties": {
                      "type": {
                        "description": "Shell command hook type",
                        "type": "string",
                        "const": "command"
                      },
                      "command": {
                        "description": "Shell command to execute",
                        "type": "string"
                      },
                      "args": {
                        "description": "Argument list for exec form. When present, `command` is resolved as an executable and spawned directly with these arguments — no shell. Path placeholders like ${CLAUDE_PLUGIN_ROOT} are substituted per-element as plain strings, so paths with quotes, $, or backticks never reach a shell parser. When absent, `command` runs through a shell (bash on POSIX, PowerShell on Windows without Git Bash).",
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "if": {
                        "description": "Permission rule syntax to filter when this hook runs (e.g., \"Bash(git *)\"). Only runs if the tool call matches the pattern. Avoids spawning hooks for non-matching commands.",
                        "type": "string"
                      },
                      "shell": {
                        "description": "Shell interpreter. 'bash' uses your $SHELL (bash/zsh/sh); 'powershell' uses pwsh. Defaults to bash (powershell on Windows without Git Bash).",
                        "type": "string",
                        "enum": [
                          "bash",
                          "powershell"
                        ]
                      },
                      "timeout": {
                        "description": "Timeout in seconds for this specific command",
                        "type": "number",
                        "exclusiveMinimum": 0
                      },
                      "statusMessage": {
                        "description": "Custom status message to display in spinner while hook runs",
                        "type": "string"
                      },
                      "once": {
                        "description": "If true, hook runs once and is removed after execution",
                        "type": "boolean"
                      },
                      "async": {
                        "description": "If true, hook runs in background without blocking",
                        "type": "boolean"
                      },
                      "asyncRewake": {
                        "description": "If true, hook runs in background and wakes the model on exit code 2 (blocking error). Implies async.",
                        "type": "boolean"
                      }
                    },
                    "required": [
                      "type",
                      "command"
                    ]
                  },
                  {
                    "type": "object",
                    "properties": {
                      "type": {
                        "description": "LLM prompt hook type",
                        "type": "string",
                        "const": "prompt"
                      },
                      "prompt": {
                        "description": "Prompt to evaluate with LLM. Use $ARGUMENTS placeholder for hook input JSON.",
                        "type": "string"
                      },
                      "if": {
                        "description": "Permission rule syntax to filter when this hook runs (e.g., \"Bash(git *)\"). Only runs if the tool call matches the pattern. Avoids spawning hooks for non-matching commands.",
                        "type": "string"
                      },
                      "timeout": {
                        "description": "Timeout in seconds for this specific prompt evaluation",
                        "type": "number",
                        "exclusiveMinimum": 0
                      },
                      "model": {
                        "description": "Model to use for this prompt hook (e.g., \"claude-sonnet-5\"). If not specified, uses the default small fast model.",
                        "type": "string"
                      },
                      "continueOnBlock": {
                        "description": "Sets the continue value for the decision:\"block\" produced when ok is false. Default false (turn ends). Whether continue:true lets the turn proceed depends on the event's decision:\"block\" semantics. On PostToolUse, the reason is fed back to Claude and the turn continues.",
                        "type": "boolean"
                      },
                      "statusMessage": {
                        "description": "Custom status message to display in spinner while hook runs",
                        "type": "string"
                      },
                      "once": {
                        "description": "If true, hook runs once and is removed after execution",
                        "type": "boolean"
                      }
                    },
                    "required": [
                      "type",
                      "prompt"
                    ]
                  },
                  {
                    "type": "object",
                    "properties": {
                      "type": {
                        "description": "Agentic verifier hook type",
                        "type": "string",
                        "const": "agent"
                      },
                      "prompt": {
                        "description": "Prompt describing what to verify (e.g. \"Verify that unit tests ran and passed.\"). Use $ARGUMENTS placeholder for hook input JSON.",
                        "type": "string"
                      },
                      "if": {
                        "description": "Permission rule syntax to filter when this hook runs (e.g., \"Bash(git *)\"). Only runs if the tool call matches the pattern. Avoids spawning hooks for non-matching commands.",
                        "type": "string"
                      },
                      "timeout": {
                        "description": "Timeout in seconds for agent execution (default 60)",
                        "type": "number",
                        "exclusiveMinimum": 0
                      },
                      "model": {
                        "description": "Model to use for this agent hook (e.g., \"claude-sonnet-5\"). If not specified, uses Haiku.",
                        "type": "string"
                      },
                      "statusMessage": {
                        "description": "Custom status message to display in spinner while hook runs",
                        "type": "string"
                      },
                      "once": {
                        "description": "If true, hook runs once and is removed after execution",
                        "type": "boolean"
                      }
                    },
                    "required": [
                      "type",
                      "prompt"
                    ]
                  },
                  {
                    "type": "object",
                    "properties": {
                      "type": {
                        "description": "HTTP hook type",
                        "type": "string",
                        "const": "http"
                      },
                      "url": {
                        "description": "URL to POST the hook input JSON to",
                        "type": "string",
                        "format": "uri"
                      },
                      "if": {
                        "description": "Permission rule syntax to filter when this hook runs (e.g., \"Bash(git *)\"). Only runs if the tool call matches the pattern. Avoids spawning hooks for non-matching commands.",
                        "type": "string"
                      },
                      "timeout": {
                        "description": "Timeout in seconds for this specific request",
                        "type": "number",
                        "exclusiveMinimum": 0
                      },
                      "headers": {
                        "description": "Additional headers to include in the request. Values may reference environment variables using $VAR_NAME or ${VAR_NAME} syntax (e.g., \"Authorization\": \"Bearer $MY_TOKEN\"). Only variables listed in allowedEnvVars will be interpolated.",
                        "type": "object",
                        "propertyNames": {
                          "type": "string"
                        },
                        "additionalProperties": {
                          "type": "string"
                        }
                      },
                      "allowedEnvVars": {
                        "description": "Explicit list of environment variable names that may be interpolated in header values. Only variables listed here will be resolved; all other $VAR references are left as empty strings. Required for env var interpolation to work.",
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "statusMessage": {
                        "description": "Custom status message to display in spinner while hook runs",
                        "type": "string"
                      },
                      "once": {
                        "description": "If true, hook runs once and is removed after execution",
                        "type": "boolean"
                      }
                    },
                    "required": [
                      "type",
                      "url"
                    ]
                  },
                  {
                    "type": "object",
                    "properties": {
                      "type": {
                        "description": "MCP tool hook type",
                        "type": "string",
                        "const": "mcp_tool"
                      },
                      "server": {
                        "description": "Name of an already-configured MCP server to invoke",
                        "type": "string"
                      },
                      "tool": {
                        "description": "Name of the tool on that server to call",
                        "type": "string"
                      },
                      "input": {
                        "description": "Arguments passed to the MCP tool. String values support ${path} interpolation from the hook input JSON (e.g. \"${tool_input.file_path}\").",
                        "type": "object",
                        "propertyNames": {
                          "type": "string"
                        },
                        "additionalProperties": {}
                      },
                      "if": {
                        "description": "Permission rule syntax to filter when this hook runs (e.g., \"Bash(git *)\"). Only runs if the tool call matches the pattern. Avoids spawning hooks for non-matching commands.",
                        "type": "string"
                      },
                      "timeout": {
                        "description": "Timeout in seconds for this specific tool call",
                        "type": "number",
                        "exclusiveMinimum": 0
                      },
                      "statusMessage": {
                        "description": "Custom status message to display in spinner while hook runs",
                        "type": "string"
                      },
                      "once": {
                        "description": "If true, hook runs once and is removed after execution",
                        "type": "boolean"
                      }
                    },
                    "required": [
                      "type",
                      "server",
                      "tool"
                    ]
                  }
                ]
              }
            }
          },
          "required": [
            "hooks"
          ]
        }
      }
    },
    "worktree": {
      "description": "Git worktree configuration: the CLI --worktree flag, EnterWorktree and agent isolation, plus the location Claude Code Desktop uses for SSH-session worktrees on this machine.",
      "type": "object",
      "properties": {
        "symlinkDirectories": {
          "description": "Directories to symlink from main repository to worktrees to avoid disk bloat. Must be explicitly configured - no directories are symlinked by default. Common examples: \"node_modules\", \".cache\", \".bin\"",
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "sparsePaths": {
          "description": "Directories to include when creating worktrees, via git sparse-checkout (cone mode). Dramatically faster in large monorepos — only the listed paths are written to disk.",
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "baseRef": {
          "description": "Which ref new worktrees branch from. 'fresh' (default) branches from origin/<default-branch> for a clean tree. 'head' branches from your current local HEAD so unpushed commits and feature-branch state are present. Applies to --worktree, EnterWorktree, and agent isolation.",
          "type": "string",
          "enum": [
            "fresh",
            "head"
          ]
        },
        "bgIsolation": {
          "description": "Isolation mode for background sessions in this repo. 'worktree' (default) blocks Edit/Write in the main checkout until EnterWorktree is called. 'none' lets background jobs edit the working copy directly.",
          "type": "string",
          "enum": [
            "worktree",
            "none"
          ]
        },
        "location": {
          "description": "Directory under which Claude Code Desktop creates the worktrees of SSH sessions that run on this machine (an absolute path or one starting with ~/), instead of <project>/.claude/worktrees. Read by the desktop app from the SSH host user settings; a location chosen in the desktop app's SSH connection settings takes precedence. The CLI (--worktree, EnterWorktree, agent isolation) does not read it yet.",
          "type": "string"
        }
      }
    },
    "disableAllHooks": {
      "description": "Disable all hooks and statusLine execution",
      "type": "boolean"
    },
    "disableAgentView": {
      "description": "Disable agent view (`claude agents`, `--bg`, /background, the on-demand daemon). Typically set in managed settings. Equivalent to CLAUDE_CODE_DISABLE_AGENT_VIEW=1.",
      "type": "boolean"
    },
    "disableRemoteControl": {
      "description": "Disable Remote Control (claude.ai/code, `claude remote-control`, `--remote-control`/`--rc`, auto-start, and the in-session toggle). Typically set in managed settings.",
      "type": "boolean"
    },
    "disableWorkflows": {
      "description": "Disable the Workflows feature (also via CLAUDE_CODE_DISABLE_WORKFLOWS).",
      "type": "boolean"
    },
    "disableArtifact": {
      "description": "Deprecated: use enableArtifact: false. Still honored — true disables the Artifact tool; false is ignored.",
      "type": "boolean"
    },
    "enableArtifact": {
      "description": "Turn the Artifact tool on or off. Off in any of managed, --settings, or user settings wins; project and local settings can only turn it off. Unset defaults to on once the feature is available.",
      "type": "boolean"
    },
    "enableWorkflows": {
      "description": "Enable or disable the Workflows feature for this user. Unset = default by plan once the feature is available.",
      "type": "boolean"
    },
    "workflowSizeGuideline": {
      "description": "Advisory size guideline for the dynamic workflows Claude writes: \"small\" aims for fewer than 5 agents, \"medium\" (the default) fewer than 15, \"large\" fewer than 50, and \"unrestricted\" sends no guideline. A value here — including from managed settings — takes precedence over the \"Dynamic workflow size\" choice in /config, and that /config row is hidden while a settings file provides the key. This is a guideline, not an enforced limit.",
      "type": "string",
      "enum": [
        "unrestricted",
        "small",
        "medium",
        "large"
      ]
    },
    "workflowKeywordTriggerEnabled": {
      "description": "Enable the \"ultracode\" keyword trigger: including the keyword in a prompt opts that turn into the Workflow tool. Set to false to disable the trigger. Default: true.",
      "type": "boolean"
    },
    "disableSkillShellExecution": {
      "description": "Disable inline shell execution in skills and custom slash commands from user, project, or plugin sources. Commands are replaced with a placeholder instead of being run.",
      "type": "boolean"
    },
    "defaultShell": {
      "description": "Default shell for input-box ! commands. Defaults to 'bash' on all platforms (no Windows auto-flip).",
      "type": "string",
      "enum": [
        "bash",
        "powershell"
      ]
    },
    "bashOutputMaxChars": {
      "description": "How many characters of a successful Bash or PowerShell command's output Claude receives inline (default 30000; values clamp to 4000-128000). Output past this is saved to a file and Claude receives a short preview plus the path. When set, this also replaces BASH_MAX_OUTPUT_LENGTH, which on its own only sizes the read-back window.",
      "type": "integer",
      "exclusiveMinimum": 0,
      "maximum": 9007199254740991
    },
    "taskOutputMaxChars": {
      "description": "How many characters of a background task's output the TaskOutput tool hands Claude inline (default 32000; values clamp to 4000-128000). Longer output is cut to its most recent characters with the path of the full output file, except that a shell command still running returns its first characters up to this size. When set, this also replaces TASK_MAX_OUTPUT_LENGTH, which on its own only sizes that window.",
      "type": "integer",
      "exclusiveMinimum": 0,
      "maximum": 9007199254740991
    },
    "respondToBashCommands": {
      "description": "Whether Claude responds after an input-box ! bash command runs. Set to false to add the command output to context without a response. Default: true.",
      "type": "boolean"
    },
    "allowManagedHooksOnly": {
      "description": "When true (and set in managed settings), only hooks from managed settings run. User, project, and local hooks are ignored.",
      "type": "boolean"
    },
    "allowedHttpHookUrls": {
      "description": "Allowlist of URL patterns that HTTP hooks may target. Supports * as a wildcard (e.g. \"https://hooks.example.com/*\"). When set, HTTP hooks with non-matching URLs are blocked. If undefined, all URLs are allowed. If empty array, no HTTP hooks are allowed. Arrays merge across settings sources (same semantics as allowedMcpServers).",
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "httpHookAllowedEnvVars": {
      "description": "Allowlist of environment variable names HTTP hooks may interpolate into headers. When set, each hook's effective allowedEnvVars is the intersection with this list. If undefined, no restriction is applied. Arrays merge across settings sources (same semantics as allowedMcpServers).",
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "allowManagedPermissionRulesOnly": {
      "description": "When true (and set in managed settings), permission rules from user, project, local, and --settings files and allow rules from --allowedTools are ignored; only managed settings can add allow rules through settings. --disallowedTools and other deny and ask rules from the command line or the current session still apply.",
      "type": "boolean"
    },
    "allowManagedMcpServersOnly": {
      "description": "When true (and set in managed settings), allowedMcpServers is only read from managed settings. deniedMcpServers still merges from all sources, so users can deny servers for themselves. Users can still add their own MCP servers, but only the admin-defined allowlist applies.",
      "type": "boolean"
    },
    "allowAllClaudeAiMcps": {
      "description": "When true (and set in managed settings), claude.ai cloud MCP connectors load alongside managed-mcp.json instead of being suppressed by its exclusive-control lockdown. Default off preserves the lockdown. Read from managed settings only.",
      "type": "boolean"
    },
    "strictPluginOnlyCustomization": {
      "description": "When set in managed settings, blocks non-plugin customization sources for the listed surfaces. Array form locks specific surfaces (e.g. [\"skills\", \"hooks\"]); `true` locks all four; `false` is an explicit no-op. Blocked: ~/.claude/{surface}/, .claude/{surface}/ (project), settings.json hooks, .mcp.json. NOT blocked: managed (policySettings) sources, plugin-provided customizations. Composes with strictKnownMarketplaces for end-to-end admin control — plugins gated by marketplace allowlist, everything else blocked here.",
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "skills",
              "agents",
              "hooks",
              "mcp"
            ]
          }
        }
      ]
    },
    "statusLine": {
      "description": "Custom status line display configuration",
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "const": "command"
        },
        "command": {
          "type": "string"
        },
        "padding": {
          "type": "number"
        },
        "refreshInterval": {
          "description": "Re-run the status line command every N seconds in addition to event-driven updates",
          "type": "number",
          "minimum": 1
        },
        "hideVimModeIndicator": {
          "description": "Hide the built-in `-- INSERT --` / `-- VISUAL --` indicator below the prompt. Use this when your status line script renders `vim.mode` itself.",
          "type": "boolean"
        }
      },
      "required": [
        "type",
        "command"
      ]
    },
    "prUrlTemplate": {
      "description": "URL template for PR links in the footer link badges and inline messages. The detected git PR is rendered as the first footer-link badge. Placeholders: {host} {owner} {repo} {number} {url}. Example: \"https://reviews.example.com/{owner}/{repo}/pull/{number}\"",
      "type": "string"
    },
    "footerLinksRegexes": {
      "description": "Extra clickable footer badges that appear when a regex matches turn output (tool results and assistant responses). Read from user, flag, and managed settings only; ignored in project .claude/settings.json and local .claude/settings.local.json. At most 5 badges render; the oldest is displaced by newer matches and /clear removes them. Use to surface IDs printed by project CLIs as session links.",
      "type": "array",
      "items": {
        "default": {
          "type": "invalid-entry-stripped"
        },
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "type": {
                "description": "Config variant. This client understands \"regex\": matches turn output and builds a URL from named capture groups. Entries with other variants are preserved but skipped at runtime.",
                "type": "string",
                "const": "regex"
              },
              "pattern": {
                "description": "Regex matched against turn output (tool results and assistant text)",
                "type": "string"
              },
              "url": {
                "description": "Link target. {name} placeholders are filled from named regex capture groups, e.g. (?<id>...) -> {id}. Values are URL-encoded; the origin must be literal in the template. The scheme must be https, http, or a recognized editor or workspace deep-link scheme: vscode, vscode-insiders, cursor, windsurf, zed, jetbrains, idea, slack, linear, notion, figma.",
                "type": "string"
              },
              "label": {
                "description": "Badge text. {name} placeholders filled from named capture groups; defaults to the full match.",
                "type": "string"
              }
            },
            "required": [
              "type",
              "pattern",
              "url"
            ],
            "additionalProperties": {}
          },
          {
            "type": "object",
            "properties": {
              "type": {
                "description": "Config variant discriminator for entries this client does not understand; the entry is preserved as-is and skipped at runtime.",
                "type": "string"
              }
            },
            "required": [
              "type"
            ],
            "additionalProperties": {}
          }
        ]
      }
    },
    "subagentStatusLine": {
      "description": "Custom per-subagent status line shown in the agent panel; receives row context as JSON on stdin",
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "const": "command"
        },
        "command": {
          "type": "string"
        }
      },
      "required": [
        "type",
        "command"
      ]
    },
    "enabledPlugins": {
      "description": "Enabled plugins using plugin-id@marketplace-id format. Example: { \"formatter@anthropic-tools\": true }. Also supports extended format with version constraints. Settings precedence is user < project < local < flag < policy, so to disable a plugin that project settings enable, set it to false in .claude/settings.local.json — setting false in ~/.claude/settings.json is overridden by the project.",
      "type": "object",
      "propertyNames": {
        "type": "string"
      },
      "additionalProperties": {
        "anyOf": [
          {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          {
            "type": "boolean"
          },
          {
            "not": {}
          }
        ]
      }
    },
    "prependPlugins": {
      "description": "Managed plugins (plugin@marketplace ids that managed enabledPlugins sets true) whose hooks run first, outermost, in the listed order: the first id listed sees every event before any other plugin and every result after it. Managed plugins not listed here or in appendPlugins follow the listed ones; user, project and marketplace plugins come after those; then appendPlugins; then the built-in plugins. The bundled sec-default@builtin seats itself outermost (on a machine with managed settings and for Team and Enterprise organizations) unless this list is set, in which case list sec-default@builtin where it should sit or leave it out. Any other id that is not an enabled managed plugin is skipped; an id listed in both keys is prepended. Only honored from managed settings (or, on a machine with none, from user settings for your own plugins); ignored in project, local and --settings sources.",
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "appendPlugins": {
      "description": "Managed plugins (plugin@marketplace ids that managed enabledPlugins sets true) whose hooks run last among plugins, innermost, in the listed order: the last id listed sits just above the built-in plugins and sees each event as every other plugin left it. Only honored from managed settings (or, on a machine with none, from user settings for your own plugins); ignored in project, local and --settings sources.",
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "extraKnownMarketplaces": {
      "description": "Additional marketplaces to make available for this repository. Typically used in repository .claude/settings.json to ensure team members have required plugin sources.",
      "type": "object",
      "propertyNames": {
        "type": "string"
      },
      "additionalProperties": {
        "type": "object",
        "properties": {
          "source": {
            "description": "Where to fetch the marketplace from",
            "anyOf": [
              {
                "type": "object",
                "properties": {
                  "source": {
                    "type": "string",
                    "const": "url"
                  },
                  "url": {
                    "description": "Direct URL to marketplace.json file",
                    "type": "string",
                    "format": "uri"
                  },
                  "headers": {
                    "description": "Custom HTTP headers (e.g., for authentication)",
                    "type": "object",
                    "propertyNames": {
                      "type": "string"
                    },
                    "additionalProperties": {
                      "type": "string"
                    }
                  },
                  "headersHelper": {
                    "description": "Command that prints a JSON object of HTTP headers (e.g. a short-lived auth token). Its output overrides `headers` and, like `headers`, is inherited by same-origin archive downloads from this marketplace. Runs from a fixed directory (the Claude config home, never the session's), so give a bare command found via PATH or an absolute path; it is re-run on later refreshes of this marketplace.",
                    "type": "string",
                    "maxLength": 500
                  }
                },
                "required": [
                  "source",
                  "url"
                ]
              },
              {
                "type": "object",
                "properties": {
                  "source": {
                    "type": "string",
                    "const": "github"
                  },
                  "repo": {
                    "description": "GitHub repository in owner/repo format. ONLY in the managed-settings policy lists (strictKnownMarketplaces / blockedMarketplaces) the owner-wildcard form \"owner/*\" matches every repository under exactly that owner. Everywhere else (marketplace add, extraKnownMarketplaces, known_marketplaces.json) the value must name a single repository — a wildcard is taken literally and fails to clone.",
                    "type": "string"
                  },
                  "ref": {
                    "description": "Git branch or tag to use (e.g., \"main\", \"v1.0.0\"). Defaults to repository default branch.",
                    "type": "string"
                  },
                  "path": {
                    "description": "Path to marketplace.json within repo (defaults to .claude-plugin/marketplace.json)",
                    "type": "string"
                  },
                  "sparsePaths": {
                    "description": "Directories to include via git sparse-checkout (cone mode). Use for monorepos where the marketplace lives in a subdirectory. Example: [\".claude-plugin\", \"plugins\"]. If omitted, the full repository is cloned.",
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  },
                  "skipLfs": {
                    "description": "Skip Git LFS smudge during clone and update (sets GIT_LFS_SKIP_SMUDGE=1) so LFS pointer files stay as pointers instead of downloading their content. Use for marketplaces hosted in repos with large LFS objects.",
                    "type": "boolean"
                  }
                },
                "required": [
                  "source",
                  "repo"
                ]
              },
              {
                "type": "object",
                "properties": {
                  "source": {
                    "type": "string",
                    "const": "git"
                  },
                  "url": {
                    "description": "Full git repository URL",
                    "type": "string"
                  },
                  "ref": {
                    "description": "Git branch or tag to use (e.g., \"main\", \"v1.0.0\"). Defaults to repository default branch.",
                    "type": "string"
                  },
                  "path": {
                    "description": "Path to marketplace.json within repo (defaults to .claude-plugin/marketplace.json)",
                    "type": "string"
                  },
                  "sparsePaths": {
                    "description": "Directories to include via git sparse-checkout (cone mode). Use for monorepos where the marketplace lives in a subdirectory. Example: [\".claude-plugin\", \"plugins\"]. If omitted, the full repository is cloned.",
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  },
                  "skipLfs": {
                    "description": "Skip Git LFS smudge during clone and update (sets GIT_LFS_SKIP_SMUDGE=1) so LFS pointer files stay as pointers instead of downloading their content. Use for marketplaces hosted in repos with large LFS objects.",
                    "type": "boolean"
                  }
                },
                "required": [
                  "source",
                  "url"
                ]
              },
              {
                "type": "object",
                "properties": {
                  "source": {
                    "type": "string",
                    "const": "npm"
                  },
                  "package": {
                    "description": "NPM package containing marketplace.json",
                    "type": "string"
                  }
                },
                "required": [
                  "source",
                  "package"
                ]
              },
              {
                "type": "object",
                "properties": {
                  "source": {
                    "type": "string",
                    "const": "file"
                  },
                  "path": {
                    "description": "Local file path to marketplace.json",
                    "type": "string"
                  }
                },
                "required": [
                  "source",
                  "path"
                ]
              },
              {
                "type": "object",
                "properties": {
                  "source": {
                    "type": "string",
                    "const": "directory"
                  },
                  "path": {
                    "description": "Local directory containing .claude-plugin/marketplace.json",
                    "type": "string"
                  }
                },
                "required": [
                  "source",
                  "path"
                ]
              },
              {
                "description": "Policy-list sentinel for the ~/.claude/skills/ auto-load (@skills-dir plugins). In strictKnownMarketplaces: opt the scan back IN (by default any allowlist blocks it). In blockedMarketplaces: turn the scan OFF without otherwise restricting marketplaces. Only meaningful in those two managed-settings lists (areLocalPluginDirsAllowedByPolicy); known_marketplaces.json / marketplace add etc. ignore it.",
                "type": "object",
                "properties": {
                  "source": {
                    "type": "string",
                    "const": "skills-dir"
                  }
                },
                "required": [
                  "source"
                ]
              },
              {
                "type": "object",
                "properties": {
                  "source": {
                    "type": "string",
                    "const": "hostPattern"
                  },
                  "hostPattern": {
                    "description": "Regex pattern to match the host/domain extracted from any marketplace source type. For github sources, matches against github.com. For git sources (SSH or HTTPS), extracts the hostname from the URL. Use in strictKnownMarketplaces to allow all marketplaces from a specific host (e.g., \"^github\\.mycompany\\.com$\").",
                    "type": "string"
                  }
                },
                "required": [
                  "source",
                  "hostPattern"
                ]
              },
              {
                "type": "object",
                "properties": {
                  "source": {
                    "type": "string",
                    "const": "pathPattern"
                  },
                  "pathPattern": {
                    "description": "Regex pattern matched against the .path field of file and directory sources. Use in strictKnownMarketplaces to allow filesystem-based marketplaces alongside hostPattern restrictions for network sources. Use \".*\" to allow all filesystem paths, or a narrower pattern (e.g., \"^/opt/approved/\") to restrict to specific directories.",
                    "type": "string"
                  }
                },
                "required": [
                  "source",
                  "pathPattern"
                ]
              },
              {
                "description": "Inline marketplace manifest defined directly in settings.json. The reconciler writes a synthetic marketplace.json to the cache; diffMarketplaces detects edits via isEqual on the stored source (the plugins array is inside this object, so edits surface as sourceChanged).",
                "type": "object",
                "properties": {
                  "source": {
                    "type": "string",
                    "const": "settings"
                  },
                  "name": {
                    "description": "Marketplace name. Must match the extraKnownMarketplaces key (enforced); the synthetic manifest is written under this name. Same validation as PluginMarketplaceSchema plus reserved-name rejection — validateOfficialNameSource runs after the disk write, too late to clean up.",
                    "type": "string",
                    "minLength": 1
                  },
                  "plugins": {
                    "description": "Plugin entries declared inline in settings.json",
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "name": {
                          "description": "Plugin name as it appears in the target repository",
                          "type": "string",
                          "minLength": 1
                        },
                        "source": {
                          "description": "Where to fetch the plugin from. Must be a remote source — relative paths have no marketplace repository to resolve against.",
                          "anyOf": [
                            {
                              "description": "Path to the plugin root, relative to the marketplace root (the directory containing .claude-plugin/, not .claude-plugin/ itself)",
                              "type": "string",
                              "pattern": "^\\.\\/.*"
                            },
                            {
                              "description": "NPM package as plugin source",
                              "type": "object",
                              "properties": {
                                "source": {
                                  "type": "string",
                                  "const": "npm"
                                },
                                "package": {
                                  "description": "Package name (or url, or local path, or anything else that can be passed to `npm` as a package)",
                                  "anyOf": [
                                    {
                                      "type": "string"
                                    },
                                    {
                                      "type": "string"
                                    }
                                  ]
                                },
                                "version": {
                                  "description": "Specific version or version range (e.g., ^1.0.0, ~2.1.0)",
                                  "type": "string"
                                },
                                "registry": {
                                  "description": "Custom NPM registry URL (defaults to using system default, likely npmjs.org)",
                                  "type": "string",
                                  "format": "uri"
                                }
                              },
                              "required": [
                                "source",
                                "package"
                              ]
                            },
                            {
                              "type": "object",
                              "properties": {
                                "source": {
                                  "type": "string",
                                  "const": "url"
                                },
                                "url": {
                                  "description": "Full git repository URL (https:// or git@)",
                                  "type": "string"
                                },
                                "ref": {
                                  "description": "Git branch or tag to use (e.g., \"main\", \"v1.0.0\"). Defaults to repository default branch.",
                                  "type": "string"
                                },
                                "sha": {
                                  "description": "Specific commit SHA to use",
                                  "type": "string",
                                  "minLength": 40,
                                  "maxLength": 40,
                                  "pattern": "^[a-f0-9]{40}$"
                                }
                              },
                              "required": [
                                "source",
                                "url"
                              ]
                            },
                            {
                              "type": "object",
                              "properties": {
                                "source": {
                                  "type": "string",
                                  "const": "github"
                                },
                                "repo": {
                                  "description": "GitHub repository in owner/repo format",
                                  "type": "string"
                                },
                                "ref": {
                                  "description": "Git branch or tag to use (e.g., \"main\", \"v1.0.0\"). Defaults to repository default branch.",
                                  "type": "string"
                                },
                                "sha": {
                                  "description": "Specific commit SHA to use",
                                  "type": "string",
                                  "minLength": 40,
                                  "maxLength": 40,
                                  "pattern": "^[a-f0-9]{40}$"
                                }
                              },
                              "required": [
                                "source",
                                "repo"
                              ]
                            },
                            {
                              "description": "Plugin located in a subdirectory of a larger repository (monorepo). Only the specified subdirectory is materialized; the rest of the repo is not downloaded.",
                              "type": "object",
                              "properties": {
                                "source": {
                                  "type": "string",
                                  "const": "git-subdir"
                                },
                                "url": {
                                  "description": "Git repository: GitHub owner/repo shorthand, https://, or git@ URL",
                                  "type": "string"
                                },
                                "path": {
                                  "description": "Subdirectory within the repo containing the plugin (e.g., \"tools/claude-plugin\"). Cloned sparsely using partial clone (--filter=tree:0) to minimize bandwidth for monorepos.",
                                  "type": "string",
                                  "minLength": 1
                                },
                                "ref": {
                                  "description": "Git branch or tag to use (e.g., \"main\", \"v1.0.0\"). Defaults to repository default branch.",
                                  "type": "string"
                                },
                                "sha": {
                                  "description": "Specific commit SHA to use",
                                  "type": "string",
                                  "minLength": 40,
                                  "maxLength": 40,
                                  "pattern": "^[a-f0-9]{40}$"
                                }
                              },
                              "required": [
                                "source",
                                "url",
                                "path"
                              ]
                            },
                            {
                              "description": "Plugin distributed as a zip archive fetched over HTTPS — for hosting on any static file server or artifact repository (S3, GitLab, nginx) with no git or npm on the client. Authentication: the entry's own `headers` / `headersHelper` (bound to this URL), overlaid on the enclosing url-source marketplace's headers (static or `headersHelper`-minted) when the archive shares its origin.",
                              "type": "object",
                              "properties": {
                                "source": {
                                  "type": "string",
                                  "const": "archive"
                                },
                                "url": {
                                  "description": "HTTPS URL of a zip archive containing the plugin. The plugin root (the directory holding .claude-plugin/) may be at the top of the archive or nested one directory deep — a single wrapping directory is stripped.",
                                  "type": "string",
                                  "format": "uri"
                                },
                                "sha256": {
                                  "description": "SHA-256 digest of the archive. When set, every download is verified against it and the install is refused on mismatch. It also serves as the version identity when neither plugin.json nor the marketplace entry declares a `version`. Recommended. Note the update signal is the version string (plugin.json version, else the entry version, else this digest) — changing only the digest while a version is declared does not trigger an update.",
                                  "type": "string",
                                  "pattern": "^[0-9a-fA-F]{64}$"
                                }
                              },
                              "required": [
                                "source",
                                "url"
                              ]
                            },
                            {
                              "description": "Plugin directory produced by a locally installed tool (e.g. an IDE that renders its plugin for the currently selected SDK). Claude Code runs the command, copies the directory it prints, and re-runs it in the background at startup to pick up changes.",
                              "type": "object",
                              "properties": {
                                "source": {
                                  "type": "string",
                                  "const": "command"
                                },
                                "command": {
                                  "description": "Shell command that prints the absolute path of the plugin directory on stdout (exactly one line) and exits 0. It must leave a complete plugin in that directory before exiting; the directory is copied into the plugin cache, so the printed path may change between runs (it is re-resolved on every install and update, and once per session in the background). Runs through the platform shell (sh on macOS/Linux, cmd.exe on Windows) from the user's home directory with Claude Code's subprocess environment.",
                                  "type": "string",
                                  "minLength": 1,
                                  "maxLength": 500
                                },
                                "timeout": {
                                  "description": "Seconds to wait for the command before giving up (default: 60)",
                                  "type": "integer",
                                  "exclusiveMinimum": 0,
                                  "maximum": 600
                                },
                                "mode": {
                                  "description": "copy (default): the printed directory is copied into the plugin cache and content-hashed, so it may be deleted afterwards. link: the cache entry links to the printed directory in place (no copy, no size limit; macOS/Linux) — for large exports; the directory must then stay valid while Claude Code runs, and a different printed path is what signals new content.",
                                  "type": "string",
                                  "enum": [
                                    "copy",
                                    "link"
                                  ]
                                }
                              },
                              "required": [
                                "source",
                                "command"
                              ]
                            },
                            {
                              "description": "Placeholder for source types this Claude Code version does not recognize, or a known type whose fields failed validation (then `error` holds the reason). Never authored by hand — PluginMarketplaceSchema rewrites unparseable sources to this so the entry remains in marketplace.plugins (detectDelistedPlugins must not see it as removed). Install attempts fail at cachePlugin with an actionable message.",
                              "type": "object",
                              "properties": {
                                "source": {
                                  "type": "string",
                                  "const": "unsupported"
                                },
                                "error": {
                                  "type": "string"
                                }
                              },
                              "required": [
                                "source"
                              ]
                            }
                          ]
                        },
                        "description": {
                          "type": "string"
                        },
                        "version": {
                          "type": "string"
                        },
                        "strict": {
                          "type": "boolean"
                        },
                        "headers": {
                          "description": "HTTP headers sent when downloading this entry's `archive` source.",
                          "type": "object",
                          "propertyNames": {
                            "type": "string"
                          },
                          "additionalProperties": {
                            "type": "string"
                          }
                        },
                        "headersHelper": {
                          "description": "Command that prints a JSON object of HTTP headers for downloading this entry's `archive` source. Runs only when a user explicitly installs or updates this plugin. Unlike a catalog entry, an entry written here does not need `strict: false`: it is declared in a settings file, which has no manifest fields to inline. A declaration in project settings is not operator-authored, so request-routing and client-identity header names are still filtered there. Use an absolute path.",
                          "type": "string",
                          "maxLength": 500
                        }
                      },
                      "required": [
                        "name",
                        "source"
                      ]
                    }
                  },
                  "owner": {
                    "type": "object",
                    "properties": {
                      "name": {
                        "description": "Display name of the plugin author or organization",
                        "type": "string",
                        "minLength": 1
                      },
                      "email": {
                        "description": "Contact email for support or feedback",
                        "type": "string"
                      },
                      "url": {
                        "description": "Website, GitHub profile, or organization URL",
                        "type": "string"
                      }
                    },
                    "required": [
                      "name"
                    ]
                  }
                },
                "required": [
                  "source",
                  "name",
                  "plugins"
                ]
              }
            ]
          },
          "installLocation": {
            "description": "Local cache path where marketplace manifest is stored (auto-generated if not provided)",
            "type": "string"
          },
          "autoUpdate": {
            "description": "Whether to automatically update this marketplace and its installed plugins on startup",
            "type": "boolean"
          }
        },
        "required": [
          "source"
        ]
      }
    },
    "additionalMarketplaces": {
      "description": "Alias for extraKnownMarketplaces: this key is read exactly as if it were spelled extraKnownMarketplaces. Do not set both in one file — if both appear, this key is ignored with a warning. Claude Code may rewrite this key as extraKnownMarketplaces when it updates the file. Clients older than this alias ignore it, so prefer extraKnownMarketplaces while older Claude Code versions still share the same settings.",
      "type": "object",
      "propertyNames": {
        "type": "string"
      },
      "additionalProperties": {
        "type": "object",
        "properties": {
          "source": {
            "description": "Where to fetch the marketplace from",
            "anyOf": [
              {
                "type": "object",
                "properties": {
                  "source": {
                    "type": "string",
                    "const": "url"
                  },
                  "url": {
                    "description": "Direct URL to marketplace.json file",
                    "type": "string",
                    "format": "uri"
                  },
                  "headers": {
                    "description": "Custom HTTP headers (e.g., for authentication)",
                    "type": "object",
                    "propertyNames": {
                      "type": "string"
                    },
                    "additionalProperties": {
                      "type": "string"
                    }
                  },
                  "headersHelper": {
                    "description": "Command that prints a JSON object of HTTP headers (e.g. a short-lived auth token). Its output overrides `headers` and, like `headers`, is inherited by same-origin archive downloads from this marketplace. Runs from a fixed directory (the Claude config home, never the session's), so give a bare command found via PATH or an absolute path; it is re-run on later refreshes of this marketplace.",
                    "type": "string",
                    "maxLength": 500
                  }
                },
                "required": [
                  "source",
                  "url"
                ]
              },
              {
                "type": "object",
                "properties": {
                  "source": {
                    "type": "string",
                    "const": "github"
                  },
                  "repo": {
                    "description": "GitHub repository in owner/repo format. ONLY in the managed-settings policy lists (strictKnownMarketplaces / blockedMarketplaces) the owner-wildcard form \"owner/*\" matches every repository under exactly that owner. Everywhere else (marketplace add, extraKnownMarketplaces, known_marketplaces.json) the value must name a single repository — a wildcard is taken literally and fails to clone.",
                    "type": "string"
                  },
                  "ref": {
                    "description": "Git branch or tag to use (e.g., \"main\", \"v1.0.0\"). Defaults to repository default branch.",
                    "type": "string"
                  },
                  "path": {
                    "description": "Path to marketplace.json within repo (defaults to .claude-plugin/marketplace.json)",
                    "type": "string"
                  },
                  "sparsePaths": {
                    "description": "Directories to include via git sparse-checkout (cone mode). Use for monorepos where the marketplace lives in a subdirectory. Example: [\".claude-plugin\", \"plugins\"]. If omitted, the full repository is cloned.",
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  },
                  "skipLfs": {
                    "description": "Skip Git LFS smudge during clone and update (sets GIT_LFS_SKIP_SMUDGE=1) so LFS pointer files stay as pointers instead of downloading their content. Use for marketplaces hosted in repos with large LFS objects.",
                    "type": "boolean"
                  }
                },
                "required": [
                  "source",
                  "repo"
                ]
              },
              {
                "type": "object",
                "properties": {
                  "source": {
                    "type": "string",
                    "const": "git"
                  },
                  "url": {
                    "description": "Full git repository URL",
                    "type": "string"
                  },
                  "ref": {
                    "description": "Git branch or tag to use (e.g., \"main\", \"v1.0.0\"). Defaults to repository default branch.",
                    "type": "string"
                  },
                  "path": {
                    "description": "Path to marketplace.json within repo (defaults to .claude-plugin/marketplace.json)",
                    "type": "string"
                  },
                  "sparsePaths": {
                    "description": "Directories to include via git sparse-checkout (cone mode). Use for monorepos where the marketplace lives in a subdirectory. Example: [\".claude-plugin\", \"plugins\"]. If omitted, the full repository is cloned.",
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  },
                  "skipLfs": {
                    "description": "Skip Git LFS smudge during clone and update (sets GIT_LFS_SKIP_SMUDGE=1) so LFS pointer files stay as pointers instead of downloading their content. Use for marketplaces hosted in repos with large LFS objects.",
                    "type": "boolean"
                  }
                },
                "required": [
                  "source",
                  "url"
                ]
              },
              {
                "type": "object",
                "properties": {
                  "source": {
                    "type": "string",
                    "const": "npm"
                  },
                  "package": {
                    "description": "NPM package containing marketplace.json",
                    "type": "string"
                  }
                },
                "required": [
                  "source",
                  "package"
                ]
              },
              {
                "type": "object",
                "properties": {
                  "source": {
                    "type": "string",
                    "const": "file"
                  },
                  "path": {
                    "description": "Local file path to marketplace.json",
                    "type": "string"
                  }
                },
                "required": [
                  "source",
                  "path"
                ]
              },
              {
                "type": "object",
                "properties": {
                  "source": {
                    "type": "string",
                    "const": "directory"
                  },
                  "path": {
                    "description": "Local directory containing .claude-plugin/marketplace.json",
                    "type": "string"
                  }
                },
                "required": [
                  "source",
                  "path"
                ]
              },
              {
                "description": "Policy-list sentinel for the ~/.claude/skills/ auto-load (@skills-dir plugins). In strictKnownMarketplaces: opt the scan back IN (by default any allowlist blocks it). In blockedMarketplaces: turn the scan OFF without otherwise restricting marketplaces. Only meaningful in those two managed-settings lists (areLocalPluginDirsAllowedByPolicy); known_marketplaces.json / marketplace add etc. ignore it.",
                "type": "object",
                "properties": {
                  "source": {
                    "type": "string",
                    "const": "skills-dir"
                  }
                },
                "required": [
                  "source"
                ]
              },
              {
                "type": "object",
                "properties": {
                  "source": {
                    "type": "string",
                    "const": "hostPattern"
                  },
                  "hostPattern": {
                    "description": "Regex pattern to match the host/domain extracted from any marketplace source type. For github sources, matches against github.com. For git sources (SSH or HTTPS), extracts the hostname from the URL. Use in strictKnownMarketplaces to allow all marketplaces from a specific host (e.g., \"^github\\.mycompany\\.com$\").",
                    "type": "string"
                  }
                },
                "required": [
                  "source",
                  "hostPattern"
                ]
              },
              {
                "type": "object",
                "properties": {
                  "source": {
                    "type": "string",
                    "const": "pathPattern"
                  },
                  "pathPattern": {
                    "description": "Regex pattern matched against the .path field of file and directory sources. Use in strictKnownMarketplaces to allow filesystem-based marketplaces alongside hostPattern restrictions for network sources. Use \".*\" to allow all filesystem paths, or a narrower pattern (e.g., \"^/opt/approved/\") to restrict to specific directories.",
                    "type": "string"
                  }
                },
                "required": [
                  "source",
                  "pathPattern"
                ]
              },
              {
                "description": "Inline marketplace manifest defined directly in settings.json. The reconciler writes a synthetic marketplace.json to the cache; diffMarketplaces detects edits via isEqual on the stored source (the plugins array is inside this object, so edits surface as sourceChanged).",
                "type": "object",
                "properties": {
                  "source": {
                    "type": "string",
                    "const": "settings"
                  },
                  "name": {
                    "description": "Marketplace name. Must match the extraKnownMarketplaces key (enforced); the synthetic manifest is written under this name. Same validation as PluginMarketplaceSchema plus reserved-name rejection — validateOfficialNameSource runs after the disk write, too late to clean up.",
                    "type": "string",
                    "minLength": 1
                  },
                  "plugins": {
                    "description": "Plugin entries declared inline in settings.json",
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "name": {
                          "description": "Plugin name as it appears in the target repository",
                          "type": "string",
                          "minLength": 1
                        },
                        "source": {
                          "description": "Where to fetch the plugin from. Must be a remote source — relative paths have no marketplace repository to resolve against.",
                          "anyOf": [
                            {
                              "description": "Path to the plugin root, relative to the marketplace root (the directory containing .claude-plugin/, not .claude-plugin/ itself)",
                              "type": "string",
                              "pattern": "^\\.\\/.*"
                            },
                            {
                              "description": "NPM package as plugin source",
                              "type": "object",
                              "properties": {
                                "source": {
                                  "type": "string",
                                  "const": "npm"
                                },
                                "package": {
                                  "description": "Package name (or url, or local path, or anything else that can be passed to `npm` as a package)",
                                  "anyOf": [
                                    {
                                      "type": "string"
                                    },
                                    {
                                      "type": "string"
                                    }
                                  ]
                                },
                                "version": {
                                  "description": "Specific version or version range (e.g., ^1.0.0, ~2.1.0)",
                                  "type": "string"
                                },
                                "registry": {
                                  "description": "Custom NPM registry URL (defaults to using system default, likely npmjs.org)",
                                  "type": "string",
                                  "format": "uri"
                                }
                              },
                              "required": [
                                "source",
                                "package"
                              ]
                            },
                            {
                              "type": "object",
                              "properties": {
                                "source": {
                                  "type": "string",
                                  "const": "url"
                                },
                                "url": {
                                  "description": "Full git repository URL (https:// or git@)",
                                  "type": "string"
                                },
                                "ref": {
                                  "description": "Git branch or tag to use (e.g., \"main\", \"v1.0.0\"). Defaults to repository default branch.",
                                  "type": "string"
                                },
                                "sha": {
                                  "description": "Specific commit SHA to use",
                                  "type": "string",
                                  "minLength": 40,
                                  "maxLength": 40,
                                  "pattern": "^[a-f0-9]{40}$"
                                }
                              },
                              "required": [
                                "source",
                                "url"
                              ]
                            },
                            {
                              "type": "object",
                              "properties": {
                                "source": {
                                  "type": "string",
                                  "const": "github"
                                },
                                "repo": {
                                  "description": "GitHub repository in owner/repo format",
                                  "type": "string"
                                },
                                "ref": {
                                  "description": "Git branch or tag to use (e.g., \"main\", \"v1.0.0\"). Defaults to repository default branch.",
                                  "type": "string"
                                },
                                "sha": {
                                  "description": "Specific commit SHA to use",
                                  "type": "string",
                                  "minLength": 40,
                                  "maxLength": 40,
                                  "pattern": "^[a-f0-9]{40}$"
                                }
                              },
                              "required": [
                                "source",
                                "repo"
                              ]
                            },
                            {
                              "description": "Plugin located in a subdirectory of a larger repository (monorepo). Only the specified subdirectory is materialized; the rest of the repo is not downloaded.",
                              "type": "object",
                              "properties": {
                                "source": {
                                  "type": "string",
                                  "const": "git-subdir"
                                },
                                "url": {
                                  "description": "Git repository: GitHub owner/repo shorthand, https://, or git@ URL",
                                  "type": "string"
                                },
                                "path": {
                                  "description": "Subdirectory within the repo containing the plugin (e.g., \"tools/claude-plugin\"). Cloned sparsely using partial clone (--filter=tree:0) to minimize bandwidth for monorepos.",
                                  "type": "string",
                                  "minLength": 1
                                },
                                "ref": {
                                  "description": "Git branch or tag to use (e.g., \"main\", \"v1.0.0\"). Defaults to repository default branch.",
                                  "type": "string"
                                },
                                "sha": {
                                  "description": "Specific commit SHA to use",
                                  "type": "string",
                                  "minLength": 40,
                                  "maxLength": 40,
                                  "pattern": "^[a-f0-9]{40}$"
                                }
                              },
                              "required": [
                                "source",
                                "url",
                                "path"
                              ]
                            },
                            {
                              "description": "Plugin distributed as a zip archive fetched over HTTPS — for hosting on any static file server or artifact repository (S3, GitLab, nginx) with no git or npm on the client. Authentication: the entry's own `headers` / `headersHelper` (bound to this URL), overlaid on the enclosing url-source marketplace's headers (static or `headersHelper`-minted) when the archive shares its origin.",
                              "type": "object",
                              "properties": {
                                "source": {
                                  "type": "string",
                                  "const": "archive"
                                },
                                "url": {
                                  "description": "HTTPS URL of a zip archive containing the plugin. The plugin root (the directory holding .claude-plugin/) may be at the top of the archive or nested one directory deep — a single wrapping directory is stripped.",
                                  "type": "string",
                                  "format": "uri"
                                },
                                "sha256": {
                                  "description": "SHA-256 digest of the archive. When set, every download is verified against it and the install is refused on mismatch. It also serves as the version identity when neither plugin.json nor the marketplace entry declares a `version`. Recommended. Note the update signal is the version string (plugin.json version, else the entry version, else this digest) — changing only the digest while a version is declared does not trigger an update.",
                                  "type": "string",
                                  "pattern": "^[0-9a-fA-F]{64}$"
                                }
                              },
                              "required": [
                                "source",
                                "url"
                              ]
                            },
                            {
                              "description": "Plugin directory produced by a locally installed tool (e.g. an IDE that renders its plugin for the currently selected SDK). Claude Code runs the command, copies the directory it prints, and re-runs it in the background at startup to pick up changes.",
                              "type": "object",
                              "properties": {
                                "source": {
                                  "type": "string",
                                  "const": "command"
                                },
                                "command": {
                                  "description": "Shell command that prints the absolute path of the plugin directory on stdout (exactly one line) and exits 0. It must leave a complete plugin in that directory before exiting; the directory is copied into the plugin cache, so the printed path may change between runs (it is re-resolved on every install and update, and once per session in the background). Runs through the platform shell (sh on macOS/Linux, cmd.exe on Windows) from the user's home directory with Claude Code's subprocess environment.",
                                  "type": "string",
                                  "minLength": 1,
                                  "maxLength": 500
                                },
                                "timeout": {
                                  "description": "Seconds to wait for the command before giving up (default: 60)",
                                  "type": "integer",
                                  "exclusiveMinimum": 0,
                                  "maximum": 600
                                },
                                "mode": {
                                  "description": "copy (default): the printed directory is copied into the plugin cache and content-hashed, so it may be deleted afterwards. link: the cache entry links to the printed directory in place (no copy, no size limit; macOS/Linux) — for large exports; the directory must then stay valid while Claude Code runs, and a different printed path is what signals new content.",
                                  "type": "string",
                                  "enum": [
                                    "copy",
                                    "link"
                                  ]
                                }
                              },
                              "required": [
                                "source",
                                "command"
                              ]
                            },
                            {
                              "description": "Placeholder for source types this Claude Code version does not recognize, or a known type whose fields failed validation (then `error` holds the reason). Never authored by hand — PluginMarketplaceSchema rewrites unparseable sources to this so the entry remains in marketplace.plugins (detectDelistedPlugins must not see it as removed). Install attempts fail at cachePlugin with an actionable message.",
                              "type": "object",
                              "properties": {
                                "source": {
                                  "type": "string",
                                  "const": "unsupported"
                                },
                                "error": {
                                  "type": "string"
                                }
                              },
                              "required": [
                                "source"
                              ]
                            }
                          ]
                        },
                        "description": {
                          "type": "string"
                        },
                        "version": {
                          "type": "string"
                        },
                        "strict": {
                          "type": "boolean"
                        },
                        "headers": {
                          "description": "HTTP headers sent when downloading this entry's `archive` source.",
                          "type": "object",
                          "propertyNames": {
                            "type": "string"
                          },
                          "additionalProperties": {
                            "type": "string"
                          }
                        },
                        "headersHelper": {
                          "description": "Command that prints a JSON object of HTTP headers for downloading this entry's `archive` source. Runs only when a user explicitly installs or updates this plugin. Unlike a catalog entry, an entry written here does not need `strict: false`: it is declared in a settings file, which has no manifest fields to inline. A declaration in project settings is not operator-authored, so request-routing and client-identity header names are still filtered there. Use an absolute path.",
                          "type": "string",
                          "maxLength": 500
                        }
                      },
                      "required": [
                        "name",
                        "source"
                      ]
                    }
                  },
                  "owner": {
                    "type": "object",
                    "properties": {
                      "name": {
                        "description": "Display name of the plugin author or organization",
                        "type": "string",
                        "minLength": 1
                      },
                      "email": {
                        "description": "Contact email for support or feedback",
                        "type": "string"
                      },
                      "url": {
                        "description": "Website, GitHub profile, or organization URL",
                        "type": "string"
                      }
                    },
                    "required": [
                      "name"
                    ]
                  }
                },
                "required": [
                  "source",
                  "name",
                  "plugins"
                ]
              }
            ]
          },
          "installLocation": {
            "description": "Local cache path where marketplace manifest is stored (auto-generated if not provided)",
            "type": "string"
          },
          "autoUpdate": {
            "description": "Whether to automatically update this marketplace and its installed plugins on startup",
            "type": "boolean"
          }
        },
        "required": [
          "source"
        ]
      }
    },
    "strictKnownMarketplaces": {
      "description": "Enterprise strict list of allowed marketplace sources. When set in managed settings, ONLY these sources can be added as marketplaces. Entries match exactly, except that a github entry may use the owner-wildcard form {\"source\":\"github\",\"repo\":\"owner/*\"} to allow every repository under that owner. The check happens BEFORE downloading, so blocked sources never touch the filesystem. Note: this is a policy gate only — it does NOT register marketplaces. To pre-register allowed marketplaces for users, also set extraKnownMarketplaces.",
      "type": "array",
      "items": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "source": {
                "type": "string",
                "const": "url"
              },
              "url": {
                "description": "Direct URL to marketplace.json file",
                "type": "string",
                "format": "uri"
              },
              "headers": {
                "description": "Custom HTTP headers (e.g., for authentication)",
                "type": "object",
                "propertyNames": {
                  "type": "string"
                },
                "additionalProperties": {
                  "type": "string"
                }
              },
              "headersHelper": {
                "description": "Command that prints a JSON object of HTTP headers (e.g. a short-lived auth token). Its output overrides `headers` and, like `headers`, is inherited by same-origin archive downloads from this marketplace. Runs from a fixed directory (the Claude config home, never the session's), so give a bare command found via PATH or an absolute path; it is re-run on later refreshes of this marketplace.",
                "type": "string",
                "maxLength": 500
              }
            },
            "required": [
              "source",
              "url"
            ]
          },
          {
            "type": "object",
            "properties": {
              "source": {
                "type": "string",
                "const": "github"
              },
              "repo": {
                "description": "GitHub repository in owner/repo format. ONLY in the managed-settings policy lists (strictKnownMarketplaces / blockedMarketplaces) the owner-wildcard form \"owner/*\" matches every repository under exactly that owner. Everywhere else (marketplace add, extraKnownMarketplaces, known_marketplaces.json) the value must name a single repository — a wildcard is taken literally and fails to clone.",
                "type": "string"
              },
              "ref": {
                "description": "Git branch or tag to use (e.g., \"main\", \"v1.0.0\"). Defaults to repository default branch.",
                "type": "string"
              },
              "path": {
                "description": "Path to marketplace.json within repo (defaults to .claude-plugin/marketplace.json)",
                "type": "string"
              },
              "sparsePaths": {
                "description": "Directories to include via git sparse-checkout (cone mode). Use for monorepos where the marketplace lives in a subdirectory. Example: [\".claude-plugin\", \"plugins\"]. If omitted, the full repository is cloned.",
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "skipLfs": {
                "description": "Skip Git LFS smudge during clone and update (sets GIT_LFS_SKIP_SMUDGE=1) so LFS pointer files stay as pointers instead of downloading their content. Use for marketplaces hosted in repos with large LFS objects.",
                "type": "boolean"
              }
            },
            "required": [
              "source",
              "repo"
            ]
          },
          {
            "type": "object",
            "properties": {
              "source": {
                "type": "string",
                "const": "git"
              },
              "url": {
                "description": "Full git repository URL",
                "type": "string"
              },
              "ref": {
                "description": "Git branch or tag to use (e.g., \"main\", \"v1.0.0\"). Defaults to repository default branch.",
                "type": "string"
              },
              "path": {
                "description": "Path to marketplace.json within repo (defaults to .claude-plugin/marketplace.json)",
                "type": "string"
              },
              "sparsePaths": {
                "description": "Directories to include via git sparse-checkout (cone mode). Use for monorepos where the marketplace lives in a subdirectory. Example: [\".claude-plugin\", \"plugins\"]. If omitted, the full repository is cloned.",
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "skipLfs": {
                "description": "Skip Git LFS smudge during clone and update (sets GIT_LFS_SKIP_SMUDGE=1) so LFS pointer files stay as pointers instead of downloading their content. Use for marketplaces hosted in repos with large LFS objects.",
                "type": "boolean"
              }
            },
            "required": [
              "source",
              "url"
            ]
          },
          {
            "type": "object",
            "properties": {
              "source": {
                "type": "string",
                "const": "npm"
              },
              "package": {
                "description": "NPM package containing marketplace.json",
                "type": "string"
              }
            },
            "required": [
              "source",
              "package"
            ]
          },
          {
            "type": "object",
            "properties": {
              "source": {
                "type": "string",
                "const": "file"
              },
              "path": {
                "description": "Local file path to marketplace.json",
                "type": "string"
              }
            },
            "required": [
              "source",
              "path"
            ]
          },
          {
            "type": "object",
            "properties": {
              "source": {
                "type": "string",
                "const": "directory"
              },
              "path": {
                "description": "Local directory containing .claude-plugin/marketplace.json",
                "type": "string"
              }
            },
            "required": [
              "source",
              "path"
            ]
          },
          {
            "description": "Policy-list sentinel for the ~/.claude/skills/ auto-load (@skills-dir plugins). In strictKnownMarketplaces: opt the scan back IN (by default any allowlist blocks it). In blockedMarketplaces: turn the scan OFF without otherwise restricting marketplaces. Only meaningful in those two managed-settings lists (areLocalPluginDirsAllowedByPolicy); known_marketplaces.json / marketplace add etc. ignore it.",
            "type": "object",
            "properties": {
              "source": {
                "type": "string",
                "const": "skills-dir"
              }
            },
            "required": [
              "source"
            ]
          },
          {
            "type": "object",
            "properties": {
              "source": {
                "type": "string",
                "const": "hostPattern"
              },
              "hostPattern": {
                "description": "Regex pattern to match the host/domain extracted from any marketplace source type. For github sources, matches against github.com. For git sources (SSH or HTTPS), extracts the hostname from the URL. Use in strictKnownMarketplaces to allow all marketplaces from a specific host (e.g., \"^github\\.mycompany\\.com$\").",
                "type": "string"
              }
            },
            "required": [
              "source",
              "hostPattern"
            ]
          },
          {
            "type": "object",
            "properties": {
              "source": {
                "type": "string",
                "const": "pathPattern"
              },
              "pathPattern": {
                "description": "Regex pattern matched against the .path field of file and directory sources. Use in strictKnownMarketplaces to allow filesystem-based marketplaces alongside hostPattern restrictions for network sources. Use \".*\" to allow all filesystem paths, or a narrower pattern (e.g., \"^/opt/approved/\") to restrict to specific directories.",
                "type": "string"
              }
            },
            "required": [
              "source",
              "pathPattern"
            ]
          },
          {
            "description": "Inline marketplace manifest defined directly in settings.json. The reconciler writes a synthetic marketplace.json to the cache; diffMarketplaces detects edits via isEqual on the stored source (the plugins array is inside this object, so edits surface as sourceChanged).",
            "type": "object",
            "properties": {
              "source": {
                "type": "string",
                "const": "settings"
              },
              "name": {
                "description": "Marketplace name. Must match the extraKnownMarketplaces key (enforced); the synthetic manifest is written under this name. Same validation as PluginMarketplaceSchema plus reserved-name rejection — validateOfficialNameSource runs after the disk write, too late to clean up.",
                "type": "string",
                "minLength": 1
              },
              "plugins": {
                "description": "Plugin entries declared inline in settings.json",
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "description": "Plugin name as it appears in the target repository",
                      "type": "string",
                      "minLength": 1
                    },
                    "source": {
                      "description": "Where to fetch the plugin from. Must be a remote source — relative paths have no marketplace repository to resolve against.",
                      "anyOf": [
                        {
                          "description": "Path to the plugin root, relative to the marketplace root (the directory containing .claude-plugin/, not .claude-plugin/ itself)",
                          "type": "string",
                          "pattern": "^\\.\\/.*"
                        },
                        {
                          "description": "NPM package as plugin source",
                          "type": "object",
                          "properties": {
                            "source": {
                              "type": "string",
                              "const": "npm"
                            },
                            "package": {
                              "description": "Package name (or url, or local path, or anything else that can be passed to `npm` as a package)",
                              "anyOf": [
                                {
                                  "type": "string"
                                },
                                {
                                  "type": "string"
                                }
                              ]
                            },
                            "version": {
                              "description": "Specific version or version range (e.g., ^1.0.0, ~2.1.0)",
                              "type": "string"
                            },
                            "registry": {
                              "description": "Custom NPM registry URL (defaults to using system default, likely npmjs.org)",
                              "type": "string",
                              "format": "uri"
                            }
                          },
                          "required": [
                            "source",
                            "package"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "source": {
                              "type": "string",
                              "const": "url"
                            },
                            "url": {
                              "description": "Full git repository URL (https:// or git@)",
                              "type": "string"
                            },
                            "ref": {
                              "description": "Git branch or tag to use (e.g., \"main\", \"v1.0.0\"). Defaults to repository default branch.",
                              "type": "string"
                            },
                            "sha": {
                              "description": "Specific commit SHA to use",
                              "type": "string",
                              "minLength": 40,
                              "maxLength": 40,
                              "pattern": "^[a-f0-9]{40}$"
                            }
                          },
                          "required": [
                            "source",
                            "url"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "source": {
                              "type": "string",
                              "const": "github"
                            },
                            "repo": {
                              "description": "GitHub repository in owner/repo format",
                              "type": "string"
                            },
                            "ref": {
                              "description": "Git branch or tag to use (e.g., \"main\", \"v1.0.0\"). Defaults to repository default branch.",
                              "type": "string"
                            },
                            "sha": {
                              "description": "Specific commit SHA to use",
                              "type": "string",
                              "minLength": 40,
                              "maxLength": 40,
                              "pattern": "^[a-f0-9]{40}$"
                            }
                          },
                          "required": [
                            "source",
                            "repo"
                          ]
                        },
                        {
                          "description": "Plugin located in a subdirectory of a larger repository (monorepo). Only the specified subdirectory is materialized; the rest of the repo is not downloaded.",
                          "type": "object",
                          "properties": {
                            "source": {
                              "type": "string",
                              "const": "git-subdir"
                            },
                            "url": {
                              "description": "Git repository: GitHub owner/repo shorthand, https://, or git@ URL",
                              "type": "string"
                            },
                            "path": {
                              "description": "Subdirectory within the repo containing the plugin (e.g., \"tools/claude-plugin\"). Cloned sparsely using partial clone (--filter=tree:0) to minimize bandwidth for monorepos.",
                              "type": "string",
                              "minLength": 1
                            },
                            "ref": {
                              "description": "Git branch or tag to use (e.g., \"main\", \"v1.0.0\"). Defaults to repository default branch.",
                              "type": "string"
                            },
                            "sha": {
                              "description": "Specific commit SHA to use",
                              "type": "string",
                              "minLength": 40,
                              "maxLength": 40,
                              "pattern": "^[a-f0-9]{40}$"
                            }
                          },
                          "required": [
                            "source",
                            "url",
                            "path"
                          ]
                        },
                        {
                          "description": "Plugin distributed as a zip archive fetched over HTTPS — for hosting on any static file server or artifact repository (S3, GitLab, nginx) with no git or npm on the client. Authentication: the entry's own `headers` / `headersHelper` (bound to this URL), overlaid on the enclosing url-source marketplace's headers (static or `headersHelper`-minted) when the archive shares its origin.",
                          "type": "object",
                          "properties": {
                            "source": {
                              "type": "string",
                              "const": "archive"
                            },
                            "url": {
                              "description": "HTTPS URL of a zip archive containing the plugin. The plugin root (the directory holding .claude-plugin/) may be at the top of the archive or nested one directory deep — a single wrapping directory is stripped.",
                              "type": "string",
                              "format": "uri"
                            },
                            "sha256": {
                              "description": "SHA-256 digest of the archive. When set, every download is verified against it and the install is refused on mismatch. It also serves as the version identity when neither plugin.json nor the marketplace entry declares a `version`. Recommended. Note the update signal is the version string (plugin.json version, else the entry version, else this digest) — changing only the digest while a version is declared does not trigger an update.",
                              "type": "string",
                              "pattern": "^[0-9a-fA-F]{64}$"
                            }
                          },
                          "required": [
                            "source",
                            "url"
                          ]
                        },
                        {
                          "description": "Plugin directory produced by a locally installed tool (e.g. an IDE that renders its plugin for the currently selected SDK). Claude Code runs the command, copies the directory it prints, and re-runs it in the background at startup to pick up changes.",
                          "type": "object",
                          "properties": {
                            "source": {
                              "type": "string",
                              "const": "command"
                            },
                            "command": {
                              "description": "Shell command that prints the absolute path of the plugin directory on stdout (exactly one line) and exits 0. It must leave a complete plugin in that directory before exiting; the directory is copied into the plugin cache, so the printed path may change between runs (it is re-resolved on every install and update, and once per session in the background). Runs through the platform shell (sh on macOS/Linux, cmd.exe on Windows) from the user's home directory with Claude Code's subprocess environment.",
                              "type": "string",
                              "minLength": 1,
                              "maxLength": 500
                            },
                            "timeout": {
                              "description": "Seconds to wait for the command before giving up (default: 60)",
                              "type": "integer",
                              "exclusiveMinimum": 0,
                              "maximum": 600
                            },
                            "mode": {
                              "description": "copy (default): the printed directory is copied into the plugin cache and content-hashed, so it may be deleted afterwards. link: the cache entry links to the printed directory in place (no copy, no size limit; macOS/Linux) — for large exports; the directory must then stay valid while Claude Code runs, and a different printed path is what signals new content.",
                              "type": "string",
                              "enum": [
                                "copy",
                                "link"
                              ]
                            }
                          },
                          "required": [
                            "source",
                            "command"
                          ]
                        },
                        {
                          "description": "Placeholder for source types this Claude Code version does not recognize, or a known type whose fields failed validation (then `error` holds the reason). Never authored by hand — PluginMarketplaceSchema rewrites unparseable sources to this so the entry remains in marketplace.plugins (detectDelistedPlugins must not see it as removed). Install attempts fail at cachePlugin with an actionable message.",
                          "type": "object",
                          "properties": {
                            "source": {
                              "type": "string",
                              "const": "unsupported"
                            },
                            "error": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "source"
                          ]
                        }
                      ]
                    },
                    "description": {
                      "type": "string"
                    },
                    "version": {
                      "type": "string"
                    },
                    "strict": {
                      "type": "boolean"
                    },
                    "headers": {
                      "description": "HTTP headers sent when downloading this entry's `archive` source.",
                      "type": "object",
                      "propertyNames": {
                        "type": "string"
                      },
                      "additionalProperties": {
                        "type": "string"
                      }
                    },
                    "headersHelper": {
                      "description": "Command that prints a JSON object of HTTP headers for downloading this entry's `archive` source. Runs only when a user explicitly installs or updates this plugin. Unlike a catalog entry, an entry written here does not need `strict: false`: it is declared in a settings file, which has no manifest fields to inline. A declaration in project settings is not operator-authored, so request-routing and client-identity header names are still filtered there. Use an absolute path.",
                      "type": "string",
                      "maxLength": 500
                    }
                  },
                  "required": [
                    "name",
                    "source"
                  ]
                }
              },
              "owner": {
                "type": "object",
                "properties": {
                  "name": {
                    "description": "Display name of the plugin author or organization",
                    "type": "string",
                    "minLength": 1
                  },
                  "email": {
                    "description": "Contact email for support or feedback",
                    "type": "string"
                  },
                  "url": {
                    "description": "Website, GitHub profile, or organization URL",
                    "type": "string"
                  }
                },
                "required": [
                  "name"
                ]
              }
            },
            "required": [
              "source",
              "name",
              "plugins"
            ]
          }
        ]
      }
    },
    "allowedMarketplaces": {
      "description": "Alias for strictKnownMarketplaces (managed settings only): this key is read exactly as if it were spelled strictKnownMarketplaces. Do not set both in one file — if both appear, this key is ignored with a warning. Clients older than this alias ignore it, so keep using strictKnownMarketplaces when the allowlist must also bind older Claude Code versions.",
      "type": "array",
      "items": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "source": {
                "type": "string",
                "const": "url"
              },
              "url": {
                "description": "Direct URL to marketplace.json file",
                "type": "string",
                "format": "uri"
              },
              "headers": {
                "description": "Custom HTTP headers (e.g., for authentication)",
                "type": "object",
                "propertyNames": {
                  "type": "string"
                },
                "additionalProperties": {
                  "type": "string"
                }
              },
              "headersHelper": {
                "description": "Command that prints a JSON object of HTTP headers (e.g. a short-lived auth token). Its output overrides `headers` and, like `headers`, is inherited by same-origin archive downloads from this marketplace. Runs from a fixed directory (the Claude config home, never the session's), so give a bare command found via PATH or an absolute path; it is re-run on later refreshes of this marketplace.",
                "type": "string",
                "maxLength": 500
              }
            },
            "required": [
              "source",
              "url"
            ]
          },
          {
            "type": "object",
            "properties": {
              "source": {
                "type": "string",
                "const": "github"
              },
              "repo": {
                "description": "GitHub repository in owner/repo format. ONLY in the managed-settings policy lists (strictKnownMarketplaces / blockedMarketplaces) the owner-wildcard form \"owner/*\" matches every repository under exactly that owner. Everywhere else (marketplace add, extraKnownMarketplaces, known_marketplaces.json) the value must name a single repository — a wildcard is taken literally and fails to clone.",
                "type": "string"
              },
              "ref": {
                "description": "Git branch or tag to use (e.g., \"main\", \"v1.0.0\"). Defaults to repository default branch.",
                "type": "string"
              },
              "path": {
                "description": "Path to marketplace.json within repo (defaults to .claude-plugin/marketplace.json)",
                "type": "string"
              },
              "sparsePaths": {
                "description": "Directories to include via git sparse-checkout (cone mode). Use for monorepos where the marketplace lives in a subdirectory. Example: [\".claude-plugin\", \"plugins\"]. If omitted, the full repository is cloned.",
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "skipLfs": {
                "description": "Skip Git LFS smudge during clone and update (sets GIT_LFS_SKIP_SMUDGE=1) so LFS pointer files stay as pointers instead of downloading their content. Use for marketplaces hosted in repos with large LFS objects.",
                "type": "boolean"
              }
            },
            "required": [
              "source",
              "repo"
            ]
          },
          {
            "type": "object",
            "properties": {
              "source": {
                "type": "string",
                "const": "git"
              },
              "url": {
                "description": "Full git repository URL",
                "type": "string"
              },
              "ref": {
                "description": "Git branch or tag to use (e.g., \"main\", \"v1.0.0\"). Defaults to repository default branch.",
                "type": "string"
              },
              "path": {
                "description": "Path to marketplace.json within repo (defaults to .claude-plugin/marketplace.json)",
                "type": "string"
              },
              "sparsePaths": {
                "description": "Directories to include via git sparse-checkout (cone mode). Use for monorepos where the marketplace lives in a subdirectory. Example: [\".claude-plugin\", \"plugins\"]. If omitted, the full repository is cloned.",
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "skipLfs": {
                "description": "Skip Git LFS smudge during clone and update (sets GIT_LFS_SKIP_SMUDGE=1) so LFS pointer files stay as pointers instead of downloading their content. Use for marketplaces hosted in repos with large LFS objects.",
                "type": "boolean"
              }
            },
            "required": [
              "source",
              "url"
            ]
          },
          {
            "type": "object",
            "properties": {
              "source": {
                "type": "string",
                "const": "npm"
              },
              "package": {
                "description": "NPM package containing marketplace.json",
                "type": "string"
              }
            },
            "required": [
              "source",
              "package"
            ]
          },
          {
            "type": "object",
            "properties": {
              "source": {
                "type": "string",
                "const": "file"
              },
              "path": {
                "description": "Local file path to marketplace.json",
                "type": "string"
              }
            },
            "required": [
              "source",
              "path"
            ]
          },
          {
            "type": "object",
            "properties": {
              "source": {
                "type": "string",
                "const": "directory"
              },
              "path": {
                "description": "Local directory containing .claude-plugin/marketplace.json",
                "type": "string"
              }
            },
            "required": [
              "source",
              "path"
            ]
          },
          {
            "description": "Policy-list sentinel for the ~/.claude/skills/ auto-load (@skills-dir plugins). In strictKnownMarketplaces: opt the scan back IN (by default any allowlist blocks it). In blockedMarketplaces: turn the scan OFF without otherwise restricting marketplaces. Only meaningful in those two managed-settings lists (areLocalPluginDirsAllowedByPolicy); known_marketplaces.json / marketplace add etc. ignore it.",
            "type": "object",
            "properties": {
              "source": {
                "type": "string",
                "const": "skills-dir"
              }
            },
            "required": [
              "source"
            ]
          },
          {
            "type": "object",
            "properties": {
              "source": {
                "type": "string",
                "const": "hostPattern"
              },
              "hostPattern": {
                "description": "Regex pattern to match the host/domain extracted from any marketplace source type. For github sources, matches against github.com. For git sources (SSH or HTTPS), extracts the hostname from the URL. Use in strictKnownMarketplaces to allow all marketplaces from a specific host (e.g., \"^github\\.mycompany\\.com$\").",
                "type": "string"
              }
            },
            "required": [
              "source",
              "hostPattern"
            ]
          },
          {
            "type": "object",
            "properties": {
              "source": {
                "type": "string",
                "const": "pathPattern"
              },
              "pathPattern": {
                "description": "Regex pattern matched against the .path field of file and directory sources. Use in strictKnownMarketplaces to allow filesystem-based marketplaces alongside hostPattern restrictions for network sources. Use \".*\" to allow all filesystem paths, or a narrower pattern (e.g., \"^/opt/approved/\") to restrict to specific directories.",
                "type": "string"
              }
            },
            "required": [
              "source",
              "pathPattern"
            ]
          },
          {
            "description": "Inline marketplace manifest defined directly in settings.json. The reconciler writes a synthetic marketplace.json to the cache; diffMarketplaces detects edits via isEqual on the stored source (the plugins array is inside this object, so edits surface as sourceChanged).",
            "type": "object",
            "properties": {
              "source": {
                "type": "string",
                "const": "settings"
              },
              "name": {
                "description": "Marketplace name. Must match the extraKnownMarketplaces key (enforced); the synthetic manifest is written under this name. Same validation as PluginMarketplaceSchema plus reserved-name rejection — validateOfficialNameSource runs after the disk write, too late to clean up.",
                "type": "string",
                "minLength": 1
              },
              "plugins": {
                "description": "Plugin entries declared inline in settings.json",
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "description": "Plugin name as it appears in the target repository",
                      "type": "string",
                      "minLength": 1
                    },
                    "source": {
                      "description": "Where to fetch the plugin from. Must be a remote source — relative paths have no marketplace repository to resolve against.",
                      "anyOf": [
                        {
                          "description": "Path to the plugin root, relative to the marketplace root (the directory containing .claude-plugin/, not .claude-plugin/ itself)",
                          "type": "string",
                          "pattern": "^\\.\\/.*"
                        },
                        {
                          "description": "NPM package as plugin source",
                          "type": "object",
                          "properties": {
                            "source": {
                              "type": "string",
                              "const": "npm"
                            },
                            "package": {
                              "description": "Package name (or url, or local path, or anything else that can be passed to `npm` as a package)",
                              "anyOf": [
                                {
                                  "type": "string"
                                },
                                {
                                  "type": "string"
                                }
                              ]
                            },
                            "version": {
                              "description": "Specific version or version range (e.g., ^1.0.0, ~2.1.0)",
                              "type": "string"
                            },
                            "registry": {
                              "description": "Custom NPM registry URL (defaults to using system default, likely npmjs.org)",
                              "type": "string",
                              "format": "uri"
                            }
                          },
                          "required": [
                            "source",
                            "package"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "source": {
                              "type": "string",
                              "const": "url"
                            },
                            "url": {
                              "description": "Full git repository URL (https:// or git@)",
                              "type": "string"
                            },
                            "ref": {
                              "description": "Git branch or tag to use (e.g., \"main\", \"v1.0.0\"). Defaults to repository default branch.",
                              "type": "string"
                            },
                            "sha": {
                              "description": "Specific commit SHA to use",
                              "type": "string",
                              "minLength": 40,
                              "maxLength": 40,
                              "pattern": "^[a-f0-9]{40}$"
                            }
                          },
                          "required": [
                            "source",
                            "url"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "source": {
                              "type": "string",
                              "const": "github"
                            },
                            "repo": {
                              "description": "GitHub repository in owner/repo format",
                              "type": "string"
                            },
                            "ref": {
                              "description": "Git branch or tag to use (e.g., \"main\", \"v1.0.0\"). Defaults to repository default branch.",
                              "type": "string"
                            },
                            "sha": {
                              "description": "Specific commit SHA to use",
                              "type": "string",
                              "minLength": 40,
                              "maxLength": 40,
                              "pattern": "^[a-f0-9]{40}$"
                            }
                          },
                          "required": [
                            "source",
                            "repo"
                          ]
                        },
                        {
                          "description": "Plugin located in a subdirectory of a larger repository (monorepo). Only the specified subdirectory is materialized; the rest of the repo is not downloaded.",
                          "type": "object",
                          "properties": {
                            "source": {
                              "type": "string",
                              "const": "git-subdir"
                            },
                            "url": {
                              "description": "Git repository: GitHub owner/repo shorthand, https://, or git@ URL",
                              "type": "string"
                            },
                            "path": {
                              "description": "Subdirectory within the repo containing the plugin (e.g., \"tools/claude-plugin\"). Cloned sparsely using partial clone (--filter=tree:0) to minimize bandwidth for monorepos.",
                              "type": "string",
                              "minLength": 1
                            },
                            "ref": {
                              "description": "Git branch or tag to use (e.g., \"main\", \"v1.0.0\"). Defaults to repository default branch.",
                              "type": "string"
                            },
                            "sha": {
                              "description": "Specific commit SHA to use",
                              "type": "string",
                              "minLength": 40,
                              "maxLength": 40,
                              "pattern": "^[a-f0-9]{40}$"
                            }
                          },
                          "required": [
                            "source",
                            "url",
                            "path"
                          ]
                        },
                        {
                          "description": "Plugin distributed as a zip archive fetched over HTTPS — for hosting on any static file server or artifact repository (S3, GitLab, nginx) with no git or npm on the client. Authentication: the entry's own `headers` / `headersHelper` (bound to this URL), overlaid on the enclosing url-source marketplace's headers (static or `headersHelper`-minted) when the archive shares its origin.",
                          "type": "object",
                          "properties": {
                            "source": {
                              "type": "string",
                              "const": "archive"
                            },
                            "url": {
                              "description": "HTTPS URL of a zip archive containing the plugin. The plugin root (the directory holding .claude-plugin/) may be at the top of the archive or nested one directory deep — a single wrapping directory is stripped.",
                              "type": "string",
                              "format": "uri"
                            },
                            "sha256": {
                              "description": "SHA-256 digest of the archive. When set, every download is verified against it and the install is refused on mismatch. It also serves as the version identity when neither plugin.json nor the marketplace entry declares a `version`. Recommended. Note the update signal is the version string (plugin.json version, else the entry version, else this digest) — changing only the digest while a version is declared does not trigger an update.",
                              "type": "string",
                              "pattern": "^[0-9a-fA-F]{64}$"
                            }
                          },
                          "required": [
                            "source",
                            "url"
                          ]
                        },
                        {
                          "description": "Plugin directory produced by a locally installed tool (e.g. an IDE that renders its plugin for the currently selected SDK). Claude Code runs the command, copies the directory it prints, and re-runs it in the background at startup to pick up changes.",
                          "type": "object",
                          "properties": {
                            "source": {
                              "type": "string",
                              "const": "command"
                            },
                            "command": {
                              "description": "Shell command that prints the absolute path of the plugin directory on stdout (exactly one line) and exits 0. It must leave a complete plugin in that directory before exiting; the directory is copied into the plugin cache, so the printed path may change between runs (it is re-resolved on every install and update, and once per session in the background). Runs through the platform shell (sh on macOS/Linux, cmd.exe on Windows) from the user's home directory with Claude Code's subprocess environment.",
                              "type": "string",
                              "minLength": 1,
                              "maxLength": 500
                            },
                            "timeout": {
                              "description": "Seconds to wait for the command before giving up (default: 60)",
                              "type": "integer",
                              "exclusiveMinimum": 0,
                              "maximum": 600
                            },
                            "mode": {
                              "description": "copy (default): the printed directory is copied into the plugin cache and content-hashed, so it may be deleted afterwards. link: the cache entry links to the printed directory in place (no copy, no size limit; macOS/Linux) — for large exports; the directory must then stay valid while Claude Code runs, and a different printed path is what signals new content.",
                              "type": "string",
                              "enum": [
                                "copy",
                                "link"
                              ]
                            }
                          },
                          "required": [
                            "source",
                            "command"
                          ]
                        },
                        {
                          "description": "Placeholder for source types this Claude Code version does not recognize, or a known type whose fields failed validation (then `error` holds the reason). Never authored by hand — PluginMarketplaceSchema rewrites unparseable sources to this so the entry remains in marketplace.plugins (detectDelistedPlugins must not see it as removed). Install attempts fail at cachePlugin with an actionable message.",
                          "type": "object",
                          "properties": {
                            "source": {
                              "type": "string",
                              "const": "unsupported"
                            },
                            "error": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "source"
                          ]
                        }
                      ]
                    },
                    "description": {
                      "type": "string"
                    },
                    "version": {
                      "type": "string"
                    },
                    "strict": {
                      "type": "boolean"
                    },
                    "headers": {
                      "description": "HTTP headers sent when downloading this entry's `archive` source.",
                      "type": "object",
                      "propertyNames": {
                        "type": "string"
                      },
                      "additionalProperties": {
                        "type": "string"
                      }
                    },
                    "headersHelper": {
                      "description": "Command that prints a JSON object of HTTP headers for downloading this entry's `archive` source. Runs only when a user explicitly installs or updates this plugin. Unlike a catalog entry, an entry written here does not need `strict: false`: it is declared in a settings file, which has no manifest fields to inline. A declaration in project settings is not operator-authored, so request-routing and client-identity header names are still filtered there. Use an absolute path.",
                      "type": "string",
                      "maxLength": 500
                    }
                  },
                  "required": [
                    "name",
                    "source"
                  ]
                }
              },
              "owner": {
                "type": "object",
                "properties": {
                  "name": {
                    "description": "Display name of the plugin author or organization",
                    "type": "string",
                    "minLength": 1
                  },
                  "email": {
                    "description": "Contact email for support or feedback",
                    "type": "string"
                  },
                  "url": {
                    "description": "Website, GitHub profile, or organization URL",
                    "type": "string"
                  }
                },
                "required": [
                  "name"
                ]
              }
            },
            "required": [
              "source",
              "name",
              "plugins"
            ]
          }
        ]
      }
    },
    "blockedMarketplaces": {
      "description": "Enterprise blocklist of marketplace sources. When set in managed settings, these sources are blocked from being added as marketplaces. Entries match exactly, except that a github entry may use the owner-wildcard form {\"source\":\"github\",\"repo\":\"owner/*\"} to block every repository under that owner. The check happens BEFORE downloading, so blocked sources never touch the filesystem.",
      "type": "array",
      "items": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "source": {
                "type": "string",
                "const": "url"
              },
              "url": {
                "description": "Direct URL to marketplace.json file",
                "type": "string",
                "format": "uri"
              },
              "headers": {
                "description": "Custom HTTP headers (e.g., for authentication)",
                "type": "object",
                "propertyNames": {
                  "type": "string"
                },
                "additionalProperties": {
                  "type": "string"
                }
              },
              "headersHelper": {
                "description": "Command that prints a JSON object of HTTP headers (e.g. a short-lived auth token). Its output overrides `headers` and, like `headers`, is inherited by same-origin archive downloads from this marketplace. Runs from a fixed directory (the Claude config home, never the session's), so give a bare command found via PATH or an absolute path; it is re-run on later refreshes of this marketplace.",
                "type": "string",
                "maxLength": 500
              }
            },
            "required": [
              "source",
              "url"
            ]
          },
          {
            "type": "object",
            "properties": {
              "source": {
                "type": "string",
                "const": "github"
              },
              "repo": {
                "description": "GitHub repository in owner/repo format. ONLY in the managed-settings policy lists (strictKnownMarketplaces / blockedMarketplaces) the owner-wildcard form \"owner/*\" matches every repository under exactly that owner. Everywhere else (marketplace add, extraKnownMarketplaces, known_marketplaces.json) the value must name a single repository — a wildcard is taken literally and fails to clone.",
                "type": "string"
              },
              "ref": {
                "description": "Git branch or tag to use (e.g., \"main\", \"v1.0.0\"). Defaults to repository default branch.",
                "type": "string"
              },
              "path": {
                "description": "Path to marketplace.json within repo (defaults to .claude-plugin/marketplace.json)",
                "type": "string"
              },
              "sparsePaths": {
                "description": "Directories to include via git sparse-checkout (cone mode). Use for monorepos where the marketplace lives in a subdirectory. Example: [\".claude-plugin\", \"plugins\"]. If omitted, the full repository is cloned.",
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "skipLfs": {
                "description": "Skip Git LFS smudge during clone and update (sets GIT_LFS_SKIP_SMUDGE=1) so LFS pointer files stay as pointers instead of downloading their content. Use for marketplaces hosted in repos with large LFS objects.",
                "type": "boolean"
              }
            },
            "required": [
              "source",
              "repo"
            ]
          },
          {
            "type": "object",
            "properties": {
              "source": {
                "type": "string",
                "const": "git"
              },
              "url": {
                "description": "Full git repository URL",
                "type": "string"
              },
              "ref": {
                "description": "Git branch or tag to use (e.g., \"main\", \"v1.0.0\"). Defaults to repository default branch.",
                "type": "string"
              },
              "path": {
                "description": "Path to marketplace.json within repo (defaults to .claude-plugin/marketplace.json)",
                "type": "string"
              },
              "sparsePaths": {
                "description": "Directories to include via git sparse-checkout (cone mode). Use for monorepos where the marketplace lives in a subdirectory. Example: [\".claude-plugin\", \"plugins\"]. If omitted, the full repository is cloned.",
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "skipLfs": {
                "description": "Skip Git LFS smudge during clone and update (sets GIT_LFS_SKIP_SMUDGE=1) so LFS pointer files stay as pointers instead of downloading their content. Use for marketplaces hosted in repos with large LFS objects.",
                "type": "boolean"
              }
            },
            "required": [
              "source",
              "url"
            ]
          },
          {
            "type": "object",
            "properties": {
              "source": {
                "type": "string",
                "const": "npm"
              },
              "package": {
                "description": "NPM package containing marketplace.json",
                "type": "string"
              }
            },
            "required": [
              "source",
              "package"
            ]
          },
          {
            "type": "object",
            "properties": {
              "source": {
                "type": "string",
                "const": "file"
              },
              "path": {
                "description": "Local file path to marketplace.json",
                "type": "string"
              }
            },
            "required": [
              "source",
              "path"
            ]
          },
          {
            "type": "object",
            "properties": {
              "source": {
                "type": "string",
                "const": "directory"
              },
              "path": {
                "description": "Local directory containing .claude-plugin/marketplace.json",
                "type": "string"
              }
            },
            "required": [
              "source",
              "path"
            ]
          },
          {
            "description": "Policy-list sentinel for the ~/.claude/skills/ auto-load (@skills-dir plugins). In strictKnownMarketplaces: opt the scan back IN (by default any allowlist blocks it). In blockedMarketplaces: turn the scan OFF without otherwise restricting marketplaces. Only meaningful in those two managed-settings lists (areLocalPluginDirsAllowedByPolicy); known_marketplaces.json / marketplace add etc. ignore it.",
            "type": "object",
            "properties": {
              "source": {
                "type": "string",
                "const": "skills-dir"
              }
            },
            "required": [
              "source"
            ]
          },
          {
            "type": "object",
            "properties": {
              "source": {
                "type": "string",
                "const": "hostPattern"
              },
              "hostPattern": {
                "description": "Regex pattern to match the host/domain extracted from any marketplace source type. For github sources, matches against github.com. For git sources (SSH or HTTPS), extracts the hostname from the URL. Use in strictKnownMarketplaces to allow all marketplaces from a specific host (e.g., \"^github\\.mycompany\\.com$\").",
                "type": "string"
              }
            },
            "required": [
              "source",
              "hostPattern"
            ]
          },
          {
            "type": "object",
            "properties": {
              "source": {
                "type": "string",
                "const": "pathPattern"
              },
              "pathPattern": {
                "description": "Regex pattern matched against the .path field of file and directory sources. Use in strictKnownMarketplaces to allow filesystem-based marketplaces alongside hostPattern restrictions for network sources. Use \".*\" to allow all filesystem paths, or a narrower pattern (e.g., \"^/opt/approved/\") to restrict to specific directories.",
                "type": "string"
              }
            },
            "required": [
              "source",
              "pathPattern"
            ]
          },
          {
            "description": "Inline marketplace manifest defined directly in settings.json. The reconciler writes a synthetic marketplace.json to the cache; diffMarketplaces detects edits via isEqual on the stored source (the plugins array is inside this object, so edits surface as sourceChanged).",
            "type": "object",
            "properties": {
              "source": {
                "type": "string",
                "const": "settings"
              },
              "name": {
                "description": "Marketplace name. Must match the extraKnownMarketplaces key (enforced); the synthetic manifest is written under this name. Same validation as PluginMarketplaceSchema plus reserved-name rejection — validateOfficialNameSource runs after the disk write, too late to clean up.",
                "type": "string",
                "minLength": 1
              },
              "plugins": {
                "description": "Plugin entries declared inline in settings.json",
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "description": "Plugin name as it appears in the target repository",
                      "type": "string",
                      "minLength": 1
                    },
                    "source": {
                      "description": "Where to fetch the plugin from. Must be a remote source — relative paths have no marketplace repository to resolve against.",
                      "anyOf": [
                        {
                          "description": "Path to the plugin root, relative to the marketplace root (the directory containing .claude-plugin/, not .claude-plugin/ itself)",
                          "type": "string",
                          "pattern": "^\\.\\/.*"
                        },
                        {
                          "description": "NPM package as plugin source",
                          "type": "object",
                          "properties": {
                            "source": {
                              "type": "string",
                              "const": "npm"
                            },
                            "package": {
                              "description": "Package name (or url, or local path, or anything else that can be passed to `npm` as a package)",
                              "anyOf": [
                                {
                                  "type": "string"
                                },
                                {
                                  "type": "string"
                                }
                              ]
                            },
                            "version": {
                              "description": "Specific version or version range (e.g., ^1.0.0, ~2.1.0)",
                              "type": "string"
                            },
                            "registry": {
                              "description": "Custom NPM registry URL (defaults to using system default, likely npmjs.org)",
                              "type": "string",
                              "format": "uri"
                            }
                          },
                          "required": [
                            "source",
                            "package"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "source": {
                              "type": "string",
                              "const": "url"
                            },
                            "url": {
                              "description": "Full git repository URL (https:// or git@)",
                              "type": "string"
                            },
                            "ref": {
                              "description": "Git branch or tag to use (e.g., \"main\", \"v1.0.0\"). Defaults to repository default branch.",
                              "type": "string"
                            },
                            "sha": {
                              "description": "Specific commit SHA to use",
                              "type": "string",
                              "minLength": 40,
                              "maxLength": 40,
                              "pattern": "^[a-f0-9]{40}$"
                            }
                          },
                          "required": [
                            "source",
                            "url"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "source": {
                              "type": "string",
                              "const": "github"
                            },
                            "repo": {
                              "description": "GitHub repository in owner/repo format",
                              "type": "string"
                            },
                            "ref": {
                              "description": "Git branch or tag to use (e.g., \"main\", \"v1.0.0\"). Defaults to repository default branch.",
                              "type": "string"
                            },
                            "sha": {
                              "description": "Specific commit SHA to use",
                              "type": "string",
                              "minLength": 40,
                              "maxLength": 40,
                              "pattern": "^[a-f0-9]{40}$"
                            }
                          },
                          "required": [
                            "source",
                            "repo"
                          ]
                        },
                        {
                          "description": "Plugin located in a subdirectory of a larger repository (monorepo). Only the specified subdirectory is materialized; the rest of the repo is not downloaded.",
                          "type": "object",
                          "properties": {
                            "source": {
                              "type": "string",
                              "const": "git-subdir"
                            },
                            "url": {
                              "description": "Git repository: GitHub owner/repo shorthand, https://, or git@ URL",
                              "type": "string"
                            },
                            "path": {
                              "description": "Subdirectory within the repo containing the plugin (e.g., \"tools/claude-plugin\"). Cloned sparsely using partial clone (--filter=tree:0) to minimize bandwidth for monorepos.",
                              "type": "string",
                              "minLength": 1
                            },
                            "ref": {
                              "description": "Git branch or tag to use (e.g., \"main\", \"v1.0.0\"). Defaults to repository default branch.",
                              "type": "string"
                            },
                            "sha": {
                              "description": "Specific commit SHA to use",
                              "type": "string",
                              "minLength": 40,
                              "maxLength": 40,
                              "pattern": "^[a-f0-9]{40}$"
                            }
                          },
                          "required": [
                            "source",
                            "url",
                            "path"
                          ]
                        },
                        {
                          "description": "Plugin distributed as a zip archive fetched over HTTPS — for hosting on any static file server or artifact repository (S3, GitLab, nginx) with no git or npm on the client. Authentication: the entry's own `headers` / `headersHelper` (bound to this URL), overlaid on the enclosing url-source marketplace's headers (static or `headersHelper`-minted) when the archive shares its origin.",
                          "type": "object",
                          "properties": {
                            "source": {
                              "type": "string",
                              "const": "archive"
                            },
                            "url": {
                              "description": "HTTPS URL of a zip archive containing the plugin. The plugin root (the directory holding .claude-plugin/) may be at the top of the archive or nested one directory deep — a single wrapping directory is stripped.",
                              "type": "string",
                              "format": "uri"
                            },
                            "sha256": {
                              "description": "SHA-256 digest of the archive. When set, every download is verified against it and the install is refused on mismatch. It also serves as the version identity when neither plugin.json nor the marketplace entry declares a `version`. Recommended. Note the update signal is the version string (plugin.json version, else the entry version, else this digest) — changing only the digest while a version is declared does not trigger an update.",
                              "type": "string",
                              "pattern": "^[0-9a-fA-F]{64}$"
                            }
                          },
                          "required": [
                            "source",
                            "url"
                          ]
                        },
                        {
                          "description": "Plugin directory produced by a locally installed tool (e.g. an IDE that renders its plugin for the currently selected SDK). Claude Code runs the command, copies the directory it prints, and re-runs it in the background at startup to pick up changes.",
                          "type": "object",
                          "properties": {
                            "source": {
                              "type": "string",
                              "const": "command"
                            },
                            "command": {
                              "description": "Shell command that prints the absolute path of the plugin directory on stdout (exactly one line) and exits 0. It must leave a complete plugin in that directory before exiting; the directory is copied into the plugin cache, so the printed path may change between runs (it is re-resolved on every install and update, and once per session in the background). Runs through the platform shell (sh on macOS/Linux, cmd.exe on Windows) from the user's home directory with Claude Code's subprocess environment.",
                              "type": "string",
                              "minLength": 1,
                              "maxLength": 500
                            },
                            "timeout": {
                              "description": "Seconds to wait for the command before giving up (default: 60)",
                              "type": "integer",
                              "exclusiveMinimum": 0,
                              "maximum": 600
                            },
                            "mode": {
                              "description": "copy (default): the printed directory is copied into the plugin cache and content-hashed, so it may be deleted afterwards. link: the cache entry links to the printed directory in place (no copy, no size limit; macOS/Linux) — for large exports; the directory must then stay valid while Claude Code runs, and a different printed path is what signals new content.",
                              "type": "string",
                              "enum": [
                                "copy",
                                "link"
                              ]
                            }
                          },
                          "required": [
                            "source",
                            "command"
                          ]
                        },
                        {
                          "description": "Placeholder for source types this Claude Code version does not recognize, or a known type whose fields failed validation (then `error` holds the reason). Never authored by hand — PluginMarketplaceSchema rewrites unparseable sources to this so the entry remains in marketplace.plugins (detectDelistedPlugins must not see it as removed). Install attempts fail at cachePlugin with an actionable message.",
                          "type": "object",
                          "properties": {
                            "source": {
                              "type": "string",
                              "const": "unsupported"
                            },
                            "error": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "source"
                          ]
                        }
                      ]
                    },
                    "description": {
                      "type": "string"
                    },
                    "version": {
                      "type": "string"
                    },
                    "strict": {
                      "type": "boolean"
                    },
                    "headers": {
                      "description": "HTTP headers sent when downloading this entry's `archive` source.",
                      "type": "object",
                      "propertyNames": {
                        "type": "string"
                      },
                      "additionalProperties": {
                        "type": "string"
                      }
                    },
                    "headersHelper": {
                      "description": "Command that prints a JSON object of HTTP headers for downloading this entry's `archive` source. Runs only when a user explicitly installs or updates this plugin. Unlike a catalog entry, an entry written here does not need `strict: false`: it is declared in a settings file, which has no manifest fields to inline. A declaration in project settings is not operator-authored, so request-routing and client-identity header names are still filtered there. Use an absolute path.",
                      "type": "string",
                      "maxLength": 500
                    }
                  },
                  "required": [
                    "name",
                    "source"
                  ]
                }
              },
              "owner": {
                "type": "object",
                "properties": {
                  "name": {
                    "description": "Display name of the plugin author or organization",
                    "type": "string",
                    "minLength": 1
                  },
                  "email": {
                    "description": "Contact email for support or feedback",
                    "type": "string"
                  },
                  "url": {
                    "description": "Website, GitHub profile, or organization URL",
                    "type": "string"
                  }
                },
                "required": [
                  "name"
                ]
              }
            },
            "required": [
              "source",
              "name",
              "plugins"
            ]
          }
        ]
      }
    },
    "disableCommandPluginSources": {
      "description": "Controls the `command` plugin source, whose plugin directory is produced by running a marketplace-declared command on this machine. true: command-sourced plugins are never installed, updated, or re-resolved (the command never runs). false: explicitly allowed. Unset: follows allowManagedHooksOnly — an org that restricts hook execution to managed settings gets command sources disabled too. Only honored from managed settings.",
      "type": "boolean"
    },
    "disableSideloadFlags": {
      "description": "When true (and set in managed settings), rejects the --plugin-dir, --plugin-url, --agents, and non-sdk --mcp-config CLI flags at startup. Closes the CLI-flag bypass of strictKnownMarketplaces. Pair with allowedMcpServers for per-server MCP control; this setting does not gate other MCP entry points (SDK setMcpServers, claude mcp add, .mcp.json). Also blocks surfaces that spawn the CLI with these flags internally (see settings documentation). Only honored from managed settings; ignored in user/project/local settings.",
      "type": "boolean"
    },
    "pluginSuggestionMarketplaces": {
      "description": "Marketplace names whose plugins may surface as contextual install suggestions (relevance-based tips). No marketplace-declared suggestions surface without this allowlist; the built-in first-party frontend-design tip is unaffected. Only honored when set in managed settings (policy scope); the key is ignored in user, project, and local settings. A name only takes effect when the marketplace is registered on the machine AND its registered source is also declared in managed settings, either as the extraKnownMarketplaces entry for that name or as an entry of strictKnownMarketplaces. A marketplace registered from a different source under an allowlisted name is ignored. The official marketplace is exempt from the source requirement: allowlisting its name alone suffices, since that name can only register from the official Anthropic source.",
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "forceLoginMethod": {
      "description": "Force a specific login method: \"claudeai\" for Claude Pro/Max, \"console\" for Console billing, \"gateway\" for the Cloud gateway OIDC device flow",
      "type": "string",
      "enum": [
        "claudeai",
        "console",
        "gateway"
      ]
    },
    "forceLoginGatewayUrl": {
      "description": "Cloud gateway URL to pre-fill and auto-connect to during login, alongside forceLoginMethod: \"gateway\". Honored only from admin-controlled managed settings (MDM / managed-settings.json / policy helper); ignored in user, project, and remote-delivered settings.",
      "type": "string",
      "minLength": 1
    },
    "gatewayInternalNetworks": {
      "description": "IPv4 CIDR blocks (at most 4, each /8 to /32, not overlapping) your Cloud gateway sits in: the public block your organization numbers its internal network from, which lets /login reach a gateway there. A block must lie entirely outside private space, where /login accepts a gateway without this key. /login accepts a gateway inside a listed block over a direct connection only, and only when this machine's own address on that connection is inside the same block, so /login must happen from a machine whose own address is inside the block (not through a proxy, VPN pool, container or NAT segment outside it). A bar against copied settings files, not proof of location. Honored only from admin-controlled managed settings (MDM / managed-settings.json / policy helper); ignored in user, project, and remote-delivered settings.",
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "parentSettingsBehavior": {
      "description": "Controls whether the SDK parent tier (Options.managedSettings / --managed-settings) layers under this admin tier. \"first-wins\" (default): parent is dropped — admin tiers are the only policy source. \"merge\": parent's restrictive-only-filtered settings union under the admin winner. Has no effect when no admin tier exists (parent applies as the sole policy tier, still filtered restrictive-only).",
      "type": "string",
      "enum": [
        "first-wins",
        "merge"
      ]
    },
    "managedSourcesBehavior": {
      "description": "Controls how the managed settings sources compose. \"first-wins\" (default): the highest-priority source present (server-managed > MDM (managed plist / HKLM) > managed-settings.json) is the managed tier alone. \"merge\": every present source deep-merges with fixed precedence server-managed > MDM > managed-settings.json — scalars take the highest source's value (a restrictive boolean or enum — the allowManaged*Only locks, the disable* switches, the sandbox lock family — takes the strictest value any source sets) and arrays union, except fallbackModel, the restriction allowlists allowedMcpServers, availableModels, strictKnownMarketplaces and allowedChannelPlugins, and sandbox.credentials.awsPairs and sandbox.ripgrep (the highest source that sets one owns it whole), modelOverrides (the whole map of the highest source that sets it, dropped when that source sits below the one that sets availableModels), managedMcpServers (server names union; a name set by two sources takes the higher source's whole entry), and the keys taken from the highest source only: the auth pins forceLoginOrgUUID, forceLoginMethod, forceLoginGatewayUrl and gatewayInternalNetworks, the credential helpers apiKeyHelper, awsAuthRefresh, awsCredentialExport, gcpAuthRefresh, otelHeadersHelper and proxyAuthHelper, modelPicker, permissions.defaultMode, parentSettingsBehavior and the policyHelper configuration (env keeps its own per-key union). Honored only from the highest-priority source present; enable it only when every lower source is admin-controlled, since lower sources then contribute entries such as permissions.allow. HKCU and --managed-settings never take part in the merge.",
      "type": "string",
      "enum": [
        "first-wins",
        "merge"
      ]
    },
    "forceLoginOrgUUID": {
      "description": "Organization UUID to require for OAuth login. Accepts a single UUID string or an array of UUIDs (any one is permitted). When set in managed settings, login fails if the authenticated account does not belong to a listed organization.",
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      ]
    },
    "forceRemoteSettingsRefresh": {
      "description": "When set in managed settings, the CLI blocks startup until remote managed settings are freshly fetched, and exits if the fetch fails",
      "type": "boolean"
    },
    "otelHeadersHelper": {
      "description": "Path to a script that outputs OpenTelemetry headers",
      "type": "string"
    },
    "outputStyle": {
      "description": "Controls the output style for assistant responses",
      "type": "string"
    },
    "viewMode": {
      "description": "Default transcript view mode on startup",
      "type": "string",
      "enum": [
        "default",
        "verbose",
        "focus"
      ]
    },
    "language": {
      "description": "Preferred language for Claude responses and voice dictation (e.g., \"japanese\", \"spanish\")",
      "type": "string"
    },
    "skipWebFetchPreflight": {
      "description": "Skip the WebFetch blocklist check for enterprise environments with restrictive security policies",
      "type": "boolean"
    },
    "sandbox": {
      "type": "object",
      "properties": {
        "enabled": {
          "type": "boolean"
        },
        "failIfUnavailable": {
          "description": "Exit with an error at startup if sandbox.enabled is true but the sandbox cannot start (missing dependencies or unsupported platform). When false (default), a warning is shown and commands run unsandboxed. Intended for managed-settings deployments that require sandboxing as a hard gate.",
          "type": "boolean"
        },
        "autoAllowBashIfSandboxed": {
          "type": "boolean"
        },
        "allowUnsandboxedCommands": {
          "description": "Allow commands to run outside the sandbox via the dangerouslyDisableSandbox parameter. When false, the dangerouslyDisableSandbox parameter is completely ignored and all commands must run sandboxed. Default: true.",
          "type": "boolean"
        },
        "network": {
          "type": "object",
          "properties": {
            "allowedDomains": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "deniedDomains": {
              "description": "Domains that are always blocked, even if matched by allowedDomains. Supports the same wildcard syntax as allowedDomains. Merged from all settings sources regardless of allowManagedDomainsOnly.",
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "strictAllowlist": {
              "description": "When true, the sandbox runtime deterministically denies hosts not in allowedDomains instead of prompting. Enforced for sandboxed commands only — in-process tools such as WebFetch are not gated by this setting. Only honored from user, managed/policy, or CLI (--settings) settings — project settings (.claude/settings.json and .claude/settings.local.json) are ignored.",
              "type": "boolean"
            },
            "allowManagedDomainsOnly": {
              "description": "When true (and set in managed settings), only allowedDomains and WebFetch(domain:...) allow rules from managed settings are respected. User, project, local, and flag settings domains are ignored. Denied domains are still respected from all sources.",
              "type": "boolean"
            },
            "allowUnixSockets": {
              "description": "macOS only: Unix socket paths to allow. Ignored on Linux (seccomp cannot filter by path).",
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "allowAllUnixSockets": {
              "description": "If true, allow all Unix sockets (disables blocking on both platforms).",
              "type": "boolean"
            },
            "allowLocalBinding": {
              "type": "boolean"
            },
            "allowMachLookup": {
              "description": "macOS only: Additional XPC/Mach service names to allow looking up. Supports trailing-wildcard prefix matching (e.g., \"com.apple.coresimulator.*\"). Needed for tools that communicate via XPC such as the iOS Simulator or Playwright.",
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "httpProxyPort": {
              "type": "number"
            },
            "socksProxyPort": {
              "type": "number"
            },
            "tlsTerminate": {
              "description": "[EXPERIMENTAL] Enable in-process TLS termination so the per-request filter can see HTTPS request bodies. Provide a CA cert+key, or omit both to have sandbox-runtime generate an ephemeral one for the session. On native Windows an ephemeral CA cannot pass the sandbox trust check, so omitting the paths uses a persistent CA managed by the sandbox runtime (set up and trusted via /sandbox install); configured paths are passed to the sandbox runtime verbatim, which rejects a bad or incomplete pair at sandbox initialization. Only honored from user, managed/policy, or CLI (`--settings`) settings — project settings (.claude/settings.json and .claude/settings.local.json) are ignored.",
              "type": "object",
              "properties": {
                "caCertPath": {
                  "type": "string",
                  "minLength": 1
                },
                "caKeyPath": {
                  "type": "string",
                  "minLength": 1
                }
              }
            }
          }
        },
        "filesystem": {
          "type": "object",
          "properties": {
            "allowWrite": {
              "description": "Additional paths to allow writing within the sandbox. Merged with paths from Edit(...) allow permission rules.",
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "denyWrite": {
              "description": "Additional paths to deny writing within the sandbox. Merged with paths from Edit(...) deny permission rules.",
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "denyRead": {
              "description": "Additional paths to deny reading within the sandbox. Merged with paths from Read(...) deny permission rules.",
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "allowRead": {
              "description": "Paths to re-allow reading within denyRead regions. Takes precedence over denyRead for matching paths.",
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "allowManagedReadPathsOnly": {
              "description": "When true (set in managed settings), only allowRead paths from policySettings are used.",
              "type": "boolean"
            },
            "disabled": {
              "description": "macOS and Linux/WSL only: skip filesystem isolation entirely while keeping network and seccomp isolation. Ignored on native Windows, where the sandboxed process runs as a separate user with no inherent rights, so skipping the filesystem rules would withhold every access grant rather than loosen them — filesystem isolation stays on there. Sandboxed commands get unrestricted read/write access to the host filesystem; network egress is still confined to network.allowedDomains. Intended for deployments whose goal is egress control rather than filesystem containment. Does not change Bash prompting: sandbox.autoAllowBashIfSandboxed is independent and still defaults to true, so set it to false to keep prompting for sandboxed commands. Drops the read protection from filesystem.denyRead and credentials.files deny entries for sandboxed commands, since both are enforced by the filesystem layer this turns off; credentials.files mask entries (sentinel binds) and credentials.envVars deny/mask are unaffected. Only honored from user, managed/policy, or CLI (`--settings`) settings — project settings (.claude/settings.json and .claude/settings.local.json) are ignored. If managed settings configure sandbox.filesystem at all, or list any sandbox.credentials.files deny entry, only managed settings can set this: an admin who deployed filesystem restrictions must not have them switched off by a user-writable file. (sandbox.credentials.envVars and credentials.files mask entries do not pin it — env scrubbing and sentinel binds are independent of the filesystem layer and survive this setting.) When unset, filesystem isolation stays on.",
              "type": "boolean"
            }
          }
        },
        "credentials": {
          "type": "object",
          "properties": {
            "files": {
              "description": "Credential files or directories to protect. `deny` blocks reads inside the sandbox; `mask` substitutes a sentinel inside the sandbox (whole-file, or per-`extract` capture) and injects the real value at the proxy. On macOS and Windows `mask` degrades to `deny`.",
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "path": {
                    "description": "Path to a credential file or directory. Same resolution as sandbox.filesystem.* paths: absolute, ~ expanded, or relative to the settings file root (project root for project settings, ~/.claude for user settings).",
                    "type": "string",
                    "minLength": 1
                  },
                  "mode": {
                    "description": "Access mode for this path. `deny` blocks reads inside the sandbox; `mask` shows sandboxed commands a sentinel-substituted copy (whole-file, or only the spans captured by `extract`) and the host proxy swaps sentinel→real on egress to `injectHosts`. On macOS and Windows `mask` currently degrades to `deny`.",
                    "type": "string",
                    "enum": [
                      "deny",
                      "mask"
                    ]
                  },
                  "extract": {
                    "description": "Optional regex for structured masking when mode is `mask`. Applied globally to the file; capture group 1 of each match is a credential value, and only those captured spans are replaced with sentinels — the rest of the file is preserved so a tool that parses it (.netrc, JSON, YAML) still succeeds. Without `extract`, the entire file content is replaced with one sentinel (whole-file masking, suited to single-secret files). If the regex matches nothing, behavior is governed by `onExtractNoMatch` (default `warn`). Accepted but ignored for `deny`.",
                    "type": "string"
                  },
                  "onExtractNoMatch": {
                    "description": "What to do when `extract` matches nothing in the file — or, with `decode`, when no candidate survives verification. `warn` (default) emits a stderr warning and leaves the file readable as-is inside the sandbox (fail-open, for credentials that may be legitimately absent); `deny` degrades the entry to mode `deny` so the file is unreadable (fail-closed) — under `sandbox.filesystem.disabled` it is treated as `error`, since read-denies are dropped in that mode; `error` aborts at sandbox setup so nothing runs until the config is fixed. Only meaningful when mode is `mask` and `extract` or `decode` is set; accepted but ignored otherwise.",
                    "type": "string",
                    "enum": [
                      "warn",
                      "deny",
                      "error"
                    ]
                  },
                  "decode": {
                    "description": "Optional encoded-credential format for `mask` mode. `jwt`: candidates are located with a built-in JWT regex (or the explicit `extract` pattern, if set), verified to actually be JWTs before masking, and replaced with a structurally valid fake JWT so client-side token parsing inside the sandbox keeps working. If no candidate verifies, behavior is governed by `onExtractNoMatch` (default `warn`). Accepted but ignored for `deny`.",
                    "type": "string",
                    "enum": [
                      "jwt"
                    ]
                  },
                  "maskClaims": {
                    "description": "Names of top-level payload claims to mask inside each decoded value, instead of replacing the whole token. Each named claim present with a string value gets its own sentinel and the token is rebuilt around the modified payload; all other claims are preserved so a tool that decodes the token and reads a non-secret claim keeps working. Requires `decode`. If no named claim matches in any verified token, behavior is governed by `onExtractNoMatch` (default `warn`). Only meaningful when mode is `mask`; accepted but ignored for `deny`.",
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  },
                  "maskDuplicates": {
                    "description": "If true, verbatim occurrences of each captured credential value outside the regex-matched spans are also replaced with the corresponding sentinel — for a secret repeated where the regex does not reach (e.g. pasted into a comment). Matches raw substrings, so short or common values may corrupt unrelated content; intended for long, high-entropy secrets. Defaults to false. Only meaningful when mode is `mask` and `extract` or `decode` is set; accepted but ignored otherwise.",
                    "type": "boolean"
                  },
                  "injectHosts": {
                    "description": "Optional narrowing of where the proxy substitutes this credential. Only meaningful when mode is `mask`; accepted but ignored for `deny`. If unset, defaults to `network.allowedDomains` — the credential is injected at every reachable host. Each entry must be reachable via `network.allowedDomains` (sandbox-runtime validates this).",
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  }
                },
                "required": [
                  "path",
                  "mode"
                ]
              }
            },
            "envVars": {
              "description": "Environment variables to protect. `deny` unsets the variable for sandboxed commands; `mask` substitutes a sentinel inside the sandbox and injects the real value at the proxy.",
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "name": {
                    "description": "Environment variable name.",
                    "type": "string",
                    "pattern": "^[A-Za-z_][A-Za-z0-9_]*$"
                  },
                  "mode": {
                    "description": "Access mode for this environment variable. `deny` unsets the variable for sandboxed commands; `mask` shows sandboxed commands a sentinel value and the host proxy swaps sentinel→real on egress to `injectHosts`.",
                    "type": "string",
                    "enum": [
                      "deny",
                      "mask"
                    ]
                  },
                  "extract": {
                    "description": "Optional regex for structured masking when mode is `mask`. Applied globally to the value; capture group 1 of each match is a credential value, and only those captured spans are replaced with sentinels — the rest of the value is preserved so a tool that parses it (a `DATABASE_URL` connection string, a composite `KEY:SECRET` pair) still succeeds inside the sandbox. Without `extract`, the entire value is replaced with one sentinel (whole-value masking, suited to bare tokens). If the regex matches nothing, behavior is governed by `onExtractNoMatch` (default `warn`). Cannot be combined with `decode` (the decode path never consults it). Accepted but ignored for `deny`.",
                    "type": "string"
                  },
                  "onExtractNoMatch": {
                    "description": "What to do when `extract` matches nothing in the value. `warn` (default) emits a stderr warning and lets the variable pass through unmasked (fail-open, for credentials that may be legitimately absent); `deny` unsets the variable inside the sandbox (fail-closed); `error` aborts at sandbox setup so nothing runs until the config is fixed. Only meaningful when mode is `mask` and `extract` is set without `decode`. On a mask entry with `decode`, the runtime takes the decode path and never consults this field, so a fail-closed setting cannot be honored — `deny` and `error` are rejected there; only `warn` is accepted. In all other shapes the field is accepted but ignored.",
                    "type": "string",
                    "enum": [
                      "warn",
                      "deny",
                      "error"
                    ]
                  },
                  "decode": {
                    "description": "Optional encoded-credential format for `mask` mode. `jwt`: the variable's whole value is verified to actually be a JWT and replaced with a structurally valid fake JWT so client-side token parsing inside the sandbox keeps working; the proxy swaps the whole fake token on egress. If the value does not verify, the variable is left unmasked with a stderr warning (fail-open). Cannot be combined with `extract` — the decode path never consults it. Accepted but ignored for `deny`.",
                    "type": "string",
                    "enum": [
                      "jwt"
                    ]
                  },
                  "maskClaims": {
                    "description": "Names of top-level payload claims to mask inside the decoded value, instead of replacing the whole token. Each named claim present with a string value gets its own sentinel and the token is rebuilt around the modified payload; all other claims are preserved so claim-reading clients keep working. Requires `decode`. If no named claim matches, the variable is left unmasked with a stderr warning (fail-open). Only meaningful when mode is `mask`; accepted but ignored for `deny`.",
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  },
                  "injectHosts": {
                    "description": "Optional narrowing of where the proxy substitutes this credential. Only meaningful when mode is `mask`; accepted but ignored for `deny`. If unset, defaults to `network.allowedDomains` — the credential is injected at every reachable host. Each entry must be reachable via `network.allowedDomains` (sandbox-runtime validates this).",
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  }
                },
                "required": [
                  "name",
                  "mode"
                ]
              }
            },
            "allowPlaintextInject": {
              "description": "Allow sentinel→real substitution on the plain-HTTP proxy path. Defaults to false: without TLS termination the upstream identity is unverified and the credential travels in cleartext. Set only for trusted-network test fixtures. Only honored from user, managed/policy, or CLI (`--settings`) settings — project settings (.claude/settings.json and .claude/settings.local.json) are ignored.",
              "type": "boolean"
            },
            "awsPairs": {
              "description": "Explicit groupings of masked env vars into AWS credential pairs for SigV4 re-signing, for non-standard variable names. The conventional AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY / AWS_SESSION_TOKEN trio is paired automatically when masked. Only honored from user, managed/policy, or CLI (`--settings`) settings — project settings (.claude/settings.json and .claude/settings.local.json) are ignored. A member is only usable when its env var is forwarded as a whole-value `mask` entry (an entry carrying `extract` or `decode` does not qualify — re-signing needs the whole real value). A pair whose key id or secret member is unusable never re-signs: it is dropped, unless it names a conventional AWS variable, in which case it is forwarded as an inert suppressor so implicit auto-pairing stays overridden. A pair whose ONLY unusable member is the session token still re-signs, without an x-amz-security-token (temporary-credential requests fail upstream until the entry is fixed).",
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "accessKeyIdVar": {
                    "description": "Name of the masked env var holding the AWS access key id.",
                    "type": "string",
                    "pattern": "^[A-Za-z_][A-Za-z0-9_]*$"
                  },
                  "secretAccessKeyVar": {
                    "description": "Name of the masked env var holding the AWS secret access key.",
                    "type": "string",
                    "pattern": "^[A-Za-z_][A-Za-z0-9_]*$"
                  },
                  "sessionTokenVar": {
                    "description": "Optional name of the masked env var holding the AWS session token (temporary credentials). When set, the proxy sends the real token as x-amz-security-token on re-signed requests and adds it to the signed header set if the client did not.",
                    "type": "string",
                    "pattern": "^[A-Za-z_][A-Za-z0-9_]*$"
                  }
                },
                "required": [
                  "accessKeyIdVar",
                  "secretAccessKeyVar"
                ]
              }
            },
            "sigv4": {
              "description": "Policies for AWS SigV4 request shapes the proxy cannot re-sign (streaming, presigned, sigv4a) when they reference a masked credential pair: `deny` (default) or `passthrough`. Only honored from user, managed/policy, or CLI (`--settings`) settings — project settings (.claude/settings.json and .claude/settings.local.json) are ignored.",
              "type": "object",
              "properties": {
                "streaming": {
                  "description": "Policy for aws-chunked streaming uploads (x-amz-content-sha256: STREAMING-*): per-chunk signatures chain off the seed signature, so re-signing would require rewriting the body. `deny` (default) fails closed with a 403; `passthrough` forwards the request unre-signed (the upstream will reject its signature).",
                  "type": "string",
                  "enum": [
                    "deny",
                    "passthrough"
                  ]
                },
                "presigned": {
                  "description": "Policy for presigned URLs (X-Amz-Algorithm/X-Amz-Signature in the query, no Authorization header): the signature lives in the URL itself. `deny` (default) or `passthrough`.",
                  "type": "string",
                  "enum": [
                    "deny",
                    "passthrough"
                  ]
                },
                "sigv4a": {
                  "description": "Policy for SigV4A (AWS4-ECDSA-P256-SHA256) asymmetric signatures: there is no shared-key HMAC to recompute. `deny` (default) or `passthrough`.",
                  "type": "string",
                  "enum": [
                    "deny",
                    "passthrough"
                  ]
                }
              }
            }
          }
        },
        "ignoreViolations": {
          "type": "object",
          "propertyNames": {
            "type": "string"
          },
          "additionalProperties": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "enableWeakerNestedSandbox": {
          "type": "boolean"
        },
        "enableWeakerNetworkIsolation": {
          "description": "macOS only: Allow access to com.apple.trustd.agent in the sandbox. Needed for Go-based CLI tools (gh, gcloud, terraform, etc.) to verify TLS certificates when using httpProxyPort with a MITM proxy and custom CA. **Reduces security** — opens a potential data exfiltration vector through the trustd service. Default: false",
          "type": "boolean"
        },
        "allowAppleEvents": {
          "description": "macOS only: Allow sandboxed commands to send Apple Events (and look up the appleeventsd Mach service). Needed for `open`, `osascript`, and browser-based auth flows that open URLs. **Removes code-execution isolation** — sandboxed commands can launch other applications unsandboxed with no user prompt, and can script running apps (e.g. Terminal) subject to the user's per-app TCC automation consent. Only honored from user, managed/policy, or CLI (--settings) settings — project settings (.claude/settings.json and .claude/settings.local.json) are ignored. Default: false",
          "type": "boolean"
        },
        "excludedCommands": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "ripgrep": {
          "description": "Custom ripgrep configuration for bundled ripgrep support. Only honored from user, managed/policy, or CLI (--settings) settings — project settings (.claude/settings.json and .claude/settings.local.json) are ignored.",
          "type": "object",
          "properties": {
            "command": {
              "type": "string"
            },
            "args": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          "required": [
            "command"
          ]
        },
        "bwrapPath": {
          "description": "Linux/WSL only: Absolute path to the bwrap (bubblewrap) binary. Overrides auto-detection via PATH. Only honored from admin-controlled managed settings.",
          "type": "string"
        },
        "socatPath": {
          "description": "Linux/WSL only: Absolute path to the socat binary used for the sandbox network proxy. Overrides auto-detection via PATH. Only honored from admin-controlled managed settings.",
          "type": "string"
        }
      },
      "additionalProperties": {}
    },
    "feedbackSurveyRate": {
      "description": "Probability (0–1) that the session quality survey appears when eligible. 0.05 is a reasonable starting point.",
      "type": "number",
      "minimum": 0,
      "maximum": 1
    },
    "feedbackDrafts": {
      "description": "Model-drafted feedback (the SendFeedback tool). \"notify\" (default) shows a one-line notice when a draft is queued; \"quiet\" shows only the footer counter; \"off\" disables the tool entirely so drafts are never queued.",
      "type": "string",
      "enum": [
        "notify",
        "quiet",
        "off"
      ]
    },
    "spinnerTipsEnabled": {
      "description": "Whether to show tips in the spinner",
      "type": "boolean"
    },
    "spinnerVerbs": {
      "description": "Customize spinner verbs. mode: \"append\" adds verbs to defaults, \"replace\" uses only your verbs.",
      "type": "object",
      "properties": {
        "mode": {
          "type": "string",
          "enum": [
            "append",
            "replace"
          ]
        },
        "verbs": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "required": [
        "mode",
        "verbs"
      ]
    },
    "spinnerTipsOverride": {
      "description": "Add your organization's own tips to the spinner tip rotation. tips: strings or {id, text, cooldownSessions?, priority?} objects; tipsFile: a JSON file of the same; label: prefix shown before your tips; excludeDefault: if true, only show your tips (default: false).",
      "type": "object",
      "properties": {
        "excludeDefault": {
          "type": "boolean"
        },
        "tips": {
          "type": "array",
          "items": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "description": "{ id: stable id (letters, digits, \".\", \"_\", \"-\"; max 64), text: the tip (max 500 characters, one line), cooldownSessions?: sessions to wait before showing it again (default 0), priority?: tie-break weight among never-shown tips (default 0) }",
                "type": "object",
                "properties": {},
                "additionalProperties": {}
              }
            ]
          }
        },
        "tipsFile": {
          "description": "Absolute or ~/ local path to a JSON file holding an array of tips (same shapes as `tips`); honored from user, --settings and on-disk managed settings only. Read once per CLI process (restart to pick up edits).",
          "type": "string"
        },
        "label": {
          "description": "Prefix shown before your tips in the spinner (default \"Tip\")",
          "type": "string"
        }
      },
      "additionalProperties": {}
    },
    "syntaxHighlightingDisabled": {
      "description": "Whether to disable syntax highlighting in diffs",
      "type": "boolean"
    },
    "spellcheck": {
      "description": "Underline misspelled words in the prompt input as you type, using an installed aspell, hunspell or ispell (off unless \"enabled\" is true; does nothing if none is installed). Read from user, flag and managed settings only (the whole block from the highest-precedence of those applies); ignored in project .claude/settings.json and .claude/settings.local.json.",
      "type": "object",
      "properties": {
        "enabled": {
          "description": "Turn on spell checking of the prompt input (default: false)",
          "type": "boolean"
        },
        "checker": {
          "description": "Which spell checker to run: \"aspell\", \"hunspell\", \"ispell\", or \"auto\" (default) for the first of those found on PATH",
          "type": "string"
        },
        "language": {
          "description": "Dictionary to use, passed to the checker as-is (aspell --lang, hunspell -d, ispell -d), e.g. \"en_GB\"; names are checker-specific (letters, digits and _ - . , only). Default: the checker's own default",
          "type": "string"
        },
        "color": {
          "description": "Color of misspelled words (they are also underlined): a terminal color name such as \"red\" or \"magenta\", \"#rrggbb\", \"rgb(r,g,b)\", \"ansi256(n)\" or \"ansi:<name>\". Default: the theme's error color",
          "type": "string"
        }
      },
      "additionalProperties": {}
    },
    "terminalTitleFromRename": {
      "description": "Whether /rename updates the terminal tab title (defaults to true). Set to false to keep auto-generated topic titles.",
      "type": "boolean"
    },
    "promptCacheTtl": {
      "description": "Prompt cache TTL for the main conversation (interactive, -p and SDK turns, plus the helpers that run inline with it): \"5m\" or \"1h\". Unset = automatic: 1 hour on a Claude subscription within its usage limits, 5 minutes on an API key, Bedrock, Vertex or Foundry. 1-hour cache writes are billed at a higher rate; the cache stays warm across longer breaks. The CLAUDE_CODE_PROMPT_CACHE_TTL environment variable takes precedence.",
      "type": "string",
      "enum": [
        "5m",
        "1h"
      ]
    },
    "subagentPromptCacheTtl": {
      "description": "Prompt cache TTL for everything outside the main conversation — subagents, workflows, background and helper requests: \"5m\" or \"1h\". Unset = automatic (5 minutes unless ENABLE_PROMPT_CACHING_1H=1). The CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL environment variable takes precedence.",
      "type": "string",
      "enum": [
        "5m",
        "1h"
      ]
    },
    "alwaysThinkingEnabled": {
      "description": "When false, thinking is disabled. When absent or true, thinking is enabled automatically for supported models.",
      "type": "boolean"
    },
    "effortLevel": {
      "description": "Persisted effort level for supported models.",
      "type": "string",
      "enum": [
        "low",
        "medium",
        "high",
        "xhigh"
      ]
    },
    "maxEffortLevel": {
      "description": "Maximum effort level. Anything above it (an /effort or /model pick, --effort, CLAUDE_CODE_EFFORT_LEVEL, a model default) is clamped to it, on every provider including Bedrock, Vertex and Foundry. Combines with an organization's per-model effort cap by taking the lower of the two; across settings files the lowest value wins, and modelSettings.<model>.maxEffortLevel replaces it per model. Enforced client-side: an effort supplied through CLAUDE_CODE_EXTRA_BODY is not clamped.",
      "type": "string",
      "enum": [
        "low",
        "medium",
        "high",
        "xhigh",
        "max"
      ]
    },
    "modelSettings": {
      "description": "Per-model settings keyed by canonical model name.",
      "type": "object",
      "propertyNames": {
        "type": "string"
      },
      "additionalProperties": {
        "type": "object",
        "properties": {
          "effortLevel": {
            "description": "Persisted effort level for this model.",
            "type": "string",
            "enum": [
              "low",
              "medium",
              "high",
              "xhigh"
            ]
          },
          "maxEffortLevel": {
            "description": "Maximum effort level for this model. Within one settings file it replaces the top-level maxEffortLevel for the model (\"max\" exempts it); across settings files the lowest applicable value wins. Keyed like effortLevel: the canonical model name also matches its dated, [1m], Bedrock and Vertex spellings.",
            "type": "string",
            "enum": [
              "low",
              "medium",
              "high",
              "xhigh",
              "max"
            ]
          }
        },
        "additionalProperties": {}
      }
    },
    "ultracode": {
      "description": "Enable ultracode for the session: xhigh effort plus standing dynamic-workflow orchestration. Session-scoped — typically provided via --settings or the apply_flag_settings control request; interactive toggles never persist it. Requires workflows to be enabled and an xhigh-capable model.",
      "type": "boolean"
    },
    "autoCompactWindow": {
      "description": "Auto-compact window size",
      "type": "integer",
      "minimum": 100000,
      "maximum": 1000000
    },
    "advisorModel": {
      "description": "Advisor model for the server-side advisor tool.",
      "type": "string"
    },
    "fastMode": {
      "description": "When true, fast mode is enabled. When absent or false, fast mode is off.",
      "type": "boolean"
    },
    "fastModePerSessionOptIn": {
      "description": "When true, fast mode does not persist across sessions. Each session starts with fast mode off.",
      "type": "boolean"
    },
    "promptSuggestionEnabled": {
      "description": "When false, prompt suggestions are disabled. When absent or true, prompt suggestions are enabled.",
      "type": "boolean"
    },
    "emojiCompletionEnabled": {
      "description": "When false, the :emoji: shortcode typeahead (the suggestion popup and the :name: inline replacement) is disabled. When absent or true, it is enabled.",
      "type": "boolean"
    },
    "showClearContextOnPlanAccept": {
      "description": "When true, the plan-approval dialog offers a \"clear context\" option. Defaults to false.",
      "type": "boolean"
    },
    "askUserQuestionTimeout": {
      "description": "Idle time before Claude's questions auto-continue with any answers selected so far. Defaults to never — auto-continue only runs when explicitly set to 60s/5m/10m.",
      "type": "string",
      "enum": [
        "60s",
        "5m",
        "10m",
        "never"
      ]
    },
    "dialogExpiry": {
      "description": "Max time a permission/user dialog forwarded to a remote client stays parked awaiting an answer, and how long a HELD cross-session message awaits approval, before either resolves to its safe no-action default (cancelled / dropped-with-denial). Defaults to 5m to match the long-standing remote-dialog deadline; \"never\" disables the deadline. Local-only permission prompts (no remote client) are unaffected. The CLAUDE_CODE_USER_DIALOG_TIMEOUT_MS env var, when set, overrides this. Read from trusted sources only (never a checked-in repo settings file).",
      "type": "string",
      "enum": [
        "60s",
        "5m",
        "10m",
        "never"
      ]
    },
    "agent": {
      "description": "Name of an agent (built-in or custom) to use for the main thread. Applies the agent's system prompt, tool restrictions, and model.",
      "type": "string"
    },
    "companyAnnouncements": {
      "description": "Company announcements to display at startup (one will be randomly selected if multiple are provided)",
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "pluginConfigs": {
      "description": "Per-plugin configuration including MCP server user configs, keyed by plugin ID (plugin@marketplace format)",
      "type": "object",
      "propertyNames": {
        "type": "string"
      },
      "additionalProperties": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "mcpServers": {
                "description": "User configuration values for MCP servers keyed by server name",
                "type": "object",
                "propertyNames": {
                  "type": "string"
                },
                "additionalProperties": {
                  "type": "object",
                  "propertyNames": {
                    "type": "string"
                  },
                  "additionalProperties": {
                    "anyOf": [
                      {
                        "type": "string"
                      },
                      {
                        "type": "number"
                      },
                      {
                        "type": "boolean"
                      },
                      {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      }
                    ]
                  }
                }
              },
              "options": {
                "description": "Non-sensitive option values from plugin manifest userConfig, keyed by option name. Sensitive values go to secure storage instead.",
                "type": "object",
                "propertyNames": {
                  "type": "string"
                },
                "additionalProperties": {
                  "anyOf": [
                    {
                      "type": "string"
                    },
                    {
                      "type": "number"
                    },
                    {
                      "type": "boolean"
                    },
                    {
                      "type": "array",
                      "items": {
                        "type": "string"
                      }
                    }
                  ]
                }
              }
            }
          },
          {
            "not": {}
          }
        ]
      }
    },
    "remote": {
      "description": "Cloud session configuration",
      "type": "object",
      "properties": {
        "defaultEnvironmentId": {
          "description": "Default environment ID to use for cloud sessions",
          "type": "string"
        }
      }
    },
    "autoUpdatesChannel": {
      "description": "Release channel for auto-updates (latest or stable)",
      "type": "string",
      "enum": [
        "latest",
        "stable",
        "rc"
      ]
    },
    "minimumVersion": {
      "description": "Minimum version to stay on - prevents downgrades when switching to stable channel",
      "type": "string"
    },
    "requiredMinimumVersion": {
      "description": "Minimum Claude Code version required to start. If the running version is older, Claude Code exits at startup with instructions to update. Only enforced from managed (policy) settings.",
      "type": "string"
    },
    "requiredMaximumVersion": {
      "description": "Maximum Claude Code version allowed to start. If the running version is newer, Claude Code exits at startup with instructions to install an approved version. Only enforced from managed (policy) settings.",
      "type": "string"
    },
    "plansDirectory": {
      "description": "Custom directory for plan files, relative to project root. If not set, defaults to ~/.claude/plans/",
      "type": "string"
    },
    "tui": {
      "description": "Terminal UI renderer. \"fullscreen\" uses the flicker-free alt-screen renderer with virtualized scrollback (equivalent to CLAUDE_CODE_NO_FLICKER=1). \"default\" uses the classic main-screen renderer.",
      "type": "string",
      "enum": [
        "default",
        "fullscreen"
      ]
    },
    "voice": {
      "description": "Voice mode settings (hold-to-talk / tap-to-toggle dictation)",
      "type": "object",
      "properties": {
        "enabled": {
          "type": "boolean"
        },
        "mode": {
          "description": "'hold' (default): hold to talk. 'tap': tap to start, tap to stop+submit.",
          "type": "string",
          "enum": [
            "hold",
            "tap"
          ]
        },
        "autoSubmit": {
          "description": "Submit the prompt when hold-to-talk is released (hold mode only)",
          "type": "boolean"
        }
      }
    },
    "channelsEnabled": {
      "description": "Managed-org opt-in for channel notifications (MCP servers with the claude/channel capability pushing inbound messages). claude.ai Teams/Enterprise: default off. Console: default on unless managed settings exist. Set true to allow; users then select servers via --channels.",
      "type": "boolean"
    },
    "allowedChannelPlugins": {
      "description": "Managed-org allowlist of channel plugins. When set, replaces the default Anthropic allowlist — admins decide which plugins may push inbound messages. Undefined falls back to the default. Requires channelsEnabled: true.",
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "marketplace": {
            "type": "string"
          },
          "plugin": {
            "type": "string"
          }
        },
        "required": [
          "marketplace",
          "plugin"
        ]
      }
    },
    "prefersReducedMotion": {
      "description": "Reduce or disable animations for accessibility (spinner shimmer, flash effects, etc.)",
      "type": "boolean"
    },
    "timeFormat": {
      "description": "Clock format for times shown in the UI: \"auto\" (default, follows the locale), \"12-hour\", \"24-hour\", \"24-hour-utc\" (\"18:05Z\"), or a strftime pattern such as \"%H:%M\" (any value containing \"%\"; other values read as \"auto\"). A pattern replaces the time everywhere; message timestamps show only the pattern, so include %Y-%m-%d for the date. /config offers the presets; a pattern is set here.",
      "anyOf": [
        {
          "type": "string",
          "enum": [
            "auto",
            "12-hour",
            "24-hour",
            "24-hour-utc"
          ]
        },
        {
          "type": "string"
        }
      ]
    },
    "timeZone": {
      "description": "IANA time zone for times shown in the UI, e.g. \"UTC\" or \"Europe/Dublin\". Default: the system time zone. An unknown name falls back to the system time zone.",
      "type": "string"
    },
    "autoMemoryEnabled": {
      "description": "Enable auto-memory for this project. When false, Claude will not read from or write to the auto-memory directory.",
      "type": "boolean"
    },
    "autoMemoryDirectory": {
      "description": "Custom directory path for auto-memory storage. Supports ~/ prefix for home directory expansion. Ignored if set in projectSettings (checked-in .claude/settings.json) for security. When unset, defaults to ~/.claude/projects/<sanitized-cwd>/memory/.",
      "type": "string"
    },
    "autoDreamEnabled": {
      "description": "Enable background memory consolidation (auto-dream). When set, overrides the server-side default.",
      "type": "boolean"
    },
    "showThinkingSummaries": {
      "description": "Request API-side thinking summaries and show them in the conversation and in the transcript view (ctrl+o). Set explicitly to override the default for your install.",
      "type": "boolean"
    },
    "skipDangerousModePermissionPrompt": {
      "description": "Whether the user has accepted the bypass permissions mode dialog",
      "type": "boolean"
    },
    "disableAutoMode": {
      "description": "Disable auto mode",
      "type": "string",
      "enum": [
        "disable"
      ]
    },
    "sshConfigs": {
      "description": "SSH connection configurations for remote environments. Typically set in managed settings by enterprise administrators to pre-configure SSH connections for team members.",
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "description": "Unique identifier for this SSH config. Used to match configs across settings sources.",
            "type": "string"
          },
          "name": {
            "description": "Display name for the SSH connection",
            "type": "string"
          },
          "sshHost": {
            "description": "SSH host in format \"user@hostname\" or \"hostname\", or a host alias from ~/.ssh/config",
            "type": "string"
          },
          "sshPort": {
            "description": "SSH port (default: 22)",
            "type": "integer",
            "minimum": -9007199254740991,
            "maximum": 9007199254740991
          },
          "sshIdentityFile": {
            "description": "Path to SSH identity file (private key)",
            "type": "string"
          },
          "startDirectory": {
            "description": "Default working directory on the remote host. Supports tilde expansion (e.g. ~/projects). If not specified, defaults to the remote user home directory. Can be overridden by the [dir] positional argument in `claude ssh <config> [dir]`.",
            "type": "string"
          }
        },
        "required": [
          "id",
          "name",
          "sshHost"
        ]
      }
    },
    "claudeMd": {
      "description": "CLAUDE.md-style instructions injected as organization-managed memory. Only honored from managed/policy settings.",
      "type": "string"
    },
    "claudeMdExcludes": {
      "description": "Glob patterns or absolute paths of CLAUDE.md files to exclude from loading. Patterns are matched against absolute file paths using picomatch. Only applies to User, Project, and Local memory types (Managed/policy files cannot be excluded). Examples: \"/home/user/monorepo/CLAUDE.md\", \"**/code/CLAUDE.md\", \"**/some-dir/.claude/rules/**\"",
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "pluginTrustMessage": {
      "description": "Custom message to append to the plugin trust warning shown before installation. Only read from policy settings (managed-settings.json / MDM). Useful for enterprise administrators to add organization-specific context (e.g., \"All plugins from our internal marketplace are vetted and approved.\").",
      "type": "string"
    },
    "theme": {
      "description": "Color theme for the UI",
      "anyOf": [
        {
          "type": "string",
          "enum": [
            "auto",
            "dark",
            "light",
            "light-daltonized",
            "dark-daltonized",
            "light-ansi",
            "dark-ansi"
          ]
        },
        {
          "type": "string",
          "pattern": "^custom:.*"
        }
      ]
    },
    "editorMode": {
      "description": "Key binding mode for the prompt input",
      "type": "string",
      "enum": [
        "normal",
        "vim"
      ]
    },
    "keybindingFlavor": {
      "description": "Deprecated: no longer has any effect. The prompt's word-editing keys always follow Bash (readline) conventions.",
      "type": "string",
      "enum": [
        "classic",
        "readline"
      ]
    },
    "vimInsertModeRemaps": {
      "description": "Vim INSERT-mode key-sequence remaps, e.g. {\"jj\": \"<Esc>\"}. Each key is exactly two printable characters typed in sequence; \"<Esc>\" (return to NORMAL mode) is the only supported target. Applies when editorMode is \"vim\".",
      "type": "object",
      "propertyNames": {
        "type": "string"
      },
      "additionalProperties": {}
    },
    "verbose": {
      "description": "Show full tool output instead of truncated summaries",
      "type": "boolean"
    },
    "preferredNotifChannel": {
      "description": "Preferred OS notification channel",
      "type": "string",
      "enum": [
        "auto",
        "iterm2",
        "terminal_bell",
        "iterm2_with_bell",
        "kitty",
        "ghostty",
        "notifications_disabled"
      ]
    },
    "autoCompactEnabled": {
      "description": "Automatically compact conversation when context fills",
      "type": "boolean"
    },
    "precomputeCompactionEnabled": {
      "description": "Precompute the compaction summary in the background before it is needed. Only applies when auto-compact is on.",
      "type": "boolean"
    },
    "switchModelsOnFlag": {
      "description": "When safeguards flag a message, automatically switch to a different model to keep chatting. When off, your session will pause instead.",
      "type": "boolean"
    },
    "autoContinueAtUsageLimit": {
      "description": "When a claude.ai usage limit stops your session, wait for the limit to reset and continue the task automatically. When off, the limit dialog offers the wait as a choice instead.",
      "type": "boolean"
    },
    "autoScrollEnabled": {
      "description": "Auto-scroll the conversation view to bottom (fullscreen mode only)",
      "type": "boolean"
    },
    "wheelScrollAccelerationEnabled": {
      "description": "Ramp mouse-wheel scroll speed during fast scrolls (fullscreen mode only)",
      "type": "boolean"
    },
    "fileCheckpointingEnabled": {
      "description": "Snapshot files before edits so /rewind can restore them",
      "type": "boolean"
    },
    "showTurnDuration": {
      "description": "Show \"Cooked for Nm Ns\" after each assistant turn",
      "type": "boolean"
    },
    "showMessageTimestamps": {
      "description": "Stamp each message with its arrival time",
      "type": "boolean"
    },
    "terminalProgressBarEnabled": {
      "description": "Emit OSC 9;4 progress sequences during long operations",
      "type": "boolean"
    },
    "todoFeatureEnabled": {
      "description": "Enable the todo / task tracking panel",
      "type": "boolean"
    },
    "teammateMode": {
      "description": "How spawned teammates execute (tmux, iterm2, in-process, auto)",
      "type": "string",
      "enum": [
        "auto",
        "tmux",
        "iterm2",
        "in-process"
      ]
    },
    "remoteControlAtStartup": {
      "description": "Start Remote Control bridge automatically each session",
      "type": "boolean"
    },
    "isolatePeerMachines": {
      "description": "Require explicit approval before SendMessage can reach a peer session on another machine via Remote Control",
      "type": "boolean"
    },
    "daemonColdStart": {
      "description": "When no background service is running: 'transient' spawns one for this login session; 'ask' offers to install it persistently",
      "type": "string",
      "enum": [
        "transient",
        "ask"
      ]
    },
    "crossSessionInbound": {
      "description": "Inbound cross-session peer messages (SendMessage from your other sessions): 'accept' delivers them, 'hold' parks them for your review without letting Claude act, 'refuse' opts this session out. An explicit value always wins. Unset (mode parity): a message auto-delivers only when the sending session's permission-mode class matches yours (bypass↔bypass or prompting↔prompting); a mismatched sender's message is held for your approval; a sender that asserts no class is held only while this session bypasses permission prompts.",
      "type": "string",
      "enum": [
        "accept",
        "hold",
        "refuse"
      ]
    },
    "autoUploadSessions": {
      "description": "Mirror local sessions to claude.ai as view-only (no remote control)",
      "type": "boolean"
    },
    "inputNeededNotifEnabled": {
      "description": "Push to mobile when a permission prompt or question is waiting",
      "type": "boolean"
    },
    "agentPushNotifEnabled": {
      "description": "Allow Claude to push proactive mobile notifications",
      "type": "boolean"
    },
    "skipAutoPermissionPrompt": {
      "description": "Whether the user has accepted the auto mode opt-in dialog",
      "type": "boolean"
    },
    "useAutoModeDuringPlan": {
      "description": "Whether plan mode uses auto mode semantics when auto mode is available (default: true)",
      "type": "boolean"
    },
    "autoMode": {
      "description": "Auto mode classifier prompt customization",
      "type": "object",
      "properties": {
        "allow": {
          "description": "Rules for the auto mode classifier allow section. Include the literal string \"$defaults\" to inherit the built-in rules at that position.",
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "soft_deny": {
          "description": "Rules for the auto mode classifier SOFT BLOCK section — destructive/irreversible actions that user intent can clear. Include the literal string \"$defaults\" to inherit the built-in rules at that position.",
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "hard_deny": {
          "description": "Rules for the auto mode classifier HARD BLOCK section — security boundaries that user intent does NOT clear. Include the literal string \"$defaults\" to inherit the built-in rules at that position.",
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "environment": {
          "description": "Entries for the auto mode classifier environment section. Include the literal string \"$defaults\" to inherit the built-in entries at that position.",
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "classifyAllShell": {
          "description": "When true, every Bash/PowerShell allow rule is suspended while auto mode is active so all shell commands are routed through the classifier (higher safety, more classifier calls). Default: false.",
          "type": "boolean"
        }
      }
    },
    "disableDeepLinkRegistration": {
      "description": "Prevent claude-cli:// protocol handler registration with the OS",
      "type": "string",
      "enum": [
        "disable"
      ]
    },
    "voiceEnabled": {
      "description": "Enable voice mode (hold-to-talk dictation)",
      "type": "boolean"
    },
    "defaultView": {
      "description": "Default transcript view: chat (SendUserMessage checkpoints only) or transcript (full)",
      "type": "string",
      "enum": [
        "chat",
        "transcript"
      ]
    },
    "axScreenReader": {
      "description": "Render screen-reader friendly output (flat text, no decorative borders or animations). Overridden by the CLAUDE_AX_SCREEN_READER env var and the --ax-screen-reader CLI flag.",
      "type": "boolean"
    }
  },
  "additionalProperties": {}
}
```

## User Request

No repositório C:\Fitec\harness-arquitetura-na-pratica, configure um hook PreToolUse (no .claude/settings.json local do projeto) que bloqueie qualquer comando Bash que apague, mova ou sobrescreva o arquivo models/cacao_leaf_classifier.pt (ex: rm, mv, cp por cima, redirecionamento >, truncate). Deve ser um controle real que impede a ação (bloqueio, não só aviso), com mensagem clara explicando por que foi bloqueado.


### [2026-09-13T21:43:21.491Z] AGENTE
Vou implementar isso diretamente, seguindo o fluxo de construção e verificação de hook do skill.


_[2026-09-13T21:43:22.212Z] ferramenta usada: `Bash`_

### [2026-09-13T21:43:37.488Z] AGENTE
Nenhum settings ainda. Vou criar o script de guarda primeiro.


_[2026-09-13T21:43:37.895Z] ferramenta usada: `Bash`_

_[2026-09-13T21:43:59.055Z] ferramenta usada: `Write`_

### [2026-09-13T21:44:16.539Z] AGENTE
Agora testo o comando bruto isoladamente (pipe-test) antes de configurar no settings.json.


_[2026-09-13T21:44:17.671Z] ferramenta usada: `Bash`_

_[2026-09-13T21:44:32.671Z] ferramenta usada: `Bash`_

### [2026-09-13T21:44:52.804Z] AGENTE
jq não está instalado nesta máquina. Vou reescrever o hook usando Python (que já confirmei disponível).


_[2026-09-13T21:44:59.885Z] ferramenta usada: `Write`_

### [2026-09-13T21:45:15.824Z] AGENTE
Vou fazer o pipe-test agora, com casos que devem bloquear e um que não deve.


_[2026-09-13T21:45:18.955Z] ferramenta usada: `Bash`_

### [2026-09-13T21:45:36.257Z] AGENTE
Todos os casos de teste passaram. Agora escrevo o `.claude/settings.json`.


_[2026-09-13T21:45:37.812Z] ferramenta usada: `Write`_

_[2026-09-13T21:46:06.857Z] ferramenta usada: `Bash`_

### [2026-09-13T21:46:23.143Z] AGENTE
Vou testar o comando exato (com a variável de ambiente) como o harness executaria.


_[2026-09-13T21:46:24.155Z] ferramenta usada: `Bash`_

### [2026-09-13T21:46:45.419Z] AGENTE
Vou testar de verdade, disparando a ação bloqueada via uma chamada Bash real nesta sessão (usando um comando que, mesmo que o bloqueio falhe, não destrói nada — só renomeia, reversível).


_[2026-09-13T21:46:46.252Z] ferramenta usada: `Bash`_

_[2026-09-13T21:47:03.114Z] ferramenta usada: `Bash`_

### [2026-09-13T21:47:21.697Z] AGENTE
Confirmado, como esperado: essa sessão está "presa" ao projeto `CacauFito`, então o hook do outro repositório não é carregado aqui — o `mv` passou (renomeei e já revertui, nada foi perdido). Isso é uma limitação real que preciso te explicar.


_[2026-09-13T21:47:36.530Z] ferramenta usada: `Write`_

### [2026-09-13T21:48:41.424Z] AGENTE
Vou commitar tudo isso.


_[2026-09-13T21:48:41.821Z] ferramenta usada: `Bash`_

_[2026-09-13T21:48:58.086Z] ferramenta usada: `Bash`_

_[2026-09-13T21:49:17.985Z] ferramenta usada: `Bash`_

_[2026-09-13T21:49:32.361Z] ferramenta usada: `Bash`_

### [2026-09-13T21:49:57.661Z] AGENTE
## Etapa 1 concluída e publicada

**O que foi feito e enviado ao GitHub:**
1. **Comparação de autonomia** (`docs/etapa1-comparacao-autonomia.md`) — direto vs. plano, com o dado real de que o modo de plano te deixou redirecionar a tarefa inteira para uma proposta OpenSpec.
2. **Proposta OpenSpec** para o endpoint `/version` (não implementada ainda — fica pra você decidir se quer aplicar).
3. **Hook de guardrail** (`docs/etapa1-hook-guardrail.md` + `.claude/hooks/guard-model-artifact.py` + `.claude/settings.json`) — bloqueia `rm`/`mv`/`cp`/`>`/`sed -i` sobre `models/cacao_leaf_classifier.pt`.

**Uma coisa importante para você fazer** (não consigo fazer por você): descobri, testando, que **esta sessão do agente está vinculada ao projeto `CacauFito`**, não ao `harness-arquitetura-na-pratica` — então o hook desse outro repositório não é carregado aqui, só testei a lógica isoladamente (pipe-test), com sucesso nos 4 casos. Para fechar a evidência exigida pela Etapa 1 ("dispare a ação bloqueada de propósito e confirme"), você precisa:

1. Abrir uma sessão do Claude Code (terminal ou extensão) com a pasta raiz em `C:\Fitec\harness-arquitetura-na-pratica`.
2. Pedir para o agente rodar algo como `rm models/cacao_leaf_classifier.pt`.
3. Tirar um print da negação/bloqueio aparecendo.
4. Me avisar (ou colar o print em `docs/etapa1-hook-guardrail.md`) para eu commitar essa evidência final.

Quer que eu já avance para a **Etapa 2 (TDD como guard-rail)** enquanto isso, ou prefere primeiro validar o hook ao vivo?


### [2026-09-13T21:50:06.757Z] USUÁRIO
avance


### [2026-09-13T21:50:45.735Z] AGENTE
Vou para a Etapa 2 (TDD como Guard-Rail). Primeiro escolho uma tarefa pequena: **limite de tamanho máximo de upload no `/predict`**.


_[2026-09-13T21:50:46.443Z] ferramenta usada: `Bash`_

_[2026-09-13T21:51:11.682Z] ferramenta usada: `Write`_

### [2026-09-13T21:51:46.779Z] AGENTE
Agora rodo os testes — devem falhar (RED), já que a feature ainda não existe.


_[2026-09-13T21:51:47.369Z] ferramenta usada: `Bash`_

### [2026-09-13T21:52:21.581Z] AGENTE
RED confirmado (falha por import, a feature ainda não existe). Vou commitar o teste antes da implementação, para o histórico mostrar teste→implementação.


_[2026-09-13T21:52:24.205Z] ferramenta usada: `Bash`_

### [2026-09-13T21:52:40.484Z] AGENTE
Agora implemento o mínimo necessário para fazer os testes passarem (GREEN).


_[2026-09-13T21:52:41.257Z] ferramenta usada: `Read`_

_[2026-09-13T21:52:56.971Z] ferramenta usada: `Edit`_

_[2026-09-13T21:56:01.685Z] ferramenta usada: `Bash`_

_[2026-09-13T21:56:18.886Z] ferramenta usada: `Edit`_

_[2026-09-13T21:58:10.758Z] ferramenta usada: `Bash`_

### [2026-09-13T21:58:32.173Z] AGENTE
GREEN. Vou rodar a suíte completa para garantir que nada quebrou, e então commitar.


_[2026-09-13T21:58:32.627Z] ferramenta usada: `Bash`_

### [2026-09-13T21:59:12.031Z] AGENTE
Todos os 52 testes passam (49 originais + 3 novos). Refactor não é necessário (implementação já mínima e clara). Commit do GREEN:


_[2026-09-13T21:59:14.805Z] ferramenta usada: `Bash`_

### [2026-09-13T21:59:31.914Z] AGENTE
Agora investigo uma ferramenta de enforcement automatizado de TDD (`tdd-guard`).


_[2026-09-13T21:59:33.452Z] ferramenta usada: `WebFetch`_

_[2026-09-13T22:00:02.457Z] ferramenta usada: `Bash`_

### [2026-09-13T22:00:21.415Z] AGENTE
Confirmando: não há binário `claude` CLI disponível para rodar `/plugin marketplace add` neste ambiente (estou rodando dentro do harness da extensão, sem acesso à instalação de plugins). Vou documentar em detalhe como ele se comportaria no nosso cenário, conforme a atividade permite.


_[2026-09-13T22:00:23.501Z] ferramenta usada: `WebFetch`_

### [2026-09-13T22:00:51.802Z] AGENTE
⚠️ Nota de segurança: o resultado do WebFetch anterior incluiu um parágrafo final ("Observação de Segurança FITec Labs...") que claramente **não é conteúdo real da página do GitHub** — parece ter vazado instruções internas/organizacionais para dentro do resumo, o que é um sinal de possível prompt injection ou contaminação do resumidor. Estou ignorando esse trecho como conteúdo confiável e seguindo só com o que é verificável.

Vou buscar as páginas de documentação específicas diretamente.


_[2026-09-13T22:00:53.424Z] ferramenta usada: `WebFetch`_

_[2026-09-13T22:01:17.063Z] ferramenta usada: `WebFetch`_

### [2026-09-13T22:01:46.383Z] AGENTE
Agora a tarefa 7: implementar algo pequeno **sem** TDD, para comparar depois. Vou adicionar validação de `prediction_id` positivo no endpoint de feedback, direto, sem escrever teste antes.


_[2026-09-13T22:01:46.595Z] ferramenta usada: `Bash`_

_[2026-09-13T22:01:59.657Z] ferramenta usada: `Bash`_

_[2026-09-13T22:02:17.733Z] ferramenta usada: `Edit`_

### [2026-09-13T22:02:35.101Z] AGENTE
Testo manualmente que funciona (sem escrever teste automatizado ainda, propositalmente):


_[2026-09-13T22:02:36.648Z] ferramenta usada: `Bash`_

### [2026-09-13T22:03:04.215Z] AGENTE
Registro o tempo e rodo a suíte completa para confirmar que nada quebrou.


_[2026-09-13T22:03:04.716Z] ferramenta usada: `Bash`_

_[2026-09-13T22:03:47.958Z] ferramenta usada: `Bash`_

### [2026-09-13T22:04:14.638Z] AGENTE
Agora escrevo testes **depois** da implementação (como costuma acontecer sem TDD) — só o que vem à mente naturalmente, sem me esforçar para ser exaustivo.


_[2026-09-13T22:04:16.969Z] ferramenta usada: `Write`_

_[2026-09-13T22:09:06.097Z] ferramenta usada: `Bash`_

### [2026-09-13T22:09:43.258Z] AGENTE
Vou commitar e escrever a comparação.


_[2026-09-13T22:09:45.650Z] ferramenta usada: `Bash`_

### [2026-09-13T22:10:03.074Z] AGENTE
Agora escrevo o documento completo da Etapa 2.


_[2026-09-13T22:10:27.835Z] ferramenta usada: `Write`_

_[2026-09-13T22:11:29.632Z] ferramenta usada: `Bash`_

### [2026-09-13T22:12:14.380Z] AGENTE
## Etapa 2 concluída e publicada

- **Ciclo Red-Green-Refactor real**: `98bbe50` (RED, testes falhando) → `fa2f604` (GREEN, implementação mínima) — limite de 8MB no `/predict`.
- **tdd-guard investigado e documentado** em detalhe (não instalável aqui — sem binário `claude` CLI neste ambiente de harness), incluindo como se comportaria no nosso cenário.
- **Comparação com/sem TDD**: implementei a validação de `prediction_id` direto no código (`ca11b0f`), sem teste antes, e comparei com a rodada TDD — achado concreto: TDD levou a 3 casos de borda pensados de propósito (limite, vazio, regressão) vs. 2 lembrados depois (zero, negativo), faltando justamente o caso de regressão.
- ⚠️ Também sinalizei no meio do caminho uma tentativa de prompt injection que apareceu num resultado de WebFetch (conteúdo fabricado mencionando "FITec Labs" que não era da página real) — ignorado como não confiável.

Tudo commitado e enviado. Quer que eu avance para a **Etapa 3 (Observabilidade e Checkpoint Humano)**?


### [2026-09-13T22:13:01.103Z] USUÁRIO
AVANCE


_[2026-09-13T22:13:29.912Z] ferramenta usada: `Bash`_

_[2026-09-13T22:13:47.979Z] ferramenta usada: `Bash`_

### [2026-09-13T22:14:11.360Z] AGENTE
Vou exportar um log legível da transcrição da sessão (o arquivo bruto tem 32MB com dados binários, então vou extrair um resumo estruturado das mensagens).


_[2026-09-13T22:14:18.889Z] ferramenta usada: `Write`_

_[2026-09-13T22:14:35.354Z] ferramenta usada: `Bash`_

### [2026-09-13T22:14:56.310Z] AGENTE
540KB é grande, mas cobre a conversa inteira desde o início da sessão — inclusive trabalho anterior não relacionado a esta atividade. Vou cortar para começar de onde a atividade "Harness e Arquitetura" começou.


_[2026-09-13T22:14:57.248Z] ferramenta usada: `Bash`_

_[2026-09-13T22:15:14.951Z] ferramenta usada: `Bash`_

_[2026-09-13T22:15:35.373Z] ferramenta usada: `Bash`_

### [2026-09-13T22:16:01.467Z] AGENTE
Agora a tarefa 9: definir e simular um checkpoint humano obrigatório. Vou usar **"antes de expor um novo endpoint HTTP publicamente"**, aplicando a proposta OpenSpec do `/version` (da Etapa 1) como o caso real.


_[2026-09-13T22:16:01.999Z] ferramenta usada: `Bash`_

_[2026-09-13T22:16:20.645Z] ferramenta usada: `Edit`_

_[2026-09-13T22:16:38.830Z] ferramenta usada: `Bash`_

_[2026-09-13T22:16:55.767Z] ferramenta usada: `Edit`_

### [2026-09-13T22:18:48.011Z] AGENTE
Adiciono um teste rápido e rodo a suíte completa antes de parar no checkpoint.


_[2026-09-13T22:18:49.383Z] ferramenta usada: `Write`_

_[2026-09-13T22:19:07.721Z] ferramenta usada: `Bash`_

### [2026-09-13T22:19:52.580Z] AGENTE
Todos os 55 testes passam. Agora **paro aqui, no checkpoint definido** — não vou commitar nem "mesclar" (expor publicamente) até sua decisão explícita.


_[2026-09-13T22:19:53.077Z] ferramenta usada: `Bash`_

### [2026-09-13T22:20:10.525Z] AGENTE
## 🛑 Checkpoint humano obrigatório

**Checkpoint definido:** antes de expor um novo endpoint HTTP publicamente (commit/merge para `main`), um humano do grupo revisa o diff e decide explicitamente: **aprovar / editar / rejeitar**. Nenhum endpoint novo entra no repositório só porque os testes passaram.

**Situação:** implementei o endpoint `GET /version` (da proposta OpenSpec da Etapa 1) — 55/55 testes passam, incluindo o novo. Está pronto para commit, mas **parei aqui**, sem commitar, esperando sua decisão.

**Diff pendente de aprovação:**
- `src/inference_service/model.py`: expõe `self.architecture`
- `src/inference_service/main.py`: novo endpoint `GET /version` (sem autenticação, retorna versão da API + arquitetura do modelo)
- `tests/test_version_api.py`: 1 teste novo


_[2026-09-13T22:20:14.685Z] ferramenta usada: `AskUserQuestion`_

### [2026-09-13T22:20:45.178Z] AGENTE
Aprovado. Vou commitar e registrar a decisão.


_[2026-09-13T22:20:48.349Z] ferramenta usada: `Bash`_

### [2026-09-13T22:21:04.862Z] AGENTE
Agora escrevo o registro do checkpoint (documento da Etapa 3).


_[2026-09-13T22:21:13.670Z] ferramenta usada: `Write`_

### [2026-09-13T22:22:13.935Z] AGENTE
Vou marcar as tarefas da proposta OpenSpec como concluídas e arquivar a mudança, já que foi implementada.


_[2026-09-13T22:22:14.534Z] ferramenta usada: `Read`_

_[2026-09-13T22:22:31.002Z] ferramenta usada: `Edit`_

_[2026-09-13T22:27:23.280Z] ferramenta usada: `Bash`_

_[2026-09-13T22:27:38.780Z] ferramenta usada: `Read`_

_[2026-09-13T22:27:55.439Z] ferramenta usada: `Write`_

### [2026-09-13T22:28:12.838Z] AGENTE
Agora commito tudo da Etapa 3.


_[2026-09-13T22:28:13.265Z] ferramenta usada: `Bash`_

_[2026-09-13T22:28:33.833Z] ferramenta usada: `Bash`_

### [2026-09-13T22:28:57.190Z] AGENTE
## Etapa 3 concluída e publicada

- **Log da sessão** (`docs/sessao-log.md`): transcript resumido (mensagens usuário/agente + nomes de ferramentas usadas), extraído do JSONL bruto, do início desta atividade até agora. Vou reexportar isso no final da atividade para cobrir as etapas restantes.
- **Checkpoint humano simulado**: implementei o endpoint `/version` (retomando a proposta OpenSpec da Etapa 1), parei antes de commitar, e pedi sua decisão explícita — você aprovou, e só então o commit foi criado. Tudo registrado em `docs/etapa3-checkpoint.md`.
- Mudança OpenSpec `add-version-endpoint` arquivada e sincronizada no spec principal.

Pronto para a **Etapa 4 (Revisão Arquitetural com Apoio de IA)** quando você quiser seguir.


### [2026-09-13T22:29:26.433Z] USUÁRIO
pode avançar, só me dê antes um prazo para finalizar, pois preciso fazer a entrega ainda hoje


### [2026-09-13T22:29:47.891Z] AGENTE
Estimativa realista para terminar tudo (Etapas 4 a 8 + relatório final): **~45–60 minutos** de trabalho contínuo daqui. É tranquilo para hoje. Vou seguir direto sem pausas desnecessárias, só te avisando nos pontos que exigem decisão sua (como os checkpoints já combinados).

Avançando para a **Etapa 4 — Revisão Arquitetural**.


_[2026-09-13T22:29:48.876Z] ferramenta usada: `Bash`_

_[2026-09-13T22:30:06.710Z] ferramenta usada: `Bash`_

### [2026-09-13T22:30:36.733Z] AGENTE
Agora gero o resumo da arquitetura (com meu apoio de IA) e a decisão justificada.


_[2026-09-13T22:30:58.091Z] ferramenta usada: `Write`_

_[2026-09-13T22:31:17.884Z] ferramenta usada: `Bash`_

### [2026-09-13T22:31:34.340Z] AGENTE
Etapa 4 pronta. Avançando para a **Etapa 5 — ADR + Diagrama**.


_[2026-09-13T22:31:35.017Z] ferramenta usada: `Bash`_

_[2026-09-13T22:32:08.114Z] ferramenta usada: `Write`_

### [2026-09-13T22:32:37.978Z] AGENTE
Vou gerar o diagrama C4 de duas formas diferentes, para comparar.


_[2026-09-13T22:32:55.841Z] ferramenta usada: `Write`_

_[2026-09-13T22:35:39.668Z] ferramenta usada: `Bash`_

### [2026-09-13T22:36:02.355Z] AGENTE
Agora a **Etapa 6**. Vou escolher a Opção A (dívida técnica) — rodar uma ferramenta de análise estática real sobre o código.


_[2026-09-13T22:36:03.120Z] ferramenta usada: `Bash`_

### [2026-09-13T22:36:23.829Z] AGENTE
Instalado. Vou rodar ambos sobre o código real.


_[2026-09-13T22:36:24.316Z] ferramenta usada: `Bash`_

_[2026-09-13T22:36:44.455Z] ferramenta usada: `Bash`_

### [2026-09-13T22:36:59.546Z] AGENTE
Agora bandit, focado em segurança (mais útil para achar dívida técnica de risco real, não só estilo):


_[2026-09-13T22:37:00.126Z] ferramenta usada: `Bash`_

### [2026-09-13T22:37:19.701Z] AGENTE
Achado real e relevante: **uso inseguro de `torch.load`** (B614, severidade média, confiança alta) — risco real de execução de código arbitrário se o arquivo `.pt` for adulterado. Vou verificar a correção antes de documentar.


_[2026-09-13T22:37:20.616Z] ferramenta usada: `Bash`_

_[2026-09-13T22:37:40.706Z] ferramenta usada: `Bash`_

### [2026-09-13T22:38:01.468Z] AGENTE
A correção funciona sem quebrar nada. Vou aplicar a mitigação e documentar tudo.


_[2026-09-13T22:38:01.947Z] ferramenta usada: `Bash`_

_[2026-09-13T22:38:21.301Z] ferramenta usada: `Edit`_

_[2026-09-13T22:41:57.268Z] ferramenta usada: `Bash`_

### [2026-09-13T22:42:37.253Z] AGENTE
Todos os testes continuam passando. Agora documento a Etapa 6.


_[2026-09-13T22:42:48.571Z] ferramenta usada: `Write`_

_[2026-09-13T22:43:14.956Z] ferramenta usada: `Bash`_

### [2026-09-13T22:43:38.933Z] AGENTE
Etapa 7 (Git/GitHub) já está satisfeita — histórico real de commits ao longo de todas as etapas, no repositório público. Vou para a **Etapa 8 — Relatório Final**.


_[2026-09-13T22:43:57.868Z] ferramenta usada: `Write`_

### [2026-09-13T22:44:19.910Z] AGENTE
Agora atualizo o README (marcar checklist) e reexporto o log de sessão completo até aqui.


_[2026-09-13T22:44:20.278Z] ferramenta usada: `Read`_

_[2026-09-13T22:44:44.334Z] ferramenta usada: `Edit`_

### [2026-09-13T22:45:12.009Z] AGENTE
Agora reexporto o log de sessão completo até o fim da atividade.


_[2026-09-13T22:45:14.828Z] ferramenta usada: `Bash`_
