import re
import os
import time
import requests
import hashlib
from common.model import Final_Page
from common.timestamp import get_now_timestamp
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from sqlalchemy.sql import and_, asc, desc, or_
from sqlalchemy import Column, String, create_engine, Integer, SmallInteger
from sqlalchemy.orm import sessionmaker

screenshots_save_path = './data/'
sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/landing_page?charset=utf8'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
proxy = '127.0.0.1:1080'
proxies = {
    'http': 'http://' + proxy,
    'https': 'http://' + proxy
}


def visit(url, landing_page, landing_page_md5, a_num, vpn, session):
    try:
        final_page = Final_Page()
        final_page.url = url
        final_page.landing_page = landing_page
        final_page.landing_page_md5 = landing_page_md5
        final_page.type = ''
        final_page.a_num = a_num
        final_page.vpn = vpn
        final_page.domain = landing_page.split('/')[2]

        # browser.get(landing_page)
        #
        # try:
        #     save_name = screenshots_save_path + final_page.landing_page_md5 + '.png'
        #     if not os.path.exists(save_name):
        #         browser.save_screenshot(save_name)
        #         print("截图成功")
        #     else:
        #         print("截图已存在")
        # except BaseException as err_msg:
        #     print("截图失败：%s" % err_msg)
        final_page.create_time = get_now_timestamp()
        session.add(final_page)
        session.commit()
    except Exception as e:
        print("** Error: ", e)


if __name__ == '__main__':
    engine = create_engine(sqlconn, echo=True, max_overflow=8)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    try:
        with open("./final.txt", "r", encoding="UTF8") as f:
            items = f.readlines()
        for item in items:
            print('----------')
            item = item.strip()
            item = item.split('\t')
            url = item[0]
            landing_page = item[1]
            landing_page_md5 = item[2]
            a_num = item[3]
            vpn = item[4]
            rows = session.query(Final_Page).filter(Final_Page.landing_page_md5.like(landing_page_md5),
                                                    and_(Final_Page.url.like(url))).all()
            if rows:
                print("*** Already Visited. ***")
                continue
            visit(url, landing_page, landing_page_md5, a_num, vpn, session)
    except Exception as e:
        print("Error: ", e)
    finally:
        session.close()
