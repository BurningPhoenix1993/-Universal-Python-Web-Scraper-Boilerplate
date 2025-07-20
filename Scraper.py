import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape(url, selector, output='output.csv'):
    resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(resp.content, 'html.parser')
    elements = soup.select(selector)
    data = [el.get_text(strip=True) for el in elements]
    df = pd.DataFrame({'Value': data})
    df.to_csv(output, index=False)
    print(f"Scraped {len(data)} items and saved to {output}")

if __name__ == "__main__":
    url = input("Enter URL: ")
    selector = input("Enter CSS Selector: ")
    output = input("Output filename (e.g. out.csv): ")
    scrape(url, selector, output)
