# Importing libraries
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier

# Loading the tranied model
pac = PassiveAggressiveClassifier(max_iter=50)
tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
