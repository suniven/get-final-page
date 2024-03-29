import os
import requests
import hashlib
import time
from common.model import Html
from common.timestamp import get_now_timestamp
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from sqlalchemy.sql import and_, asc, desc, or_
from sqlalchemy import Column, String, create_engine, Integer, SmallInteger
from sqlalchemy.orm import sessionmaker

sqlconn = "mysql+pymysql://root:1101syw@localhost:3306/landing_page?charset=utf8mb4"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}
proxies = {
    'http': 'http://127.0.0.1:1080',
    'https': 'http://127.0.0.1:1080'
}
save_path = "./data/"
vpn = ''


def get_iframe_content(browser):
    iframe_content = ''
    try:
        iframes = browser.find_elements_by_tag_name('iframe')
    except:
        return iframe_content
    # print(browser.page_source)
    for iframe in iframes:
        browser.switch_to.frame(iframe)
        # print("------------------------")
        iframe_content += browser.page_source
        iframe_content += get_iframe_content(browser)
        browser.switch_to.parent_frame()

    return iframe_content


if __name__ == '__main__':
    # browser = webdriver.Chrome()
    # browser.maximize_window()
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    option.add_argument("--window-size=1920,1080")
    option.add_argument("--mute-audio")  # 静音
    browser = webdriver.Chrome(chrome_options=option)
    browser.implicitly_wait(30)
    engine = create_engine(sqlconn, echo=True, max_overflow=8)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    try:
        with open("./final_list.txt", "r", encoding="UTF8") as f:
            items = f.readlines()
        for item in items:
            try:
                item = item.strip()
                print('----------')
                url = item.split('\t')[0]
                landing_page = item.split('\t')[1]

                rows = session.query(Html).filter(Html.landing_page.like(landing_page)).all()
                if rows:
                    continue

                browser.get(landing_page)
                content = browser.page_source

                # # 寻找iframe中的内容
                # try:
                #     content += get_iframe_content(browser)
                # except Exception as err:
                #     print("Iframe Error: ", err)

                html = Html()
                html.url = url
                html.landing_page = landing_page
                html.html = content
                html.create_time = get_now_timestamp()
                session.add(html)
                session.commit()
            except Exception as e:
                print("request error: ", e)
    except Exception as e:
        print("Error: ", e)
    finally:
        session.close()
        browser.close()
        browser.quit()
