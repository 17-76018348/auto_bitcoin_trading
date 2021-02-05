from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import os 
import copy

def crawling(company_code):
    url = 'https://finance.naver.com/item/news_news.nhn?code=' + str(company_code) + '&page=1'
    source_code = requests.get(url).text
    html = BeautifulSoup(source_code, "lxml")
    tmp_str = ""
    news_total = html.select('.title')

    
    for news in news_total:
        news = news.get_text()
        news = re.sub('\n','',news)
        tmp_str += news

        
    dates = html.select('.date') 
    date_result = [date.get_text() for date in dates]
    print(date_result)
    return tmp_str

news = crawling('005930')
print(news)
#%%
import requests
import json

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

# 사용자 토큰
headers = {
    "Authorization": "Bearer " + '1XyWUhGA4O4bOkPHz3HSDUtau0TQmgHac1CDpAo9c04AAAF3aMGEPg'
}

data = {
    "template_object" : json.dumps({ "object_type" : "text",
                                     "text" : news,
                                     "link" : {
                                                 "web_url" : "www.naver.com"
                                              }
    })
}

response = requests.post(url, headers=headers, data=data)
print(response.status_code)
if response.json().get('result_code') == 0:
    print('메시지를 성공적으로 보냈습니다.')
else:
    print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))
    
    
