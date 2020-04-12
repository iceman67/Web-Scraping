# https://rekt77.tistory.com/100?category=823783

# Web scraping, web harvesting, or web data extraction is 
# data scraping used for extracting data from websites. 

import urllib.request
import requests
from bs4 import BeautifulSoup
 
print('Beginning file download with urllib2...')
 
url = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=176306'
#req = urllib.request.Request(url)
#res = urllib.request.urlopen(url).read()

response = requests.get(url)
print(response.status_code)
res = response.text

 
soup = BeautifulSoup(res,'html.parser')
soup = soup.find("div",class_="poster")
#img의 경로를 받아온다
imgUrl = soup.find("img")["src"]
 
#urlretrieve는 다운로드 함수
#img.alt는 이미지 대체 텍스트 == 마약왕
urllib.request.urlretrieve(imgUrl, soup.find("img")["alt"]+'.jpg')
