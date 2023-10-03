import requests, webbrowser

from bs4 import BeautifulSoup

user_input = input("Enter something to search.. ")

print("google....")

google_search = requests.get("https://www.google.com/search?q=",user_input)

soup = BeautifulSoup(google_search.text, "html.parser")

print(soup.prettify())



import requests

# from bs4 import BeautifulSoup
#
# # url = ("https://www.bing.com/search?q=google+translat")
# url = ("https://www.google.com/search?q=apple")
#
# r = requests.get(url)
#
# htmlcontent = r.content
#
# Soup = BeautifulSoup(htmlcontent,'html.parser')
#
# print(Soup)













