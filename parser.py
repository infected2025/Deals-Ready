import requests
from bs4 import BeautifulSoup
import pandas as pd

def parse_manomano(keyword="bosch"):
    url = f"https://www.manomano.de/suche?text={keyword}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    products = []
    for item in soup.select("article[data-testid='search-product-card']")[:10]:
        title_tag = item.select_one("h2, h3")
        price_tag = item.select_one("[data-testid='price']")
        link_tag = item.select_one("a")

        if title_tag and price_tag and link_tag:
            title = title_tag.text.strip()
            price = price_tag.text.strip()
            link = "https://www.manomano.de" + link_tag.get("href")
            products.append({
                "Название": title,
                "Цена": price,
                "Ссылка": link
            })

    return pd.DataFrame(products)
