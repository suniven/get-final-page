import re
import os
import time
import requests
import hashlib
from common.model import Round_1, Round_2
from common.timestamp import get_now_timestamp
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from sqlalchemy.sql import and_, asc, desc, or_
from sqlalchemy import Column, String, create_engine, Integer, SmallInteger
from sqlalchemy.orm import sessionmaker

save_path = './data/'
sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/landing_page?charset=utf8'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
proxy = '127.0.0.1:1080'
proxies = {
    'http': 'http://' + proxy,
    'https': 'http://' + proxy
}

if __name__ == '__main__':
    # 正常模式
    browser = webdriver.Chrome()
    browser.maximize_window()
    # # headless模式
    # option = webdriver.ChromeOptions()
    # option.add_argument('--headless')
    # option.add_argument("--window-size=1920,1080")
    # option.add_argument("--mute-audio")  # 静音
    # browser = webdriver.Chrome(chrome_options=option)
    # browser.implicitly_wait(15)
    engine = create_engine(sqlconn, echo=True, max_overflow=8)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    try:
        rows = session.query(Round_1).filter(Round_1.checked.like("revisit")).all()
        if rows:
            for row in rows:
                url = row.landing_page
                print('----------')
                browser.get(url)
                time.sleep(8)
                if browser.current_url == url:
                    time.sleep(12)
                if browser.current_url == url:
                    continue
                id = row.id
                a_num = 0
                try:
                    a_tags = browser.find_elements_by_tag_name('a')
                    a_num = len(a_tags)
                except:
                    print("No a tag.")
                landing_page = browser.current_url
                landing_page_md5 = hashlib.md5(landing_page.encode('UTF-8')).hexdigest()
                res = session.query(Round_1).filter(Round_1.id == id).update({"landing_page": landing_page,
                                                                              "landing_page_md5": landing_page_md5,
                                                                              "a_num": a_num,
                                                                              "checked": "final"},
                                                                             synchronize_session=False)
                session.commit()
                try:
                    save_name = save_path + landing_page_md5 + '.png'
                    if not os.path.exists(save_name):
                        browser.save_screenshot(save_name)
                        print("截图成功")
                    else:
                        print("截图已存在")
                except BaseException as err_msg:
                    print("截图失败：%s" % err_msg)
    except Exception as e:
        print("Error: ", e)
    finally:
        browser.close()
        browser.quit()
        session.close()
