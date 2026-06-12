from __future__ import annotations

import numpy as np
import pandas as pd


def safe_divide(numerator: pd.Series | float, denominator: pd.Series | float) -> pd.Series | float:
    numerator_array = np.asarray(numerator, dtype=float)
    denominator_array = np.asarray(denominator, dtype=float)
    return np.divide(
        numerator_array,
        denominator_array,
        out=np.zeros_like(numerator_array, dtype=float),
        where=denominator_array != 0,
    )


def add_ad_metrics(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["ctr"] = safe_divide(out["clicks"], out["impressions"])
    out["ecpm"] = safe_divide(out["revenue"] * 1000, out["impressions"])
    out["fill_rate"] = safe_divide(out["impressions"], out["ad_requests"])
    out["viewability_rate"] = safe_divide(out["viewable_impressions"], out["impressions"])
    out["rps"] = safe_divide(out["revenue"], out["sessions"])
    out["rpm"] = safe_divide(out["revenue"] * 1000, out["page_views"])
    out["bounce_rate"] = safe_divide(out["bounces"], out["page_views"])
    return out
