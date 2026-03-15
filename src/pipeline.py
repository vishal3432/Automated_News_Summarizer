from scraper.news_scraper import scrape_article
from preprocessing.text_cleaning import clean_text
from ner.ner_extractor import extract_entities
from summarizer.transformer_summarizer import generate_summary

def run_pipeline(url):

    title, article = scrape_article(url)

    cleaned = clean_text(article)

    entities = extract_entities(cleaned)

    summary = generate_summary(cleaned)

    return title, cleaned, entities, summary