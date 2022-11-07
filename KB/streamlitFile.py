import requests
import streamlit as st
from streamlit_lottie import st_lottie


def welcome():

    st.set_page_config(page_title="The Exo Project",
                           page_icon=":milky_way:", layout="wide")

    with st.container():
        left, right = st.columns(2)
        with left:                    
            st.subheader("Welcome to our project,")
            st.title("The Exoplanet Classification :milky_way:")
            st.write("In this project we are trying to check wheter an exoplanet is potentially **habitable** or not, and classify it in an habitable class.")

            lottie_system = load_lottie_url(
                "https://assets7.lottiefiles.com/packages/lf20_hvlfn70n.json")
       
        with right:
            st_lottie(lottie_system, height=230, key="star_system")

    st.write("---")

    with st.container():
        st.subheader("Choose one functionality: ")
        st.markdown("* MENU) Classification using Prolog and Inductive Logic Programming")    
        st.markdown("* CLASSIFICATION) Classification using some classic Machine Learning models")  


def load_lottie_url(url):
    req = requests.get(url)
    if req.status_code != 200:
        return None
    return req.json()