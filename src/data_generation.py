from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class SyntheticDataConfig:
    n_events: int = 5000
    start_date: str = "2026-03-01"
    periods_days: int = 60
    random_seed: int = 42


PAGE_CATEGORIES = ["notícias", "esportes", "finanças", "estilo de vida", "tecnologia", "entretenimento"]
AD_UNITS = ["topo da página", "meio do artigo", "lateral", "rodapé fixo", "intersticial"]
AD_FORMATS = ["banner", "nativo", "vídeo", "mídia rica"]
DEVICES = ["computador", "celular", "tablet"]
COUNTRIES = ["BR", "US", "MX", "AR", "CL"]
TRAFFIC_SOURCES = ["orgânico", "redes sociais", "direto", "referência", "newsletter"]


def generate_synthetic_data(config: SyntheticDataConfig | None = None) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Generate GAM-like ad events and CDP-like user behavior with strict constraints."""
    config = config or SyntheticDataConfig()
    rng = np.random.default_rng(config.random_seed)

    timestamps = pd.to_datetime(config.start_date) + pd.to_timedelta(
        rng.integers(0, config.periods_days * 24 * 60, config.n_events), unit="m"
    )
    event_ids = [f"evt_{i:06d}" for i in range(config.n_events)]
    session_ids = [f"sess_{rng.integers(1, max(2, config.n_events // 3)):06d}" for _ in range(config.n_events)]
    user_ids = [f"user_{rng.integers(1, max(2, config.n_events // 2)):06d}" for _ in range(config.n_events)]
    page_ids = [f"page_{rng.integers(1, 140):03d}" for _ in range(config.n_events)]

    page_category = rng.choice(PAGE_CATEGORIES, config.n_events, p=[0.22, 0.18, 0.14, 0.16, 0.17, 0.13])
    ad_format = rng.choice(AD_FORMATS, config.n_events, p=[0.46, 0.24, 0.18, 0.12])
    ad_unit = rng.choice(AD_UNITS, config.n_events, p=[0.28, 0.30, 0.16, 0.20, 0.06])
    device = rng.choice(DEVICES, config.n_events, p=[0.42, 0.48, 0.10])
    traffic_source = rng.choice(TRAFFIC_SOURCES, config.n_events, p=[0.40, 0.22, 0.18, 0.12, 0.08])

    category_multiplier = pd.Series(page_category).map(
        {
            "finanças": 1.35,
            "tecnologia": 1.20,
            "esportes": 1.05,
            "notícias": 1.00,
            "estilo de vida": 0.92,
            "entretenimento": 0.86,
        }
    ).to_numpy()
    format_multiplier = pd.Series(ad_format).map({"vídeo": 1.55, "mídia rica": 1.28, "nativo": 1.08, "banner": 0.92}).to_numpy()
    device_multiplier = pd.Series(device).map({"computador": 1.12, "tablet": 1.02, "celular": 0.92}).to_numpy()

    ad_requests = rng.integers(1, 7, config.n_events)
    fill_probability = np.clip(0.76 + 0.05 * (ad_unit == "topo da página") - 0.08 * (ad_unit == "intersticial"), 0.55, 0.96)
    impressions = rng.binomial(ad_requests, fill_probability)

    ctr_probability = np.clip(
        0.010
        + 0.008 * (ad_format == "nativo")
        + 0.006 * (ad_format == "vídeo")
        + 0.004 * (traffic_source == "redes sociais")
        - 0.003 * (device == "celular"),
        0.002,
        0.055,
    )
    clicks = rng.binomial(impressions, ctr_probability)

    viewable_impressions = rng.binomial(impressions, np.clip(0.63 + 0.10 * (ad_unit == "rodapé fixo") - 0.08 * (ad_unit == "lateral"), 0.35, 0.92))
    base_cpm = rng.lognormal(mean=1.45, sigma=0.38, size=config.n_events)
    revenue = impressions * base_cpm * category_multiplier * format_multiplier * device_multiplier / 1000
    revenue = np.maximum(revenue + rng.normal(0, 0.002, config.n_events), 0)

    gam = pd.DataFrame(
        {
            "event_id": event_ids,
            "timestamp": timestamps,
            "publisher_id": "demo_publisher",
            "site_id": rng.choice(["site A", "site B", "site C"], config.n_events, p=[0.45, 0.35, 0.20]),
            "session_id": session_ids,
            "page_id": page_ids,
            "page_category": page_category,
            "ad_unit": ad_unit,
            "ad_format": ad_format,
            "device": device,
            "country": rng.choice(COUNTRIES, config.n_events, p=[0.72, 0.10, 0.08, 0.06, 0.04]),
            "ad_requests": ad_requests,
            "impressions": impressions,
            "viewable_impressions": viewable_impressions,
            "clicks": clicks,
            "revenue": revenue.round(5),
        }
    )

    time_on_page = rng.gamma(shape=2.2, scale=28, size=config.n_events)
    scroll_depth = np.clip(rng.normal(58, 20, config.n_events) + 8 * (page_category == "finanças"), 1, 100)
    bounce_probability = np.clip(0.34 + 0.08 * (device == "celular") - 0.10 * (traffic_source == "newsletter"), 0.08, 0.72)

    cdp = pd.DataFrame(
        {
            "event_id": event_ids,
            "timestamp": timestamps,
            "user_id": user_ids,
            "session_id": session_ids,
            "page_id": page_ids,
            "page_category": page_category,
            "device": device,
            "traffic_source": traffic_source,
            "is_returning_user": rng.choice([0, 1], config.n_events, p=[0.62, 0.38]),
            "page_views": 1,
            "time_on_page_seconds": np.maximum(time_on_page, 3).round(1),
            "scroll_depth_pct": scroll_depth.round(1),
            "bounce": rng.binomial(1, bounce_probability),
        }
    )

    return gam, cdp


def write_bronze_data(output_dir: str | Path = "data/bronze", config: SyntheticDataConfig | None = None) -> tuple[Path, Path]:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    gam, cdp = generate_synthetic_data(config)
    gam_path = output_path / "gam_ad_events.csv"
    cdp_path = output_path / "cdp_user_events.csv"
    gam.to_csv(gam_path, index=False)
    cdp.to_csv(cdp_path, index=False)
    return gam_path, cdp_path
