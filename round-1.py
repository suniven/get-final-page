import os
import requests
import hashlib
from common.model import Round_1
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
vpn = '香港'


def visit(url, browser, session):
    try:
        round_1 = Round_1()
        round_1.url = url
        round_1.vpn = vpn
        round_1.status_code = ''
        round_1.landing_page = ''
        round_1.landing_page_md5 = ''
        round_1.checked = ''
        round_1.a_num = 0
        res = requests.get(url, headers=headers, timeout=8, proxies=proxies)
        print("Visiting ", url)
        print("Status Code: %s" % res.status_code)

        round_1.status_code = res.status_code
        if res.status_code != 200:
            print("响应失败")

        else:
            browser.get(url)
            try:
                round_1.a_num = len(browser.find_elements_by_tag_name('a'))
            except:
                print("No a tags.")
            round_1.landing_page = browser.current_url  # 可能有多个landing page
            round_1.landing_page_md5 = hashlib.md5(round_1.landing_page.encode('UTF-8')).hexdigest()

            domain = browser.current_url.split('/')[2]
            query = "%" + domain + "%"

            rows = session.query(Round_1).filter(Round_1.landing_page.like(query),
                                                 and_(Round_1.url.like(url))).all()
            if rows:
                print("* Already Visited. *")
                return

            try:
                save_name = save_path + round_1.landing_page_md5 + '.png'
                if not os.path.exists(save_name):
                    browser.save_screenshot(save_name)
                    print("截图成功")
                else:
                    print("截图已存在")
            except BaseException as err_msg:
                print("截图失败：%s" % err_msg)
        round_1.create_time = get_now_timestamp()
        session.add(round_1)
        session.commit()
    except Exception as e:
        print("Error: ", e)


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
    browser.implicitly_wait(10)
    engine = create_engine(sqlconn, echo=True, max_overflow=8)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    try:
        with open("./url_in_comments.txt", "r", encoding="UTF8") as f:
            urls = f.readlines()
        for url in urls:
            url = url.strip()
            print('----------')
            if 'http' not in url:
                url = 'http://' + url
            visit(url, browser, session)
    except Exception as e:
        print("Error: ", e)
    finally:
        browser.close()
        browser.quit()
        session.close()
