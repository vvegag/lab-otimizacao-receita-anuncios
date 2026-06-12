from __future__ import annotations

import pandas as pd


def generate_recommendations(gold: pd.DataFrame) -> pd.DataFrame:
    recs: list[dict[str, str | float]] = []
    by_category = gold.groupby("page_category", as_index=False).agg(revenue=("revenue", "sum"), ecpm=("ecpm", "mean"), impressions=("impressions", "sum"))
    ecpm_median = by_category["ecpm"].median()
    high_traffic = by_category["impressions"].quantile(0.70)
    for row in by_category.itertuples(index=False):
        if row.impressions >= high_traffic and row.ecpm < ecpm_median:
            recs.append(
                {
                    "priority": "Alta",
                    "area": row.page_category,
                    "signal": f"Alto tráfego com eCPM abaixo da mediana ({row.ecpm:.2f}).",
                    "recommendation": "Revisar mix de blocos de anúncio, regras de preço mínimo e qualidade da demanda nessa categoria.",
                }
            )

    by_unit = gold.groupby("ad_unit", as_index=False).agg(viewability_rate=("viewability_rate", "mean"), fill_rate=("fill_rate", "mean"), revenue=("revenue", "sum"))
    for row in by_unit.itertuples(index=False):
        if row.viewability_rate < 0.60:
            recs.append(
                {
                    "priority": "Média",
                    "area": row.ad_unit,
                    "signal": f"Baixa visibilidade ({row.viewability_rate:.1%}).",
                    "recommendation": "Testar outro posicionamento ou formato antes de aumentar a densidade de anúncios.",
                }
            )
        if row.fill_rate < 0.72:
            recs.append(
                {
                    "priority": "Média",
                    "area": row.ad_unit,
                    "signal": f"Baixa taxa de preenchimento ({row.fill_rate:.1%}).",
                    "recommendation": "Investigar demanda, configuração de inventário e restrições de preço.",
                }
            )

    ux_risk = gold.loc[(gold["revenue"] > gold["revenue"].quantile(0.75)) & (gold["bounce_rate"] > gold["bounce_rate"].quantile(0.75))]
    if not ux_risk.empty:
        recs.append(
            {
                "priority": "Alta",
                "area": "Guardrail de experiência do usuário",
                "signal": "A receita é alta em alguns segmentos, mas a taxa de rejeição também está elevada.",
                "recommendation": "Manter tempo na página e taxa de rejeição como métricas de proteção nos experimentos de otimização.",
            }
        )

    if not recs:
        recs.append(
            {
                "priority": "Baixa",
                "area": "Portfólio",
                "signal": "Nenhum sinal sintético crítico foi detectado.",
                "recommendation": "Continuar monitorando receita, visibilidade e guardrails de UX por segmento.",
            }
        )
    return pd.DataFrame(recs)
