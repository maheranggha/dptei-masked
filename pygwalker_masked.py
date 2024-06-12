from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
import streamlit as st
import pygwalker as pyg

# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Data Explorer",
    layout="wide"
)

st.title("Data Visualization Explorer")

with st.expander("Description:", expanded=True):
    st.markdown("This page is providing you Data Visualization tools of with _sample_ of the DPTEI dataset. There are only 100 records and the Students' ID and name are removed for privacy matters. Here you can drag and drop some features to build some charts. Please, don't refresh the page before you export the chart! Otherwise you will lose your work.")

# Import dataset
df = pd.read_csv("simul_combined_lab.csv")

pyg_app = StreamlitRenderer(df)

pyg_app.explorer()