# Harness e Arquitetura na Prática

Repositório de entrega da atividade prática assíncrona **Harness e Arquitetura na Prática** (Desenvolvimento de Software com IA, PPGTI/UFRN, Prof. Jean Mário Moreira de Lima).

## Sobre o projeto

Este repositório usa como base de código real uma fatia do serviço de inferência do [CacauFito](https://github.com/daniballester-ai/cacau-fito) (API FastAPI de classificação de folhas de cacau): `src/inference_service/`, seus testes (`tests/`), o modelo treinado (`models/`) e os assets estáticos do frontend (`frontend/static/`) necessários para a API subir. Não é o repositório do projeto CacauFito, é uma cópia isolada, criada especificamente para experimentar hooks, TDD, worktrees e revisão arquitetural sem risco de afetar o projeto original.

### Como rodar

```bash
python -m pip install -r requirements.txt
python -m uvicorn src.inference_service.main:app --reload
```

Abra `http://127.0.0.1:8000/health`.

### Testes

```bash
python -m pytest tests/ -v
```

## Entregáveis da atividade

- [ ] **Etapa 1** — Comparação entre os dois modos de autonomia testados + hook funcional commitado, com evidência do bloqueio.
- [ ] **Etapa 2** — Evidência do ciclo Red-Green-Refactor, relato da ferramenta de enforcement investigada, e comparação com/sem TDD.
- [ ] **Etapa 3** — Log/transcript da sessão (`docs/sessao-log.md`) e registro do checkpoint humano simulado.
- [ ] **Etapa 4** — Resumo da arquitetura atual (gerado com apoio de IA) e decisão arquitetural justificada.
- [ ] **Etapa 5** — ADR (`docs/adr/`) e diagrama de arquitetura, com comparação entre duas versões do diagrama.
- [ ] **Etapa 6** — Evidência da opção escolhida (dívida técnica, custo/performance, ou agentes em paralelo).
- [ ] **Etapa 7** — Histórico de commits real, refletindo o processo (este arquivo).
- [ ] **Etapa 8** — Relatório final de até 1 página (`docs/relatorio-final.md`).

## Estrutura

```text
src/inference_service/   API de inferência (predict, history, stats, auth, feedback, export CSV)
tests/                   suíte pytest (49 testes)
models/                  modelo treinado (EfficientNet-B0) + mapeamento de classes
frontend/static/         assets estáticos servidos pela API
samples/                 imagens de exemplo usadas pelos testes e por testes manuais
docs/                    log de sessão, ADRs, diagramas, relatório final
```

## Autoria

Danielle Magalhães Ballester ([danielleballester@gmail.com](mailto:danielleballester@gmail.com)), trabalho de PPGTI/UFRN.
