import re
import requests
from bs4 import BeautifulSoup

# REF: http://pythonstudy.xyz/python/article/401-%EC%A0%95%EA%B7%9C-%ED%91%9C%ED%98%84%EC%8B%9D-Regex
frequency = {}
url = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=001&aid=0011343153'
html = requests.get(url)
soup = BeautifulSoup(html.text, features="html5lib")

script_tag = soup.find_all(['script', 'style', 'header', 'footer', 'form'])

for script in script_tag:
    script.extract()

content = soup.get_text('\n', strip=True)
print(content)  

text_string = content.lower()
#match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
match_pattern = re.findall(r'^\w+}', text_string)
 
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
     
frequency_list = frequency.keys()
 
for words in frequency_list:
    print (words, frequency[words])

