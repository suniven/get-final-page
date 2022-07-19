from sqlalchemy import Column, String, create_engine, Integer, SmallInteger
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
