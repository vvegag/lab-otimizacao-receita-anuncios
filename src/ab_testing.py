from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats


def simulate_ab_test(gold: pd.DataFrame, treatment_lift: float = 0.08, ux_penalty: float = 0.03, random_state: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(random_state)
    base = gold.sample(min(len(gold), 800), replace=len(gold) < 800, random_state=random_state).copy()
    base["variant"] = rng.choice(["Controle", "Tratamento"], len(base))
    treatment_mask = base["variant"] == "Tratamento"

    base["sim_revenue"] = base["revenue"] * rng.normal(1.0, 0.04, len(base))
    base.loc[treatment_mask, "sim_revenue"] *= 1 + treatment_lift
    base["sim_ecpm"] = np.where(base["impressions"] == 0, 0, base["sim_revenue"] * 1000 / base["impressions"])

    base["sim_time_on_page_seconds"] = base["avg_time_on_page_seconds"] * rng.normal(1.0, 0.03, len(base))
    base.loc[treatment_mask, "sim_time_on_page_seconds"] *= 1 - ux_penalty
    base["sim_bounce_rate"] = np.clip(base["bounce_rate"] + rng.normal(0, 0.015, len(base)), 0, 1)
    base.loc[treatment_mask, "sim_bounce_rate"] = np.clip(base.loc[treatment_mask, "sim_bounce_rate"] + ux_penalty, 0, 1)
    return base


def summarize_ab_test(simulated: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, float]]:
    summary = (
        simulated.groupby("variant", as_index=False)
        .agg(
            revenue=("sim_revenue", "sum"),
            ecpm=("sim_ecpm", "mean"),
            time_on_page_seconds=("sim_time_on_page_seconds", "mean"),
            bounce_rate=("sim_bounce_rate", "mean"),
            sessions=("sessions", "sum"),
        )
        .sort_values("variant")
    )
    control = simulated.loc[simulated["variant"] == "Controle", "sim_revenue"]
    treatment = simulated.loc[simulated["variant"] == "Tratamento", "sim_revenue"]
    p_value = float(stats.ttest_ind(treatment, control, equal_var=False).pvalue) if len(control) > 1 and len(treatment) > 1 else 1.0
    diagnostics = {"revenue_p_value": p_value}
    return summary, diagnostics
