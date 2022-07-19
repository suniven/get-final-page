import re
import os
import time
import requests
import hashlib
import logging
from common.model import Round_2
from common.timestamp import get_now_timestamp
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from sqlalchemy.sql import and_, asc, desc, or_
from sqlalchemy import Column, String, create_engine, Integer, SmallInteger
from sqlalchemy.orm import sessionmaker

sqlconn = "mysql+pymysql://root:1101syw@localhost:3306/landing_page?charset=utf8"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
proxies = {
    'http': 'http://127.0.0.1:1080',
    'https': 'http://127.0.0.1:1080'
}
save_path = "./data/"


def visit(url_in_comment, landing_page_1, browser, session):
    try:
        print("visiting: ", landing_page_1)
        cur_domain = landing_page_1.split('/')[2]
        links = []
        browser.get(landing_page_1)
        a_num = 0
        # 提取所有a标签
        try:
            a_tags = browser.find_elements_by_tag_name('a')
            a_num = len(a_tags)
        except:
            return
        for a_tag in a_tags:
            try:
                link = a_tag.get_attribute('href')
                if 'http' in link:
                    links.append(link)
            except:
                continue
        links = list(set(links))
        for link in links:
            print('link: ', link)
            browser.get(link)
            print("* ", browser.current_url)
            domain = browser.current_url.split('/')[2]
            if domain != cur_domain:
                round_2 = Round_2()
                round_2.url = url_in_comment
                round_2.landing_page_1 = landing_page_1
                round_2.landing_page_2 = browser.current_url
                round_2.landing_page_md5 = hashlib.md5(round_2.landing_page_2.encode('UTF-8')).hexdigest()
                round_2.checked = ''
                round_2.a_num = a_num
                round_2.vpn = vpn
                try:
                    save_name = save_path + round_2.landing_page_md5 + '.png'
                    if not os.path.exists(save_name):
                        browser.save_screenshot(save_name)
                        print("截图成功")
                    else:
                        print("截图已存在")
                except BaseException as err_msg:
                    print("截图失败：%s" % err_msg)
                round_2.create_time = get_now_timestamp()
                session.add(round_2)
                session.commit()
    except Exception as e:
        print("* Error: ", e)


if __name__ == '__main__':
    # # 正常模式
    # browser = webdriver.Chrome()
    # browser.maximize_window()
    # headless模式
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    option.add_argument("--window-size=1920,1080")
    option.add_argument("--mute-audio")  # 静音
    browser = webdriver.Chrome(chrome_options=option)
    browser.implicitly_wait(20)
    engine = create_engine(sqlconn, echo=True, max_overflow=8)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    try:
        with open("url_for round_2.txt", "r", encoding="UTF8") as f:
            items = f.readlines()
        for item in items:
            item = item.strip()
            print('----------')
            url_in_comment = item.split('\t')[0]
            landing_page_1 = item.split('\t')[1]
            rows = session.query(Round_2).filter(Round_2.url.like(url_in_comment),
                                                 and_(Round_2.landing_page_1.like(landing_page_1))).all()
            if rows:
                print("* Already Visited. *")
                continue
            visit(url_in_comment, landing_page_1, browser, session)
            # break  # for test
    except Exception as e:
        print("Error: ", e)
    finally:
        browser.close()
        browser.quit()
        session.close()
