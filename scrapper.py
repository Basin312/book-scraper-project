import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
# url = 'https://books.toscrape.com/'

book_data=[]
for page_number in range(1,51):
    url = f"https://books.toscrape.com/catalogue/page-{page_number}.html"
    response = requests.get(url)
    response.encoding = 'utf-8'

    if response.status_code != 200:
        break

    page_html = response.text

    soup = BeautifulSoup(page_html, 'html.parser')
    books = soup.find_all("article", class_="product_pod")

    print(f"Scraping page {page_number}...")
    for book in books:
        name = book.h3.find("a")['title']
        price = book.find("p", class_="price_color").text[2:]

        book_data.append({
            'Title':name,
            'Price':price
        })
    time.sleep(1)

df = pd.DataFrame(book_data)
df.to_csv('book.csv', index=False)

print("Success! Data saved to book.csv")
print(df.shape)