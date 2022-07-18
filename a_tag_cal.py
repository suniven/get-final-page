import pandas as pd
import requests
from bs4 import BeautifulSoup

sqlconn = "mysql+pymysql://root:1101syw@localhost:3306/landing_page?charset=utf8"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
proxies = {
    'http': 'http://127.0.0.1:1080',
    'https': 'http://127.0.0.1:1080'
}

if __name__ == '__main__':
    res = requests.get(url, headers=headers, timeout=8, proxies=proxies)
    html = res.text
    soup = BeautifulSoup(html, 'lxml')
    a_tags = soup.find_all('a')
