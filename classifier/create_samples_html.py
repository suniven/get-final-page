import pandas as pd
from common.model import Example, HtmlMiddle, Html
from sqlalchemy.sql import and_, asc, desc, or_
from sqlalchemy import Column, String, create_engine, Integer, SmallInteger
from sqlalchemy.orm import sessionmaker
import re
from bs4 import BeautifulSoup

sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/landing_page?charset=utf8'


def extract_features(html, session, tag, url, landing_page):
    try:
        example = Example()
        example.url = url
        example.landing_page = landing_page
        example.a_count = 0
        example.img_count = 0
        example.button_count = 0
        example.div_count = 0
        example.iframe_count = 0
        example.class_count = 0
        example.words_count = 0
        example.tag = tag

        bs = BeautifulSoup(html, "lxml")
        example.a_count = len(bs.find_all("a"))
        example.img_count = len(bs.find_all("img"))
        example.button_count = len(bs.find_all("button"))
        example.div_count = len(bs.find_all("div"))
        example.iframe_count = len(bs.find_all("iframe"))
        example.words_count = len(re.sub(r"[\s\r\n\t]", "", bs.get_text()))

        classes = re.findall(r'class=\"[-_\s\w]+\"', str(html))
        classes = list(set(classes))
        example.class_count = len(classes)

        session.add(example)
        session.commit()
    except Exception as err:
        print("Error: ", err)


if __name__ == '__main__':
    engine = create_engine(sqlconn, echo=True, max_overflow=8)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    htmls = session.query(Html).filter().all()
    for html in htmls:
        rows = session.query(Example).filter(Example.url.like(html.url),
                                             and_(Example.landing_page.like(html.landing_page))).all()
        if rows:
            continue
        extract_features(html.html, session, 1, html.url, html.landing_page)

    middle_htmls = session.query(HtmlMiddle).filter().all()
    for middle_html in middle_htmls:
        rows = session.query(Example).filter(Example.url.like(middle_html.url),
                                             and_(Example.landing_page.like(middle_html.landing_page))).all()
        if rows:
            continue
        extract_features(middle_html.html, session, 0, middle_html.url, middle_html.landing_page)

    session.close()