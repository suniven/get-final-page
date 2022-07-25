from bs4 import BeautifulSoup
import re
import lxml
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

if __name__ == '__main__':
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    option.add_argument("--window-size=1920,1080")
    option.add_argument("--mute-audio")  # 静音
    browser = webdriver.Chrome(chrome_options=option)
    browser.implicitly_wait(30)
    url = 'https://shopee.co.id/winningstore?af_click_lookback=7d&af_reengagement_window=7d&af_siteid=an_11313850138&af_sub_siteid=product&af_viewthrough_lookback=1d&c=-&is_retargeting=true&pid=affiliates&smtt=0.435961385-1654966833.9&utm_campaign=-&utm_content=product&utm_medium=affiliates&utm_source=an_11313850138&utm_term=7pagpmdof1hh'
    browser.get(url)

    count = len(re.sub(r"[\s\r\n\t]", "", browser.text))

    browser.close()
    browser.quit()
    # with open('./test.html', 'rb') as f:
    #     html = f.read()
    # bs = BeautifulSoup(html, 'lxml')
    # print("iframe: ", len(bs.find_all("iframe")))
    # print("test: ", len(bs.find_all("test")))
    # text = bs.get_text()
    # print("text: ", len(text))
    #
    # text = re.sub(r"[\s\r\n\t]", "", text)
    # print(text)
    # print("text: ", len(text))
    #
    # classes = re.findall(r'class=\"[-_\s\w]+\"', str(html))
    # print(classes[:])
    # print(len(classes))
    #
    # classes = list(set(classes))
    # print(len(classes))
