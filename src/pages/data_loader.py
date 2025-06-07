import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

#config
st.set_page_config(
    page_title="Data Loader",
    page_icon="",
    layout="wide",
)

#sidebar Navigation
st.sidebar.title("Menu")
st.sidebar.page_link("main.py", label="Home")
st.sidebar.page_link("pages/data_loader.py", label="Data Loader")

# Title
st.title("Data Loader & EDA Analysis")

# load data
@st.cache_data
def load_data():
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "dataset"))
    sales = pd.read_csv(os.path.join(base_path, "sales_train_validation.csv"))
    calendar = pd.read_csv(os.path.join(base_path, "calendar.csv"))
    prices = pd.read_csv(os.path.join(base_path, "sell_prices.csv"))
    return sales, calendar, prices

with st.spinner("Loading data..."):
    sales, calendar, prices = load_data()
    st.success("Data loaded successfully!")

#Tabs
tab1, tab2, tab3 = st.tabs(["Sales Data", "Calendar Data", "Prices Data"])


for tab in [tab1, tab2, tab3]:
    with tab:

        if tab == tab1:
            st.subheader("Sales Data")
            st.dataframe(sales.head())
            st.write("Number of rows:", sales.shape[0])
            st.write("Number of columns:", sales.shape[1])
            st.write("Columns:", sales.columns.tolist())
            st.write("Data Types:", sales.dtypes.to_frame())

        elif tab == tab2:
            st.subheader("Calendar Data")
            st.dataframe(calendar.head())
            st.write("Number of rows:", calendar.shape[0])
            st.write("Number of columns:", calendar.shape[1])
            st.write("Columns:", calendar.columns.tolist())
            st.write("Data Types:", calendar.dtypes.to_frame())
        
        elif tab == tab3:
            st.subheader("Prices Data")
            st.dataframe(prices.head())
            st.write("Number of rows:", prices.shape[0])
            st.write("Number of columns:", prices.shape[1])
            st.write("Columns:", prices.columns.tolist())
            st.write("Data Types:", prices.dtypes.to_frame())
