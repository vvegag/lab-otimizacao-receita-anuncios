from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.data_generation import SyntheticDataConfig, write_bronze_data
from src.data_quality import assert_quality
from src.metrics import add_ad_metrics


def load_bronze(bronze_dir: str | Path = "data/bronze") -> tuple[pd.DataFrame, pd.DataFrame]:
    bronze_path = Path(bronze_dir)
    gam = pd.read_csv(bronze_path / "gam_ad_events.csv", parse_dates=["timestamp"])
    cdp = pd.read_csv(bronze_path / "cdp_user_events.csv", parse_dates=["timestamp"])
    return gam, cdp


def create_silver(gam: pd.DataFrame, cdp: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    gam_clean = gam.copy()
    cdp_clean = cdp.copy()
    gam_clean["timestamp"] = pd.to_datetime(gam_clean["timestamp"], errors="coerce")
    cdp_clean["timestamp"] = pd.to_datetime(cdp_clean["timestamp"], errors="coerce")

    numeric_gam = ["ad_requests", "impressions", "viewable_impressions", "clicks", "revenue"]
    numeric_cdp = ["page_views", "time_on_page_seconds", "scroll_depth_pct", "bounce", "is_returning_user"]
    for column in numeric_gam:
        gam_clean[column] = pd.to_numeric(gam_clean[column], errors="coerce").fillna(0)
    for column in numeric_cdp:
        cdp_clean[column] = pd.to_numeric(cdp_clean[column], errors="coerce").fillna(0)

    gam_clean = gam_clean.drop_duplicates(subset=["event_id"])
    cdp_clean = cdp_clean.drop_duplicates(subset=["event_id"])
    assert_quality(gam_clean, cdp_clean)

    joined = gam_clean.merge(
        cdp_clean[
            [
                "event_id",
                "user_id",
                "traffic_source",
                "is_returning_user",
                "page_views",
                "time_on_page_seconds",
                "scroll_depth_pct",
                "bounce",
            ]
        ],
        on="event_id",
        how="inner",
        validate="one_to_one",
    )
    joined["date"] = joined["timestamp"].dt.date.astype(str)
    return gam_clean, cdp_clean, joined


def create_gold(joined: pd.DataFrame) -> pd.DataFrame:
    group_cols = ["date", "site_id", "page_category", "ad_unit", "ad_format", "device", "traffic_source"]
    gold = (
        joined.groupby(group_cols, as_index=False)
        .agg(
            ad_requests=("ad_requests", "sum"),
            impressions=("impressions", "sum"),
            viewable_impressions=("viewable_impressions", "sum"),
            clicks=("clicks", "sum"),
            revenue=("revenue", "sum"),
            sessions=("session_id", "nunique"),
            users=("user_id", "nunique"),
            page_views=("page_views", "sum"),
            avg_time_on_page_seconds=("time_on_page_seconds", "mean"),
            avg_scroll_depth_pct=("scroll_depth_pct", "mean"),
            bounces=("bounce", "sum"),
            returning_user_rate=("is_returning_user", "mean"),
        )
        .sort_values(["date", "revenue"], ascending=[True, False])
    )
    gold = add_ad_metrics(gold)
    return gold


def build_medallion_pipeline(
    config: SyntheticDataConfig | None = None,
    data_dir: str | Path = "data",
    force_regenerate: bool = False,
) -> pd.DataFrame:
    data_path = Path(data_dir)
    bronze_dir = data_path / "bronze"
    silver_dir = data_path / "silver"
    gold_dir = data_path / "gold"
    silver_dir.mkdir(parents=True, exist_ok=True)
    gold_dir.mkdir(parents=True, exist_ok=True)

    if force_regenerate or not (bronze_dir / "gam_ad_events.csv").exists() or not (bronze_dir / "cdp_user_events.csv").exists():
        write_bronze_data(bronze_dir, config)

    gam, cdp = load_bronze(bronze_dir)
    gam_clean, cdp_clean, joined = create_silver(gam, cdp)
    gam_clean.to_csv(silver_dir / "gam_ad_events_clean.csv", index=False)
    cdp_clean.to_csv(silver_dir / "cdp_user_events_clean.csv", index=False)
    joined.to_csv(silver_dir / "gam_cdp_joined.csv", index=False)

    gold = create_gold(joined)
    gold.to_csv(gold_dir / "ad_revenue_gold.csv", index=False)
    return gold
