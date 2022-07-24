import os
import requests
from common.model import HtmlMiddle
from common.timestamp import get_now_timestamp
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
vpn = '日本'

if __name__ == '__main__':
    engine = create_engine(sqlconn, echo=True, max_overflow=8)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    try:
        with open("./middle_list.txt", "r", encoding="UTF8") as f:
            items = f.readlines()
        for item in items:
            try:
                item = item.strip()
                print('----------')
                url = item.split('\t')[0]
                landing_page = item.split('\t')[1]

                rows = session.query(HtmlMiddle).filter(HtmlMiddle.landing_page.like(landing_page)).all()
                if rows:
                    continue
                res = requests.get(landing_page, headers=headers, timeout=8, proxies=proxies)
                print("Visiting ", landing_page)
                print("Status Code: %s" % res.status_code)
                if res.status_code != 200:
                    print("响应失败")
                else:
                    html = HtmlMiddle()
                    html.url = url
                    html.landing_page = landing_page
                    html.html = res.text
                    html.vpn = vpn
                    html.create_time = get_now_timestamp()
                    session.add(html)
                    session.commit()
            except Exception as e:
                print("request error: ", e)
    except Exception as e:
        print("Error: ", e)
    finally:
        session.close()
