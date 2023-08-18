# Importing libraries
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier

# Loading the tranied model
pac = PassiveAggressiveClassifier(max_iter=50)
tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)

# Streamlit UI
st.set_page_config(
    page_title="TARS",
    initial_sidebar_state="expanded",
    layout="centered"
)

st.title("TARS - Fake News Detector")
st.header("TARS is a machine learning model that predicts fake news. The model can be used to classify news articles as either real or fake based on the text data in the article.")
text_input = st.text_area("Enter a news article:", "")
