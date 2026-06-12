from __future__ import annotations

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


FEATURES = [
    "page_category",
    "ad_unit",
    "ad_format",
    "device",
    "traffic_source",
    "ad_requests",
    "impressions",
    "sessions",
    "page_views",
    "avg_time_on_page_seconds",
    "avg_scroll_depth_pct",
    "bounce_rate",
    "returning_user_rate",
]

FEATURE_LABELS = {
    "page_category": "Categoria da página",
    "ad_unit": "Bloco de anúncio",
    "ad_format": "Formato do anúncio",
    "device": "Dispositivo",
    "traffic_source": "Origem do tráfego",
    "ad_requests": "Requisições de anúncio",
    "impressions": "Impressões",
    "sessions": "Sessões",
    "page_views": "Visualizações de página",
    "avg_time_on_page_seconds": "Tempo médio na página",
    "avg_scroll_depth_pct": "Profundidade média de rolagem",
    "bounce_rate": "Taxa de rejeição",
    "returning_user_rate": "Taxa de usuários recorrentes",
}


def readable_feature_name(feature_name: str) -> str:
    if feature_name.startswith("numeric__"):
        raw_name = feature_name.removeprefix("numeric__")
        return FEATURE_LABELS.get(raw_name, raw_name)

    if feature_name.startswith("categorical__"):
        raw_name = feature_name.removeprefix("categorical__")
        for column in ["page_category", "traffic_source", "ad_format", "ad_unit", "device"]:
            prefix = f"{column}_"
            if raw_name.startswith(prefix):
                value = raw_name.removeprefix(prefix)
                return f"{FEATURE_LABELS[column]}: {value}"

    return feature_name.replace("_", " ")


def train_revenue_model(gold: pd.DataFrame, random_state: int = 42) -> tuple[Pipeline, dict[str, float], pd.DataFrame]:
    model_data = gold.dropna(subset=FEATURES + ["revenue"]).copy()
    X = model_data[FEATURES]
    y = model_data["revenue"]

    categorical = ["page_category", "ad_unit", "ad_format", "device", "traffic_source"]
    numeric = [column for column in FEATURES if column not in categorical]
    preprocessor = ColumnTransformer(
        transformers=[
            ("categorical", OneHotEncoder(handle_unknown="ignore"), categorical),
            ("numeric", "passthrough", numeric),
        ]
    )
    model = RandomForestRegressor(n_estimators=160, min_samples_leaf=3, random_state=random_state, n_jobs=-1)
    pipeline = Pipeline([("preprocessor", preprocessor), ("model", model)])

    if len(model_data) < 20:
        pipeline.fit(X, y)
        predictions = pipeline.predict(X)
        metrics = {"mae": float(mean_absolute_error(y, predictions)), "r2": float(r2_score(y, predictions))}
        scored = model_data.assign(predicted_revenue=predictions)
        return pipeline, metrics, scored

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=random_state)
    pipeline.fit(X_train, y_train)
    predictions = pipeline.predict(X_test)
    metrics = {"mae": float(mean_absolute_error(y_test, predictions)), "r2": float(r2_score(y_test, predictions))}
    scored = model_data.copy()
    scored["predicted_revenue"] = pipeline.predict(X)
    return pipeline, metrics, scored


def feature_importance(model: Pipeline) -> pd.DataFrame:
    preprocessor = model.named_steps["preprocessor"]
    regressor = model.named_steps["model"]
    feature_names = preprocessor.get_feature_names_out()
    return (
        pd.DataFrame({"feature": [readable_feature_name(name) for name in feature_names], "importance": regressor.feature_importances_})
        .sort_values("importance", ascending=False)
        .head(15)
    )
