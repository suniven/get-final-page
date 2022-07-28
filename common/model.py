from sqlalchemy import Column, String, Integer, Text, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import mysql

Base = declarative_base()


class Round_1(Base):
    # 表名
    __tablename__ = 'round_1'

    id = Column(mysql.BIGINT, primary_key=True)
    url = Column(String(1200))
    landing_page = Column(String(1200))
    status_code = Column(String(3))
    landing_page_md5 = Column(String(32))
    a_num = Column(Integer)
    vpn = Column(String(20))
    checked = Column(String(50))
    create_time = Column(mysql.BIGINT)


class Final_Page(Base):
    # 表名
    __tablename__ = 'final_page'

    id = Column(mysql.BIGINT, primary_key=True)
    url = Column(String(1200))
    landing_page = Column(String(1200))
    landing_page_md5 = Column(String(32))
    domain = Column(String(50))
    vpn = Column(String(20))
    type = Column(String(100))
    a_num = Column(Integer)
    create_time = Column(mysql.BIGINT)


class Round_2(Base):
    # 表名
    __tablename__ = 'round_2'

    id = Column(mysql.BIGINT, primary_key=True)
    url = Column(String(1200))
    landing_page_1 = Column(String(1200))
    landing_page_2 = Column(String(1200))
    landing_page_md5 = Column(String(32))
    a_num = Column(Integer)
    vpn = Column(String(20))
    checked = Column(String(50))
    create_time = Column(mysql.BIGINT)


class Round_3(Base):
    # 表名
    __tablename__ = 'round_3'

    id = Column(mysql.BIGINT, primary_key=True)
    url = Column(String(1200))
    landing_page_1 = Column(String(1200))
    landing_page_2 = Column(String(1200))
    landing_page_3 = Column(String(1200))
    landing_page_md5 = Column(String(32))
    a_num = Column(Integer)
    vpn = Column(String(20))
    checked = Column(String(50))
    create_time = Column(mysql.BIGINT)


class Html(Base):
    # 表名
    __tablename__ = 'html'

    id = Column(mysql.BIGINT, primary_key=True)
    url = Column(String(1200))
    landing_page = Column(String(1200))
    html = Column(Text)
    create_time = Column(mysql.BIGINT)


class HtmlMiddle(Base):
    # 表名
    __tablename__ = 'html_middle'

    id = Column(mysql.BIGINT, primary_key=True)
    url = Column(String(1200))
    landing_page = Column(String(1200))
    html = Column(Text)
    create_time = Column(mysql.BIGINT)


class Example(Base):
    __tablename__ = 'example'

    id = Column(mysql.BIGINT, primary_key=True)
    url = Column(String(1200))
    landing_page = Column(String(1200))
    a_count = Column(Integer)
    img_count = Column(Integer)
    iframe_count = Column(Integer)
    button_count = Column(Integer)
    div_count = Column(Integer)
    class_count = Column(Integer)
    words_count = Column(Integer)
    js_count = Column(Integer)
    link_count = Column(Integer)
    a_http = Column(Float)
    a_https = Column(Float)
    link_http = Column(Float)
    link_https = Column(Float)
    a_diff = Column(Float)
    link_diff = Column(Float)
    a_hashtag = Column(Float)
    link_hashtag = Column(Float)
    tag = Column(Integer)
