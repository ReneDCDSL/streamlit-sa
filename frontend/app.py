# frontend/app.py
import streamlit as st
import requests

def predict_sentiment(text):
    backend_url = "http://localhost:8080/predict_sentiment"  # Docker service name
    data = {"text": text}
    response = requests.post(backend_url, json=data)
    result = response.json()
    return result["sentiment"]

st.title("Sentiment Analysis App")

# User input for sentiment analysis
user_input = st.text_area("Enter text for sentiment analysis:")

# Perform sentiment analysis when the user clicks a button
if st.button("Analyze Sentiment"):
    if user_input:
        # Analyze sentiment using the backend
        sentiment = predict_sentiment(user_input)
        st.write("Sentiment:", sentiment)
    else:
        st.warning("Please enter some text for analysis.")
