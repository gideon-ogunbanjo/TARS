# Importing libraries
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
import pickle

# Loading the tranied model
with open('Model/model.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)

with open('Model/vectorizer.pkl', 'rb') as vectorizer_file:
    loaded_vectorizer = pickle.load(vectorizer_file)

# Streamlit UI
st.set_page_config(
    page_title="TARS",
    initial_sidebar_state="expanded",
    layout="centered"
)

st.title("TARS - Fake News Detection App")
st.write("TARS is a machine learning model that predicts fake news. The model can be used to classify news articles as either real or fake based on the text data in the article.")
text_input = st.text_area("Enter a news article:", "")

if st.button("Predict"):
    if text_input:
        # Preprocesses the input text
        tfidf_text = loaded_vectorizer.transform([text_input])

        # Makes prediction
        prediction = loaded_model.predict(tfidf_text)
        result = "Real" if prediction[0] == 'REAL' else "Fake"

        # Displays result
        st.write(f"The news article is: {result}")
    else:
        st.warning("Please enter a news article for prediction.")
        
st.write("Disclaimer: This model is trained on limited data and might not have access to the latest news.")

link = 'Created by [Gideon Ogunbanjo](https://gideonogunbanjo.netlify.app)'
st.markdown(link, unsafe_allow_html=True)