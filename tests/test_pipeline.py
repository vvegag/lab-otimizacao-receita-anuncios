import unittest

from src.data_generation import SyntheticDataConfig, generate_synthetic_data
from src.data_quality import validate_cdp_events, validate_gam_events
from src.modeling import train_revenue_model
from src.transformations import create_gold, create_silver


class TestPipeline(unittest.TestCase):
    def test_synthetic_data_quality_rules_hold(self):
        gam, cdp = generate_synthetic_data(SyntheticDataConfig(n_events=500, random_seed=7))
        assert validate_gam_events(gam) == []
        assert validate_cdp_events(cdp) == []
        assert (gam["clicks"] <= gam["impressions"]).all()
        assert (gam["impressions"] <= gam["ad_requests"]).all()
        assert (gam["revenue"] >= 0).all()

    def test_medallion_gold_and_model_smoke(self):
        gam, cdp = generate_synthetic_data(SyntheticDataConfig(n_events=800, random_seed=11))
        _, _, joined = create_silver(gam, cdp)
        gold = create_gold(joined)
        assert not gold.empty
        assert {"ctr", "ecpm", "fill_rate", "viewability_rate", "rps", "rpm"}.issubset(gold.columns)
        _, metrics, scored = train_revenue_model(gold)
        assert "mae" in metrics
        assert "predicted_revenue" in scored.columns
