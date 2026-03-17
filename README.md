## Automated News Summarizer (Transformer + NLP Pipeline)

An end-to-end Machine Learning pipeline that scrapes news articles, processes text, generates summaries using Transformer models, and evaluates performance using ROUGE & METEOR — all visualized through an interactive dashboard.

## Features

1. News Article Scraping (URL-based)

2. Text Cleaning & Preprocessing

3. Named Entity Recognition (NER)

4. Intelligent Text Chunking (for long articles)

5. Transformer-based Summarization

6. Evaluation using ROUGE & METEOR

7. Interactive Dashboard for visualization

## ML Pipeline Architecture
 
News Scraper
      ↓
Text Cleaning
      ↓
NER (spaCy)
      ↓
Chunking
      ↓
Transformer Summarizer
      ↓
Evaluation (ROUGE / METEOR)
      ↓
Dashboard Output

## Project Structure
automated-news-summarizer
│
├── dashboard
│   └── app.py
│
├── src
│   ├── ingestion
│   ├── preprocessing
│   ├── ner
│   ├── summarizer
│   ├── evaluation
│   ├── pipeline
│   └── utils
│
├── requirements.txt
├── README.md
└── .gitignore

## Tech Stack

Python

Streamlit (Dashboard)

spaCy (NER)

BeautifulSoup (Web Scraping)

Hugging Face Transformers (Summarization)

NLTK (METEOR)

Rouge Score


1. Clone Repository
git clone https://github.com/your-username/automated-news-summarizer.git
cd automated-news-summarizer
2.Create Virtual Environment
python -m venv venv
venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
Download spaCy Model
python -m spacy download en_core_web_sm
Run the Application
streamlit run dashboard/app.py

Open in browser:

http://localhost:8501
📊 Dashboard Output

Original Article

Generated Summary

Extracted Entities

ROUGE Score

METEOR Score

 Performance Optimizations
Lightweight Transformer model for faster inference
Chunk-based summarization for long texts
Model caching using Streamlit
Reduced input size for faster processing

 Evaluation Metrics

ROUGE-1 / ROUGE-L → Measures overlap between generated and reference summary

METEOR → Measures semantic similarity

Future Improvements

FastAPI backend for production API

Docker containerization

Parallel summarization for speed

Advanced visualization (charts, graphs)

Deployment (AWS)
