import os
import requests
from bs4 import BeautifulSoup

if not os.path.exists('./sha/'):
    os.mkdir('./sha/')

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}

url = 'https://www.bilibili.com/read/cv10037387'

response = requests.get(url, headers = headers).text

soup = BeautifulSoup(response, 'lxml')
i = 0
z = 0
img_list = soup.find_all('img')
del img_list[0:3]
del img_list[0]
for img in img_list :
    img_url = img['data-src']
    i = i + 1
    img_title = i
    print(img_url, img_title)

    try:
        with open('./sha/' + '%d'%img_title + '.jpg', 'wb') as f:
            image = requests.get('http:'+img_url, headers=headers).content
            f.write(image)
            print ('Successful!', img_title)
    except Exception as e:
        print(repr(e))
