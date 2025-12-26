import requests
from bs4 import BeautifulSoup
import pandas as pd

book_list = []

# 50 pages scrape kar rahe hain
for page in range(1, 51):
    print(f"Scraping page {page}...")

    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        name = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        availability = book.find("p", class_="instock availability").text.strip()
        rating = book.p["class"][1]

        book_list.append([name, price, rating, availability])

# DataFrame banana
df = pd.DataFrame(
    book_list,
    columns=["Book Name", "Price", "Rating", "Availability"]
)

# CSV save karna
df.to_csv("books_data.csv", index=False)

print("Big dataset scraping completed!")
print("Total rows:", len(df))
