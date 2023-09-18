import streamlit as st
import textblob
from textblob import TextBlob
# Set the title and description of your app
st.title("NLP Sentiment Analysis App")
st.write("Enter a text, and I'll analyze its sentiment!")

# Create a text input widget for user input
user_input = st.text_area("Enter a text:")

# Define a function to perform sentiment analysis
def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"

# Check if user input is provided
if user_input:
    # Analyze sentiment when the user submits text
    sentiment = analyze_sentiment(user_input)
    st.write(f"Sentiment: {sentiment}")
