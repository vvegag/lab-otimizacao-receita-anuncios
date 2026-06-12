from __future__ import annotations

import plotly.express as px
import streamlit as st

from src.ab_testing import simulate_ab_test, summarize_ab_test
from src.data_generation import SyntheticDataConfig
from src.modeling import feature_importance, train_revenue_model
from src.recommendations import generate_recommendations
from src.transformations import build_medallion_pipeline


APP_NAME = "Laboratório de Otimização de Receita de Anúncios"


st.set_page_config(page_title=APP_NAME, layout="wide")


PAGE_OVERVIEW = "Visão geral"
PAGE_AD_PERFORMANCE = "Performance de anúncios"
PAGE_USER_BEHAVIOR = "Comportamento do usuário"
PAGE_REVENUE_FORECAST = "Previsão de receita"
PAGE_AB_TEST = "Simulador de teste A/B"
PAGE_RECOMMENDATIONS = "Recomendações de negócio"
PAGE_HANDOFF = "Handoff para engenharia"

LABELS = {
    "date": "Data",
    "site_id": "Site",
    "page_category": "Categoria da página",
    "ad_unit": "Bloco de anúncio",
    "ad_format": "Formato do anúncio",
    "device": "Dispositivo",
    "traffic_source": "Origem do tráfego",
    "revenue": "Receita",
    "predicted_revenue": "Receita prevista",
    "impressions": "Impressões",
    "clicks": "Cliques",
    "ecpm": "eCPM",
    "ctr": "CTR",
    "fill_rate": "Taxa de preenchimento",
    "viewability_rate": "Taxa de visibilidade",
    "rps": "RPS",
    "rpm": "RPM",
    "sessions": "Sessões",
    "page_views": "Visualizações de página",
    "avg_time_on_page_seconds": "Tempo médio na página (s)",
    "avg_scroll_depth_pct": "Profundidade média de rolagem (%)",
    "bounce_rate": "Taxa de rejeição",
    "returning_user_rate": "Taxa de usuários recorrentes",
    "variant": "Variante",
    "time_on_page_seconds": "Tempo na página (s)",
    "variable": "Métrica",
    "value": "Valor",
}

TABLE_COLUMNS = {
    "date": "Data",
    "site_id": "Site",
    "page_category": "Categoria da página",
    "ad_unit": "Bloco de anúncio",
    "ad_format": "Formato do anúncio",
    "device": "Dispositivo",
    "traffic_source": "Origem do tráfego",
    "ad_requests": "Requisições de anúncio",
    "impressions": "Impressões",
    "viewable_impressions": "Impressões visíveis",
    "clicks": "Cliques",
    "revenue": "Receita",
    "sessions": "Sessões",
    "users": "Usuários",
    "page_views": "Visualizações de página",
    "avg_time_on_page_seconds": "Tempo médio na página (s)",
    "avg_scroll_depth_pct": "Profundidade média de rolagem (%)",
    "bounces": "Rejeições",
    "returning_user_rate": "Taxa de usuários recorrentes",
    "ctr": "CTR",
    "ecpm": "eCPM",
    "fill_rate": "Taxa de preenchimento",
    "viewability_rate": "Taxa de visibilidade",
    "rps": "RPS",
    "rpm": "RPM",
    "bounce_rate": "Taxa de rejeição",
    "feature": "Variável",
    "importance": "Importância",
    "variant": "Variante",
    "sim_revenue": "Receita simulada",
    "time_on_page_seconds": "Tempo na página (s)",
    "priority": "Prioridade",
    "area": "Área",
    "signal": "Sinal",
    "recommendation": "Recomendação",
}


def display_table(df):
    return df.rename(columns=TABLE_COLUMNS)


@st.cache_data(show_spinner=False)
def load_data(n_events: int, seed: int, force_regenerate: bool):
    config = SyntheticDataConfig(n_events=n_events, random_seed=seed)
    return build_medallion_pipeline(config=config, force_regenerate=force_regenerate)


st.sidebar.title("Receita de Anúncios")
n_events = st.sidebar.slider("Eventos sintéticos", min_value=1000, max_value=20000, value=6000, step=1000)
seed = st.sidebar.number_input("Semente aleatória", min_value=1, max_value=9999, value=42)
force = st.sidebar.button("Regenerar dados")

