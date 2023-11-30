# backend/app.py
import os
import torch
from transformers import pipeline
from flask import request, jsonify
from fastapi import FastAPI, UploadFile

app = FastAPI()

# Load the pretrained sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

@app.get("/")
def greet():
    return {"message": "bonjour"}


@app.route("/predict_sentiment", methods=["POST"])
def predict_sentiment():
    data = request.get_json()
    text = data.get("text", "")

    # Analyze sentiment using the pretrained model
    result = sentiment_analyzer(text)
    sentiment = result[0]["label"]
    confidence = result[0]["score"]

    return jsonify({"sentiment": sentiment, "confidence": confidence})
