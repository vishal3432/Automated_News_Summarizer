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
      --
Text Cleaning
      --
NER (spaCy)
      --
Chunking
      --
Transformer Summarizer
      --
Evaluation (ROUGE / METEOR)
      --
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


