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
    url = 'http://esto.es/defaultsite'
    browser.get(url)

    iframes = browser.find_elements_by_tag_name('iframe')
    print(browser.page_source)
    for iframe in iframes:
        browser.switch_to.frame(iframe)
        print("------------------------")
        print(browser.page_source)
        browser.switch_to.parent_frame()

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
