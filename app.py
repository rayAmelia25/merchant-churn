import streamlit as st

st.set_page_config(
    page_title="Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

pg = st.navigation(
    {
        "Dashboard": [
            st.Page("pages/home.py", title="Visão Geral", icon=":material/home:"),
            st.Page("pages/exploratory_analysis.py", title="EDA", icon=":material/analytics:")
        ]
    },
    position="sidebar"
)

pg.run()