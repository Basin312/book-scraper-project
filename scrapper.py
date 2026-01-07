import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://books.toscrape.com/'

response = requests.get(url)
page_html = response.text

soup = BeautifulSoup(page_html, 'html.parser')
books = soup.find_all("article", class_="product_pod")

book_data=[]
for book in books:
    name = book.h3.find("a")['title']
    price = book.find("p", class_="price_color").text[2:]

    book_data.append({
        'Title':name,
        'Price':price
    })

df = pd.DataFrame(book_data)
df.to_csv('book.csv', index=False)

print("Success! Data saved to books.csv")
print(df.head())