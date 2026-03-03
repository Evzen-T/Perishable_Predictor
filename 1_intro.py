import streamlit as st

st.set_page_config(page_title='Introduction', page_icon="🏠", layout='wide')
st.title('Perishable Goods Predictor', text_alignment='center')

#Thumbnail
with st.container(border=0, horizontal_alignment="center", vertical_alignment="center",gap="xsmall"):
    img0    = r"C:\Users\evzen\Desktop\IE0005\0_Project\assets\dataset-cover.png"
    st.image(img0, caption='From Kaggle')

    #Link to dataset
    label_0 = 'Perishable Goods Dataset'
    kaggle_link = "https://www.kaggle.com/datasets/likithagedipudi/perishable-goods-management"
    st.page_link(kaggle_link, label=label_0, icon="🍎")

st.divider(width="stretch")
c1, c2 = st.columns([3,1])
with c1:
    st.subheader("Aim of this project",text_alignment="justify")
    st.markdown("""
                - Aid companies to better manage their products
                - Forecast demand
                - Supplier's reliability
                """,text_alignment="justify")

with c2:
    st.subheader("Credits",text_alignment="justify")
    st.markdown("""
                - Mak Chun Siang
                - Tan Evzen
                - Dylan Chrysander
                - Shawn Peh
                """,
                text_alignment="justify")