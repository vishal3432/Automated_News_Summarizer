import requests
from bs4 import BeautifulSoup

def scrape_article(url):

    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("title").get_text()

    paragraphs = soup.find_all("p")

    article_text = " ".join([p.get_text() for p in paragraphs])

    return title, article_text