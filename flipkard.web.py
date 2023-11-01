import requests

from bs4 import BeautifulSoup
# url = "https://htmldog.com/"

url = 'https://lyricsmint.com'

resource = requests.get(url)
# print(resource.status_code)

soup = BeautifulSoup(resource.text,'html.parser')
# print(soup.title.text)

divTag = soup.select("#carousel div.relative")
# print(len(divTeg))

aTag = [ x.find('a') for x in divTag ]
# print(len(divTag))

imgsrc = [x.find('img')for x in aTag]

srcList = [img['src']for img in imgsrc]

urls = [f"{url}{a['href']}" for a in aTag]
# print(len(srcList))
i=1
for src in srcList:
    temRes = requests.get(src)
    f = open(f'img-{i}.jpg','wb')
    f.write(temRes.content)
    f.close()
    i+=1
