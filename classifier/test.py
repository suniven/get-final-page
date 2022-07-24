from bs4 import BeautifulSoup
import re
import lxml

if __name__ == '__main__':
    with open('./test.html', 'rb') as f:
        html = f.read()
    bs = BeautifulSoup(html, 'lxml')
    print("iframe: ", len(bs.find_all("iframe")))
    print("test: ", len(bs.find_all("test")))
    text = bs.get_text()
    print("text: ", len(text))

    text = re.sub(r"[\s\r\n\t]", "", text)
    print(text)
    print("text: ", len(text))

    classes = re.findall(r'class=\"[-_\s\w]+\"', str(html))
    print(classes[:])
    print(len(classes))

    classes = list(set(classes))
    print(len(classes))
