# https://brunch.co.kr/@sukhyun9673/13

import os
import sys
import urllib.request
import json

client_id = "EPUgDWSFhMVrEkAxRnXw"
client_secret = "EIURHTmyuc"
url = "https://openapi.naver.com/v1/datalab/search";
body = "{\"startDate\":\"2019-01-01\",\"endDate\":\"2019-12-31\",\"timeUnit\":\"month\",\"keywordGroups\":[{\"groupName\":\"한글\",\"keywords\":[\"한글\",\"korean\"]},{\"groupName\":\"영어\",\"keywords\":[\"영어\",\"english\"]}],\"device\":\"pc\",\"ages\":[\"1\",\"2\"],\"gender\":\"f\"}";

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")

response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

result = json.loads(response_body)
data = result["results"][0]["data"]

print (data) 
