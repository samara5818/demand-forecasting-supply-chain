import streamlit as st
import time

# config
st.set_page_config(
    page_title = "Demand Forecasting App",
    page_icon = "",
    layout = "wide",
    initial_sidebar_state = "expanded"
)

#sidebar Navigation
st.sidebar.title("Menu")
st.sidebar.page_link("main.py", label="Home")
st.sidebar.page_link("pages/data_loader.py", label="Data Loader")





# Title and Subtitle
st.title("📦 Demand Forecasting & Supply Chain Optimization")
st.subheader("Enhancing inventory and logistics efficiency using Machine Learning")

# Project Overview
st.markdown("""
Welcome to the project dashboard! This tool presents a structured approach to solving real-world demand forecasting and supply chain challenges using the **M5 Forecasting dataset**.

### 🧠 Project Motivation
In retail supply chains, inaccurate demand forecasting often leads to:
- Overstocking and increased holding costs
- Stockouts and missed sales
- Poor customer experience

By applying **machine learning** techniques and **optimization models**, we aim to enhance the accuracy of forecasts and drive better inventory decisions.

### 🎯 Project Objectives
- Forecast daily demand at item-store level using tabular time-series data.
- Visualize trends, seasonality, and anomalies.
- Apply interpretable ML models (e.g., Random Forest, Ridge, XGBoost).
- Optimize inventory plans using MILP (Mixed Integer Linear Programming).

### 🗃️ Dataset Used
- `sales_train_validation.csv` – Daily item-level sales
- `calendar.csv` – Temporal features, holidays, SNAP
- `sell_prices.csv` – Item prices by store and week
- `sales_train_evaluation.csv` – Ground-truth for evaluation

### 📊 What You Can Explore
- Week-wise EDA and insights (`notebooks/`)
- Interactive dashboards (`streamlit_app/`)
- Optimization results and evaluation metrics (`reports/`)

""")

# Optional footer or side image
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Supply_chain_management_diagram.svg/1200px-Supply_chain_management_diagram.svg.png")
