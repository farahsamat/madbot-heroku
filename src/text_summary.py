import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver

phantomJS_path = os.path.abspath('src/phantomjs')


class TextSummary:
    def __init__(self):
        return

    def page(self, url):
        if 'googleblog' in url:
            driver = webdriver.PhantomJS(executable_path=phantomJS_path)
            driver.get(url)
            results = driver.find_element_by_xpath(".//html")
            whole_text = results.text.strip()
            return whole_text

        else:
            paragraph = [p.getText() for p in BeautifulSoup(requests.get(url).text, 'html.parser').find_all('p')]
            whole_text = ' '.join(paragraph)
            return whole_text