gold = load_data(n_events, int(seed), force)
pages = [
    PAGE_OVERVIEW,
    PAGE_AD_PERFORMANCE,
    PAGE_USER_BEHAVIOR,
    PAGE_REVENUE_FORECAST,
    PAGE_AB_TEST,
    PAGE_RECOMMENDATIONS,
    PAGE_HANDOFF,
]
page = st.sidebar.radio("Seção", pages)

st.title(APP_NAME)
st.caption("Dados sintéticos GAM + CDP, arquitetura medalhão, dashboards, modelo preditivo, métricas de proteção em teste A/B e handoff para engenharia.")


def kpi(label: str, value: str):
    st.metric(label, value)


if page == PAGE_OVERVIEW:
    st.subheader("Visão geral do portfólio")
    cols = st.columns(6)
    cols[0].metric("Receita", f"${gold['revenue'].sum():,.2f}")
    cols[1].metric("Impressões", f"{gold['impressions'].sum():,.0f}")
    cols[2].metric("CTR", f"{gold['clicks'].sum() / max(gold['impressions'].sum(), 1):.2%}")
    cols[3].metric("eCPM", f"${gold['revenue'].sum() * 1000 / max(gold['impressions'].sum(), 1):.2f}")
    cols[4].metric("Taxa de preenchimento", f"{gold['impressions'].sum() / max(gold['ad_requests'].sum(), 1):.1%}")
    cols[5].metric("RPS", f"${gold['revenue'].sum() / max(gold['sessions'].sum(), 1):.4f}")

    daily = gold.groupby("date", as_index=False).agg(revenue=("revenue", "sum"), impressions=("impressions", "sum"), sessions=("sessions", "sum"))
    daily["date"] = daily["date"].apply(lambda value: f"{value[8:10]}/{value[5:7]}/{value[0:4]}")
    st.plotly_chart(px.line(daily, x="date", y="revenue", title="Receita diária", labels=LABELS), width="stretch")
    st.dataframe(display_table(gold.head(30)), width="stretch", hide_index=True)

elif page == PAGE_AD_PERFORMANCE:
    st.subheader("Performance de anúncios")
    col1, col2 = st.columns(2)
    by_format = gold.groupby("ad_format", as_index=False).agg(ecpm=("ecpm", "mean"), revenue=("revenue", "sum"), ctr=("ctr", "mean"))
    by_unit = gold.groupby("ad_unit", as_index=False).agg(fill_rate=("fill_rate", "mean"), viewability_rate=("viewability_rate", "mean"), revenue=("revenue", "sum"))
    col1.plotly_chart(px.bar(by_format, x="ad_format", y="ecpm", color="ad_format", title="eCPM por formato de anúncio", labels=LABELS), width="stretch")
    col2.plotly_chart(px.scatter(by_unit, x="fill_rate", y="viewability_rate", size="revenue", color="ad_unit", title="Taxa de preenchimento vs. visibilidade", labels=LABELS), width="stretch")
    st.plotly_chart(px.treemap(gold, path=["page_category", "ad_format", "ad_unit"], values="revenue", color="ecpm", title="Composição da receita", labels=LABELS), width="stretch")

elif page == PAGE_USER_BEHAVIOR:
    st.subheader("Comportamento do usuário")
    by_source = gold.groupby("traffic_source", as_index=False).agg(
        rps=("rps", "mean"),
        avg_scroll_depth_pct=("avg_scroll_depth_pct", "mean"),
        avg_time_on_page_seconds=("avg_time_on_page_seconds", "mean"),
        bounce_rate=("bounce_rate", "mean"),
        revenue=("revenue", "sum"),
    )
    col1, col2 = st.columns(2)
    col1.plotly_chart(px.bar(by_source, x="traffic_source", y="rps", color="traffic_source", title="Receita por sessão por origem de tráfego", labels=LABELS), width="stretch")
    col2.plotly_chart(px.scatter(by_source, x="avg_scroll_depth_pct", y="avg_time_on_page_seconds", size="revenue", color="traffic_source", title="Engajamento e receita", labels=LABELS), width="stretch")
    st.plotly_chart(px.bar(by_source, x="traffic_source", y="bounce_rate", color="traffic_source", title="Taxa de rejeição por origem", labels=LABELS), width="stretch")

