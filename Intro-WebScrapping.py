from bs4 import BeautifulSoup
import requests

website_address = "http://quotes.toscrape.com"
result = requests.get(website_address, verify=False)

soup = BeautifulSoup(result.text, "html.parser")
# print(soup.prettify())

quotes = soup.findAll("div", {"class": "quote"})
# print(quotes)
i = 0
for quote in quotes:
    quotation = quote.find("span", {"class": "text"}).text
    author = quote.find("small", {"class": "author"}).text
    tags = quote.find("div", {"class": "tags"})
    tags_list = []
    all_values = {}

    for tag in tags.find_all('a'):
        tags_list.append(tag.text)

    all_values[i] = {
        'Quote' : quotation,
        'Author' : author,
        'Tags' : tags_list
    }
    i = i+1

    print(all_values)
