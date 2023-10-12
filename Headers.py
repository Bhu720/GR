import requests
import pandas as pd
from bs4 import BeautifulSoup
url = "https://dict.hinkhoj.com"
r = requests.get(url)
# print(r)
soup = BeautifulSoup(r.text,"lxml")
print(soup)
table = soup.find("table")
headers = table.find_all("th")
print(headers)
titles = []
for i in headers:
    titles = i.text
    titles.append(titles)
    print(titles)
    df  = pd.DataFrame(columns=titles)
    print(df)
