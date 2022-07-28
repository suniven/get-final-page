import pandas as pd
from common.model import Example, HtmlMiddle, Html
from sqlalchemy.sql import and_, asc, desc, or_
from sqlalchemy import Column, String, create_engine, Integer, SmallInteger
from sqlalchemy.orm import sessionmaker
import re
from bs4 import BeautifulSoup

sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/landing_page?charset=utf8'


def extract_features(html, session, tag, url, landing_page):
    # try:
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
    example.js_count = 0
    example.link_count = 0
    example.a_http = 0
    example.a_https = 0
    example.a_hashtag = 0
    example.link_http = 0
    example.link_https = 0
    example.link_hashtag = 0
    example.a_diff = 0
    example.link_diff = 0
    example.tag = tag

    bs = BeautifulSoup(html, "html.parser")  # lxml对html格式限制比较严格，不适合用，因为爬取iframe的时候很草率

    current_domain = landing_page.split('/')[2]

    a_tags = bs.find_all("a")
    example.a_count = len(a_tags)
    if example.a_count > 0:
        a_http = 0
        a_https = 0
        a_hashtag = 0
        a_diff = 0
        for a_tag in a_tags:
            href = a_tag.get("href")
            if href:
                if href == "#":
                    a_hashtag += 1
                elif "javascript:void" in href:
                    a_hashtag += 1
                elif href.startswith('/'):
                    # print(href)
                    if "https" in landing_page:
                        a_https += 1
                    else:
                        a_http += 1
                elif "http" in href:
                    if href.split('/')[2] != current_domain:
                        a_diff += 1
                    if "https" in href:
                        a_https += 1
                    else:
                        a_http += 1
            else:
                a_hashtag += 1
        example.a_http = a_http / example.a_count if a_http > 0 else 0
        example.a_https = a_https / example.a_count if a_https > 0 else 0
        example.a_hashtag = a_hashtag / example.a_count if a_hashtag > 0 else 0
        example.a_diff = a_diff / example.a_count if a_diff > 0 else 0

    link_tags = bs.find_all("link")
    example.link_count = len(link_tags)
    if example.link_count > 0:
        link_http = 0
        link_https = 0
        link_hashtag = 0
        link_diff = 0
        for link_tag in link_tags:
            href = link_tag.get("href")
            if href:
                if href == "#":
                    link_hashtag += 1
                elif "javascript:void" in href:
                    link_hashtag += 1
                elif href.startswith('/'):
                    if "https" in landing_page:
                        link_https += 1
                    else:
                        link_http += 1
                elif "http" in href:
                    if href.split('/')[2] != current_domain:
                        link_diff += 1
                    if "https://" in href:
                        link_https += 1
                    else:
                        link_http += 1
            else:
                link_hashtag += 1
        example.link_http = link_http / example.link_count if link_http > 0 else 0
        example.link_https = link_https / example.link_count if link_https > 0 else 0
        example.link_hashtag = link_hashtag / example.link_count if link_hashtag > 0 else 0
        example.link_diff = link_diff / example.link_count if link_diff > 0 else 0

    example.img_count = len(bs.find_all("img"))
    example.button_count = len(bs.find_all("button"))
    example.div_count = len(bs.find_all("div"))
    example.iframe_count = len(bs.find_all("iframe"))
    example.js_count = len(bs.find_all("script"))

    example.words_count = len(re.sub(r"[\s\r\n\t]", "", bs.get_text()))

    classes = re.findall(r'class=\"[-_\s\w]+\"', str(html))
    classes = list(set(classes))
    example.class_count = len(classes)

    session.add(example)
    session.commit()
    # except Exception as err:
    #     print("Error: ", err)


if __name__ == '__main__':
    engine = create_engine(sqlconn, echo=True, max_overflow=8)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    htmls = session.query(Html).filter().all()
    for index, html in enumerate(htmls, 1):
        rows = session.query(Example).filter(Example.url.like(html.url),
                                             and_(Example.landing_page.like(html.landing_page))).all()
        if rows:
            print("{0}已存在".format(index))
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
