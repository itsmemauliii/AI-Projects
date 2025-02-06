import streamlit as st
import pandas as pd
import torch
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
import openai
import plotly.express as px
from wordcloud import WordCloud
from fpdf import FPDF

# OpenAI GPT API Key
openai.api_key = "YOUR_OPENAI_API_KEY"

# Load pre-trained BERT model for sentiment analysis
model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
sentiment_analyzer = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# Streamlit UI
st.set_page_config(page_title="AI Survey Feedback Analyzer", layout="wide")

st.title("🔍 AI-Powered Survey Feedback Analyzer (Advanced)")

uploaded_file = st.file_uploader("📂 Upload survey feedback (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("📊 **Data Preview:**", df.head())

    # BERT Sentiment Analysis
    def analyze_sentiment(text):
        result = sentiment_analyzer(text[:512])[0]  # BERT has a 512-token limit
        return result['label']

    df['Sentiment'] = df['Feedback'].astype(str).apply(analyze_sentiment)

    # GPT-4 for Feedback Categorization
    def categorize_feedback_gpt(text):
        prompt = f"Categorize this survey feedback: '{text}'. Possible categories: Service, Product, Pricing, Other."
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You analyze and categorize feedback."},
                      {"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']

    df['Category'] = df['Feedback'].astype(str).apply(categorize_feedback_gpt)

    # Display Processed Data
    st.write("📝 **Processed Feedback:**", df[['Feedback', 'Category', 'Sentiment']])

    # Word Cloud
    text = " ".join(df['Feedback'].astype(str))
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    st.image(wordcloud.to_array(), caption="Feedback Word Cloud")

    # Sentiment Distribution
    fig_sentiment = px.histogram(df, x="Sentiment", title="Sentiment Analysis", color="Sentiment")
    st.plotly_chart(fig_sentiment)

    # Category Distribution
    fig_category = px.histogram(df, x="Category", title="Feedback Categories", color="Category")
    st.plotly_chart(fig_category)

    # Download Processed Data
    def generate_report():
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="AI Survey Feedback Report", ln=True, align='C')

        for i, row in df.iterrows():
            pdf.multi_cell(0, 10, f"Feedback: {row['Feedback']}\nCategory: {row['Category']}\nSentiment: {row['Sentiment']}\n")
        
        pdf.output("survey_report.pdf")
        return "survey_report.pdf"

    if st.button("📥 Download Report (PDF)"):
        report_path = generate_report()
        with open(report_path, "rb") as file:
            st.download_button("Download PDF Report", file, "survey_report.pdf", "application/pdf")

