## Live Demo

[Open the FMCG AI & Automation Hub](https://fmcg-ai-automation-app-grynfttmtqfvtcytswuucd.streamlit.app/)
# FMCG AI & Automation Hub

An end-to-end FMCG analytics and automation project demonstrating practical machine learning, anomaly detection, and inventory decision support.

## Project Overview

This project uses real grocery retail sales data from the Kaggle Store Sales dataset to build an FMCG decision-support workflow.

### Features

- Sales and promotion analysis
- Demand forecasting using Random Forest
- Time-based train/test validation
- Forecast evaluation using MAE and RMSE
- Residual-based anomaly detection
- Simulated inventory risk classification
- Reorder quantity recommendations
- Automated management insights
- Interactive Streamlit dashboard

## Model Performance

- Forecast MAE: 18,148 units
- Forecast RMSE: 29,657 units
- Detected anomalies: 17
- Higher-than-expected anomalies: 12
- Lower-than-expected anomalies: 5

## Inventory Simulation

The original dataset does not contain stock-on-hand data, so inventory levels are simulated for demonstration purposes.

The system classifies inventory into:

- High Risk
- Medium Risk
- Low Risk

It also generates simulated reorder recommendations based on forecast demand and stock coverage.

## Business Value

The project demonstrates how AI and automation can help FMCG operations with:

- Demand forecasting
- Unusual demand detection
- Stock-out risk identification
- Replenishment prioritization
- Automated management reporting

## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Matplotlib
- Google Colab
- GitHub

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
