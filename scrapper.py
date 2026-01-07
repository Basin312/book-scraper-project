import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
# url = 'https://books.toscrape.com/'
# --- SPECIALIST 1: THE FETCHER ---
def get_page_content(url):
    """
    Downloads the page and returns the Soup object.
    Includes basic error handling so the program doesn't crash on a bad page.
    """
    try:
        response = requests.get(url)
        response.encoding = 'utf-8' # Consistency fix
        
        # If the page doesn't load (e.g. 404 or 500 error), tell us
        if response.status_code != 200:
            print(f"Error loading {url} - Status: {response.status_code}")
            return None
            
        return BeautifulSoup(response.text, 'html.parser')
        
    except Exception as e:
        print(f"Connection failed: {e}")
        return None

# --- SPECIALIST 2: THE SORTER ---
def parse_books(soup):
    """
    Takes a Soup object, finds all books, and cleans the data.
    Returns a LIST of dictionaries.
    """
    page_data = []
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        name = book.h3.find("a")['title']
        price = book.find("p", class_="price_color").text[1:] # Clean price

        page_data.append({
            'Title': name,
            'Price': price
        })
    
    return page_data

# --- SPECIALIST 3: THE WAREHOUSE ---
def save_to_csv(data, filename):
    """
    Takes the final list of data and saves it.
    """
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Success! Saved {len(df)} books to {filename}")

# --- THE MANAGER (MAIN LOOP) ---
def main():
    book_data=[]
    for page_number in range(1,51):
        url = f"https://books.toscrape.com/catalogue/page-{page_number}.html"
        soup = get_page_content(url)

        if soup is None:
            continue

        books_on_page = parse_books(soup)

        book_data.extend(books_on_page)

        time.sleep(1)

    save_to_csv(book_data, 'books_refactored.csv')

if __name__ == "__main__":
    main()