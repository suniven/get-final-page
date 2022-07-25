import pandas as pd
from common.model import Example, HtmlMiddle, Html
from sqlalchemy.sql import and_, asc, desc, or_
from sqlalchemy import Column, String, create_engine, Integer, SmallInteger
from sqlalchemy.orm import sessionmaker
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/landing_page?charset=utf8'


def ele_count(browser, ele):
    try:
        results = browser.find_elements_by_tag_name(ele)
        return len(results)
    except:
        return 0


def extract_features(browser, session, tag, url, landing_page):
    try:
        browser.get(landing_page)

        example = Example()
        example.url = url
        example.landing_page = landing_page
        print("a")
        example.a_count = ele_count(browser, 'a')
        print("img")
        example.img_count = ele_count(browser, 'img')
        print("button")
        example.button_count = ele_count(browser, 'button')
        print("div")
        example.div_count = ele_count(browser, 'div')
        print("iframe")
        example.iframe_count = ele_count(browser, 'iframe')
        example.js_count = ele_count(browser, 'script')
        example.class_count = 0
        example.words_count = 0
        example.tag = tag

        html = browser.page_source
        bs = BeautifulSoup(html, "lxml")
        print("words count")
        example.words_count = len(re.sub(r"[\s\r\n\t]", "", bs.get_text()))
        print("html")
        classes = re.findall(r'class=\"[-_\s\w]+\"', str(html))
        classes = list(set(classes))
        example.class_count = len(classes)

        session.add(example)
        session.commit()
    except Exception as err:
        print("Error: ", err)


if __name__ == '__main__':
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    option.add_argument("--window-size=1920,1080")
    option.add_argument("--mute-audio")  # 静音
    browser = webdriver.Chrome(chrome_options=option)
    browser.implicitly_wait(20)

    engine = create_engine(sqlconn, echo=True, max_overflow=8)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    with open("./final_list.txt", "r", encoding="UTF8") as f:
        items = f.readlines()
    for item in items:
        try:
            item = item.strip()
            print('----------')
            url = item.split('\t')[0]
            landing_page = item.split('\t')[1]
            rows = session.query(Example).filter(Example.url.like(url),
                                                 and_(Example.landing_page.like(landing_page))).all()
            if rows:
                continue
            extract_features(browser, session, 1, url, landing_page)
        except Exception as err:
            print("Err: ", err)

    with open("./middle_list.txt", "r", encoding="UTF8") as f:
        items = f.readlines()
    for item in items:
        try:
            item = item.strip()
            print('----------')
            url = item.split('\t')[0]
            landing_page = item.split('\t')[1]
            rows = session.query(Example).filter(Example.url.like(url),
                                                 and_(Example.landing_page.like(landing_page))).all()
            if rows:
                continue
            extract_features(browser, session, 0, url, landing_page)
        except Exception as err:
            print("Err: ", err)

    session.close()
    browser.close()
    browser.quit()
