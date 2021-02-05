from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import os 

def crawling(company_code):
    url = 'https://finance.naver.com/item/news_news.nhn?code=' + str(company_code) + '&page=1'
    source_code = requests.get(url).text
    html = BeautifulSoup(source_code, "lxml")
    
    news_total = html.select('.title')
    for news in news_total:
        news = news.get_text()
        news = re.sub('\n','',news)
        print(news)
    dates = html.select('.date') 
    date_result = [date.get_text() for date in dates]
    print(date_result)

crawling('005930')