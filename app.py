
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="FMCG AI & Automation Hub",
    page_icon="📊",
    layout="wide"
)

st.title("FMCG AI & Automation Hub")
st.caption("Demand forecasting, anomaly detection, and inventory risk intelligence")

results = pd.read_csv("results_dashboard.csv")
inventory = pd.read_csv("inventory_dashboard.csv")

results["date"] = pd.to_datetime(results["date"])
inventory["date"] = pd.to_datetime(inventory["date"])

mae = (results["actual_sales"] - results["predicted_sales"]).abs().mean()

rmse = (
    ((results["actual_sales"] - results["predicted_sales"]) ** 2).mean()
) ** 0.5

anomaly_count = results["is_anomaly"].sum()

high_risk_days = (
    inventory["risk_level"] == "High Risk"
).sum()

reorder_cases = (
    inventory["recommendation"] == "Reorder"
).sum()

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Forecast MAE", f"{mae:,.0f}")
col2.metric("Forecast RMSE", f"{rmse:,.0f}")
col3.metric("Anomalies", int(anomaly_count))
col4.metric("High-Risk Days", int(high_risk_days))
col5.metric("Reorder Cases", int(reorder_cases))

st.subheader("Actual vs Predicted Sales")

chart_data = results.set_index("date")[
    ["actual_sales", "predicted_sales"]
]

st.line_chart(chart_data)

# -----------------------------
# Anomaly Detection
# -----------------------------

st.divider()
st.subheader("Anomaly Detection")

results["is_anomaly"] = (
    results["is_anomaly"]
    .astype(str)
    .str.lower()
    .eq("true")
)

anomalies = results[results["is_anomaly"]].copy()

higher_anomalies = (
    anomalies["anomaly_type"] == "Higher than expected"
).sum()

lower_anomalies = (
    anomalies["anomaly_type"] == "Lower than expected"
).sum()

a1, a2, a3 = st.columns(3)

a1.metric("Detected Anomalies", len(anomalies))
a2.metric("Higher Than Expected", int(higher_anomalies))
a3.metric("Lower Than Expected", int(lower_anomalies))

st.dataframe(
    anomalies[
        [
            "date",
            "actual_sales",
            "predicted_sales",
            "absolute_error",
            "anomaly_type"
        ]
    ].sort_values("absolute_error", ascending=False),
    use_container_width=True
)

# -----------------------------
# Inventory Risk
# -----------------------------

st.divider()
st.subheader("Inventory Risk Simulation")

risk_counts = (
    inventory["risk_level"]
    .value_counts()
    .rename_axis("Risk Level")
    .to_frame("Days")
)

st.bar_chart(risk_counts)

# -----------------------------
# Reorder Priorities
# -----------------------------

st.subheader("Top Reorder Priorities")

reorder_priorities = (
    inventory[
        inventory["recommendation"] == "Reorder"
    ]
    .sort_values("reorder_quantity", ascending=False)
    .head(10)
)

st.dataframe(
    reorder_priorities[
        [
            "date",
            "predicted_sales",
            "days_of_stock",
            "risk_level",
            "reorder_quantity"
        ]
    ],
    use_container_width=True
)

# -----------------------------
# Business Recommendations
# -----------------------------

st.divider()
st.subheader("Business Recommendations")

st.write(
    "• Investigate unexpected demand spikes and strengthen stock planning for peak-demand days."
)

st.write(
    "• Prioritize high-risk inventory cases to reduce potential stock-out risk."
)

st.write(
    "• Review simulated reorder recommendations and prioritize the largest shortages."
)

st.caption(
    "Inventory values are simulated for demonstration because the source dataset does not include real stock-on-hand data."
)
