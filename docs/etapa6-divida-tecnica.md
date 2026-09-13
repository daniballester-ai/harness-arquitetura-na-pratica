# Etapa 6 — Dívida Técnica (Opção A)

## Ferramentas rodadas

```bash
pip install ruff bandit
python -m ruff check src/ tests/
python -m bandit -r src/ -q
```

`ruff` (lint geral) encontrou 10 avisos, majoritariamente estilo/organização de imports (import não ordenado, alias desnecessário, `Optional` implícito). `bandit` (análise estática focada em segurança) encontrou o achado mais relevante desta etapa.

## Sinal real de dívida técnica identificado

```
>> Issue: [B614:pytorch_load] Use of unsafe PyTorch load
   Severity: Medium   Confidence: High
   CWE: CWE-502 (Deserialization of Untrusted Data)
   Location: src/inference_service/model.py:79
   state_dict = torch.load(os.path.join(models_dir, "cacao_leaf_classifier.pt"), map_location="cpu")
```

**Por que é um risco real, não só estilo**: `torch.load` sem `weights_only=True` usa `pickle` por baixo dos panos, o que permite execução de código arbitrário se o arquivo `.pt` carregado for adulterado ou vier de fonte não confiável (CWE-502, deserialização de dados não confiáveis). Neste projeto especificamente, o artefato do modelo é justamente o arquivo que o hook da Etapa 1 protege contra apagar/sobrescrever — mas nada impedia, antes desta correção, que um `.pt` malicioso substituído no lugar certo executasse código arbitrário assim que o serviço subisse.

## Mitigação aplicada

Adicionado `weights_only=True` na chamada de `torch.load` (`src/inference_service/model.py`), restringindo o carregamento a apenas tensores (pesos), sem permitir desserialização de objetos Python arbitrários via pickle. Verificado que:
- O carregamento do artefato real continua funcionando (`state_dict` com as mesmas 360 chaves).
- A suíte completa de testes continua passando (55/55) após a mudança.

## Achados menores (não corrigidos nesta etapa, registrados para o backlog)

- `RUF013`/imports desorganizados: cosméticos, sem risco funcional.
- 3 ocorrências de `B105` (possível senha hardcoded): falsos positivos — são exemplos de documentação da API (`examples=[...]`) e um script de smoke-test manual (`verify_api.py`), não credenciais reais.
- `B008` (chamada de função em default de argumento do FastAPI, `File(...)`/`Body(...)`): é o padrão idiomático do próprio FastAPI, não uma dívida real — o linter não conhece essa convenção do framework.
