import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import sklearn as sk
import streamlit as st

from utils.m1 import Search

sb.set()
sb.color_palette("Spectral", as_cmap=True)

#Dataset
file_path   = r"C:\Users\evzen\Desktop\IE0005\0_Project\data\perishable_goods_management.csv"
pgm         = pd.read_csv(file_path)
pgm_df      = pd.DataFrame(pgm)

#Variables
data_pt = ["record_id","product_id","product_name","category","store_id","region",
            "supplier_id","transaction_date","expiration_date","shelf_life_days",
            "days_remaining_at_purchase","storage_temp","temp_deviation","base_price",
            "cost_price","initial_quantity","spoilage_sensitivity","day_of_week",
            "is_weekend","month","daily_demand", "demand_variability","temp_abuse_events",
            "distribution_hours","handling_score","packaging_score","spoilage_risk",
            "was_spoiled","quality_grade","days_until_expiry","markdown_applied","discount_pct",
            "selling_price","units_sold","units_wasted","waste_pct","revenue","waste_cost","profit"
            ,"profit_margin_pct","supplier_score","is_promoted"]

#Streamlit page
st.set_page_config(page_title="Statisics", page_icon="📈", layout='wide')

#Statistics
jdf, x, y, df1, df2 = Search.algo1(pgm_df,data_pt) #Set up sidebar to get selected df + var
st.title(f'{x} vs {y}')

with st.container(border=1, height=450, horizontal_alignment="center", vertical_alignment="center",gap="xsmall"):
    st.dataframe(jdf)
    st.write(f'Data Dimensions (Rows: {pgm.shape[0]}, Columns: {pgm.shape[1]})')

c1, c2 = st.columns(2)
en_SP = st.sidebar.checkbox(label="Enable Scatterplot", value=1)
en_H = st.sidebar.checkbox(label="Enable Histogram", value=1)
en_BP = st.sidebar.checkbox(label="Enable Boxplot", value=1)
en_JP = st.sidebar.checkbox(label="Enable Jointplot", value=1)
en_PP = st.sidebar.checkbox(label="Enable Pairplot", value=1)

with c1:
    if en_SP:
        #Display scatterplot
        scatter = st.scatter_chart(data=jdf, x=x, y=y, x_label=f"{x}", y_label=f"{y}")

    if en_H:
        #Display Histogram
        fig_h1 = plt.figure(figsize=(16, 4))
        sb.histplot(data = df1, kde = True)
        st.pyplot(fig_h1)

        fig_h2 = plt.figure(figsize=(16, 4))
        sb.histplot(data = df2, kde = True)
        st.pyplot(fig_h2)

    if en_BP:
        #Display Boxplot
        fig_b1 = plt.figure(figsize=(16, 4))
        sb.boxplot(data = df1, orient = "h")
        st.pyplot(fig_b1)

        fig_b2 = plt.figure(figsize=(16, 4))
        sb.boxplot(data = df2, orient = "h")
        st.pyplot(fig_b2)

with c2:
    if en_JP:
        #Display Jointplot
        jp = sb.jointplot(data=jdf, x=f"{x}", y=f"{y}", kind='reg', height=8)
        st.pyplot(jp)

    if en_PP:
        #Display Pairplot
        pp = sb.pairplot(data=jdf)
        st.pyplot(pp)