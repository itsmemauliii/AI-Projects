# AI-Enhanced Survey & Feedback Analyzer

## 📌 Overview
This project is a **AI-powered survey and feedback analysis platform** that leverages **NLP models** to analyze open-ended responses, perform sentiment analysis, and generate insights.

## 🚀 Features
- **Upload CSV Feedback Data**
- **Sentiment Analysis (Positive/Negative/Neutral)**
- **Keyword Extraction (NLP)**
- **Word Cloud Visualization**
- **Download PDF Reports**

## 📂 Folder Structure
```
📂 AI-Survey-Feedback-Analyzer
│── 📄 app.py               # Main Streamlit app
│── 📄 requirements.txt     # Python dependencies
│── 📄 README.md            # Project description
│── 📂 data                 # Sample datasets
│   ├── sample_feedback.csv # Example feedback data
│── 📂 utils                # Helper functions
│   ├── processing.py       # Data processing functions
│── 📂 models               # Pre-trained models (if applicable)
│── 📂 images               # Screenshots (for README)
│── 📄 .gitignore           # Ignore unnecessary files
│── 📄 config.py            # API keys & configurations
│── 📂 .github/workflows    # GitHub Actions for auto-deploy
│   ├── deploy.yml          # Deployment workflow
```

## 🛠 Setup & Installation
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/AI-Survey-Feedback-Analyzer.git
cd AI-Survey-Feedback-Analyzer
```
### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```
### **3️⃣ Run the App**
```bash
streamlit run app.py
```

## 📌 Sample Code
### **app.py (Streamlit UI)**
```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from utils.processing import analyze_sentiment, extract_keywords

st.title("AI Survey Feedback Analyzer")
uploaded_file = st.file_uploader("Upload CSV Feedback Data", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df['Sentiment'] = df['Feedback'].apply(analyze_sentiment)
    st.write(df)
    
    # Word Cloud
    text = ' '.join(df['Feedback'])
    wordcloud = WordCloud(width=800, height=400).generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot(plt)
```

### **processing.py (NLP Functions)**
```python
from textblob import TextBlob
def analyze_sentiment(text):
    sentiment = TextBlob(text).sentiment.polarity
    return "Positive" if sentiment > 0 else "Negative" if sentiment < 0 else "Neutral"
```

## 🚀 Deployment on Streamlit Cloud
1. Push code to GitHub
2. Go to **[Streamlit Cloud](https://share.streamlit.io)**
3. Connect to GitHub & Deploy!

## 🔥 GitHub Actions Auto-Deploy
`.github/workflows/deploy.yml`
```yaml
name: Deploy to Streamlit

on: [push]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.8
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Deploy
        run: streamlit run app.py
```

## 📌 Next Steps
✅ Improve sentiment analysis using **BERT/GPT**

✅ Add more visualizations (e.g., Pie Charts, Heatmaps)

✅ Integrate **ChatGPT API** for feedback summarization

### **🔗 Connect & Contribute**
📌 **GitHub:** [repo-link](https://github.com/itsmemauliii/AI-Projects)