elif page == PAGE_REVENUE_FORECAST:
    st.subheader("Modelo de previsão de receita")
    model, metrics, scored = train_revenue_model(gold)
    cols = st.columns(2)
    cols[0].metric("MAE", f"${metrics['mae']:.4f}")
    cols[1].metric("R2", f"{metrics['r2']:.3f}")
    st.plotly_chart(px.scatter(scored, x="revenue", y="predicted_revenue", color="ad_format", title="Receita real vs. receita prevista", labels=LABELS), width="stretch")
    st.dataframe(display_table(feature_importance(model)), width="stretch", hide_index=True)

elif page == PAGE_AB_TEST:
    st.subheader("Simulador de teste A/B")
    col1, col2 = st.columns(2)
    lift = col1.slider("Ganho de receita do tratamento", 0.0, 0.25, 0.08, 0.01)
    penalty = col2.slider("Penalidade na experiência do usuário", 0.0, 0.15, 0.03, 0.01)
    simulated = simulate_ab_test(gold, treatment_lift=lift, ux_penalty=penalty, random_state=int(seed))
    summary, diagnostics = summarize_ab_test(simulated)
    st.dataframe(display_table(summary), width="stretch", hide_index=True)
    st.metric("p-valor da receita", f"{diagnostics['revenue_p_value']:.4f}")
    c1, c2 = st.columns(2)
    primary_metrics = summary.rename(columns={"revenue": "Receita", "ecpm": "eCPM"})
    protection_metrics = summary.rename(columns={"time_on_page_seconds": "Tempo na página (s)", "bounce_rate": "Taxa de rejeição"})
    c1.plotly_chart(px.bar(primary_metrics, x="variant", y=["Receita", "eCPM"], barmode="group", title="Métricas primárias", labels={"variant": "Variante", "variable": "Métrica", "value": "Valor"}), width="stretch")
    c2.plotly_chart(px.bar(protection_metrics, x="variant", y=["Tempo na página (s)", "Taxa de rejeição"], barmode="group", title="Métricas de proteção", labels={"variant": "Variante", "variable": "Métrica", "value": "Valor"}), width="stretch")

elif page == PAGE_RECOMMENDATIONS:
    st.subheader("Recomendações de negócio")
    st.dataframe(display_table(generate_recommendations(gold)), width="stretch", hide_index=True)

elif page == PAGE_HANDOFF:
    st.subheader("Handoff para engenharia")
    st.markdown(
        """
| Tópico | Definição na POC | Caminho para produção |
|---|---|---|
| Entradas | Eventos sintéticos do GAM e eventos de usuário da CDP | Exportações/API reais do GAM mais pipeline de eventos da CDP |
| Granularidade | Evento na Bronze/Silver, segmento-dia na Gold | Granularidade contratada do evento e tabelas Gold particionadas |
| Saída | `data/gold/ad_revenue_gold.csv` | Tabela gerenciada ou API consumida por dashboards/produtos |
| Atualização | Regeneração manual no Streamlit | Job agendado com checagens de frescor dos dados |
| Qualidade | clicks <= impressions <= ad_requests; revenue >= 0; IDs não nulos | Testes automatizados, alertas, validação de schema e linhagem |
| Modelo | Regressor Random Forest para receita | Modelo registrado com monitoramento, drift e política de retreino |
| Guardrails A/B | Receita/eCPM mais tempo na página e taxa de rejeição | Plataforma de experimentos com métricas primárias e de proteção |
"""
    )
    st.markdown(
        """
Próximos passos para produção:

1. Substituir a geração de CSVs por conectores reais GAM/CDP.
2. Mover transformações para Databricks, dbt ou jobs Spark orquestrados.
3. Adicionar contratos de dados para as tabelas Bronze e Silver.
4. Registrar métricas Gold em uma camada semântica compartilhada.
5. Servir os scores do modelo por tabela ou API leve.
6. Monitorar receita, visibilidade, taxa de preenchimento, guardrails de UX e drift do modelo.
"""
    )
