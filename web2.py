import requests
from bs4 import BeautifulSoup

user_input = input("Enter something to search.. ")

print("Google Search Results for:", user_input)

search_query = "https://www.google.com/search?q=" + user_input.replace(" ", "+")

google_search = requests.get(search_query)

soup = BeautifulSoup(google_search.text, "html.parser")

print(soup)