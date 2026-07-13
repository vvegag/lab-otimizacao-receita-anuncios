# Laboratório de Otimização de Receita de Anúncios

POC em Streamlit para demonstrar uma visao ponta a ponta de Data Science aplicada a monetizacao de anuncios: dados sinteticos estilo Google Ad Manager e CDP, arquitetura Bronze/Silver/Gold, metricas AdTech, dashboards, modelo preditivo, simulador A/B e handoff para engenharia.

## Por que esta POC existe

A entrevista pede uma conversa sobre dados de anuncios, comportamento de usuario, produto e engenharia. Esta POC mostra que o problema nao termina no notebook: os dados precisam ser validados, transformados em tabela analitica confiavel, expostos em dashboard, usados em modelo simples e entregues de forma compreensivel para engenharia e negocio.

## Estrutura

```text
app.py
src/
  data_generation.py
  data_quality.py
  transformations.py
  metrics.py
  modeling.py
  ab_testing.py
  recommendations.py
data/
  bronze/
  silver/
  gold/
docs/
tests/
```

## Arquitetura Medalhao

Bronze:
- `gam_ad_events.csv`
- `cdp_user_events.csv`

Silver:
- dados tipados, limpos e validados;
- join GAM + CDP por `event_id`;
- regras fortes: `clicks <= impressions <= ad_requests`, `viewable_impressions <= impressions`, `revenue >= 0`, IDs obrigatorios.

Gold:
- tabela analitica `data/gold/ad_revenue_gold.csv`;
- metricas: CTR, eCPM, fill rate, viewability rate, RPS, RPM, bounce rate, scroll depth e time on page.

## Como rodar

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

Para validar a POC:

```powershell
python -m unittest discover -s tests
```

Ou, se `pytest` estiver instalado:

```powershell
pytest
```

## Validação e demonstração

Para um passo a passo completo de execução, geração dos dados sintéticos, validação local no Bash, validação com Streamlit e checagem final do fluxo, veja:

- [`docs/validacao_e_demonstracao.md`](docs/validacao_e_demonstracao.md)
