# import requests
# from bs4 import BeautifulSoup
# url = 'https://twitter.com'
# resource = requests.get(url)
# # print(resource.status_code)
#
# soup = BeautifulSoup(resource.text, 'html.parser')
# print(soup)

import requests
from bs4 import BeautifulSoup
twitter_username = 'twitter_username'

url = f'https://twitter.com/{twitter_username}'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    tweets = soup.find_all('p', class_='tweet-text')

    for tweet in tweets:
        print(tweet.get_text())
else:
    print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
