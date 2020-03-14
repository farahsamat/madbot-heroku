import requests
import random
from bs4 import BeautifulSoup


class Websites:
    try:
        def __init__(self):
            return

        def web(self, url, html_item, link_format, text_item, hashtag):
            web_data = BeautifulSoup(requests.get(url).text, 'html.parser').find_all(class_='{}'.format(html_item))
            feeling_lucky = random.choice(web_data)
            link = '{}'.format(link_format) + feeling_lucky.find('a')['href']
            text = feeling_lucky.find('{}'.format(text_item)).text.strip()
            return '#{} '.format(hashtag) + text[:100], link

    except IndexError:
        print("Index error")

    except AttributeError:
        print("Attribute error")

    except TypeError:
        print("Type error")


