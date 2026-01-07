# 📚 Book Scraper Project

A Python script that automatically scrapes book data (Title and Price) from [Books to Scrape](http://books.toscrape.com). It iterates through all 50 pages and saves the data to a CSV file.

## 🛠️ Built With

- **Python 3**
- **Requests** (Fetching data)
- **BeautifulSoup4** (Parsing HTML)
- **Pandas** (Saving to CSV)

## 🚀 How to Run

1.  Clone the repository:

    ```bash
    git clone [https://github.com/Basin312/book-scraper-project.git](https://github.com/Basin312/book-scraper-project.git)
    ```

2.  Install the required libraries:

    ```bash
    pip install requests beautifulsoup4 pandas
    ```

3.  Run the script:
    ```bash
    python scraper.py
    ```

## 📂 Output

The script generates a file named `book.csv` containing ~1000 rows of data.
