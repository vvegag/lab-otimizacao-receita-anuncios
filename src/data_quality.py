from __future__ import annotations

import pandas as pd


REQUIRED_GAM_COLUMNS = {
    "event_id",
    "timestamp",
    "session_id",
    "page_id",
    "ad_requests",
    "impressions",
    "viewable_impressions",
    "clicks",
    "revenue",
}

REQUIRED_CDP_COLUMNS = {
    "event_id",
    "timestamp",
    "user_id",
    "session_id",
    "page_id",
    "page_views",
    "time_on_page_seconds",
    "scroll_depth_pct",
    "bounce",
}


def validate_gam_events(df: pd.DataFrame) -> list[str]:
    errors: list[str] = []
    missing = REQUIRED_GAM_COLUMNS.difference(df.columns)
    if missing:
        errors.append(f"Missing GAM columns: {sorted(missing)}")
        return errors

    if df[["event_id", "session_id", "page_id"]].isna().any().any():
        errors.append("GAM has null identifiers.")
    if pd.to_datetime(df["timestamp"], errors="coerce").isna().any():
        errors.append("GAM has invalid timestamps.")
    if (df["impressions"] > df["ad_requests"]).any():
        errors.append("GAM quality rule failed: impressions > ad_requests.")
    if (df["clicks"] > df["impressions"]).any():
        errors.append("GAM quality rule failed: clicks > impressions.")
    if (df["viewable_impressions"] > df["impressions"]).any():
        errors.append("GAM quality rule failed: viewable_impressions > impressions.")
    if (df["revenue"] < 0).any():
        errors.append("GAM quality rule failed: revenue < 0.")
    if df["event_id"].duplicated().any():
        errors.append("GAM has duplicated event_id values.")
    return errors


def validate_cdp_events(df: pd.DataFrame) -> list[str]:
    errors: list[str] = []
    missing = REQUIRED_CDP_COLUMNS.difference(df.columns)
    if missing:
        errors.append(f"Missing CDP columns: {sorted(missing)}")
        return errors

    if df[["event_id", "user_id", "session_id", "page_id"]].isna().any().any():
        errors.append("CDP has null identifiers.")
    if pd.to_datetime(df["timestamp"], errors="coerce").isna().any():
        errors.append("CDP has invalid timestamps.")
    if (df["page_views"] < 0).any():
        errors.append("CDP quality rule failed: page_views < 0.")
    if (df["time_on_page_seconds"] < 0).any():
        errors.append("CDP quality rule failed: time_on_page_seconds < 0.")
    if ((df["scroll_depth_pct"] < 0) | (df["scroll_depth_pct"] > 100)).any():
        errors.append("CDP quality rule failed: scroll_depth_pct outside 0-100.")
    if df["event_id"].duplicated().any():
        errors.append("CDP has duplicated event_id values.")
    return errors


def assert_quality(gam: pd.DataFrame, cdp: pd.DataFrame) -> None:
    errors = validate_gam_events(gam) + validate_cdp_events(cdp)
    if errors:
        raise ValueError("Data quality validation failed:\n" + "\n".join(f"- {error}" for error in errors))
