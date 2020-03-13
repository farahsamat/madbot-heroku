import requests
import random
from bs4 import BeautifulSoup

bbcnews = 'https://www.bbc.com'
ny_times = 'https://www.nytimes.com/'
the_star = 'https://www.thestar.com.my/'
malaysia_kini = 'https://www.malaysiakini.com/'
abc = 'https://www.abc.net.au/news/'
nine_news = 'https://www.9news.com.au/'
towards_data_science = 'https://towardsdatascience.com/'
nature = 'https://www.nature.com/'
google_ai = 'https://ai.googleblog.com/'
the_verge = 'https://www.theverge.com/'
tech_crunch = 'https://techcrunch.com/'
business_insider = 'https://www.businessinsider.com.au/'
sc_news = "https://www.sciencenews.org/"


class Websites:
    try:
        def __init__(self):
            return

        def bbc(self):
            web_data = BeautifulSoup(requests.get(bbcnews).text, 'html.parser').find_all(class_='media-list__item media-list__item--1')
            feeling_lucky = random.choice(web_data)
            link = '{}'.format(bbcnews) + feeling_lucky.find('a')['href']
            text = feeling_lucky.find('h3').text.strip()
            return text[:100], link

        def ny_times(self):
            web_data = BeautifulSoup(requests.get(ny_times).text, 'html.parser').find_all(class_='css-1qiat4j eqveam63')
            feeling_lucky = random.choice(web_data)
            link = '{}'.format(ny_times[:-1]) + feeling_lucky.find('a')['href']
            text = feeling_lucky.find('h2').text
            return text[:100], link

        def the_star(self):
            web_data = BeautifulSoup(requests.get(the_star).text, 'html.parser').find_all(class_='col-sm-3 in-sec-story')
            feeling_lucky = random.choice(web_data)
            link = feeling_lucky.find('a')['href']
            text = feeling_lucky.find('h2').text.strip()
            return text[:100], link

        def malaysia_kini(self):
            web_data = BeautifulSoup(requests.get(malaysia_kini).text, 'html.parser').find_all(class_='jsx-2856008738 titleStoryCard')
            feeling_lucky = random.choice(web_data)
            link = '{}'.format(malaysia_kini[:-1]) + feeling_lucky.find('a')['href']
            text = feeling_lucky.find('h3').text
            return text[:100], link

        def abc(self):
            web_data = BeautifulSoup(requests.get(abc).text, 'html.parser').find_all(class_='doctype-article')
            feeling_lucky = random.choice(web_data)
            link = '{}'.format(abc[:-6]) + feeling_lucky.find('a')['href']
            text = feeling_lucky.find('h3').text.strip()
            return text[:100], link

        def nine_news(self):
            web_data = BeautifulSoup(requests.get(nine_news).text, 'html.parser').find_all('article')
            feeling_lucky = random.choice(web_data)
            link = feeling_lucky.find('a')['href']
            text = feeling_lucky.find('h3').text
            return text[:100], link

        def towards_data_science(self):
            web_data = BeautifulSoup(requests.get(towards_data_science).text, 'html.parser').find_all(
                class_='col u-xs-size12of12 js-trackPostPresentation u-paddingLeft12 u-marginBottom15 u-paddingRight12 u-size4of12')
            feeling_lucky = random.choice(web_data)
            link = feeling_lucky.find('a')['href']
            text = feeling_lucky.find('h3').text
            return text[:100], link

        def nature(self):
            web_data = BeautifulSoup(requests.get(nature).text, 'html.parser').find_all(class_='app-featured-row__item')
            feeling_lucky = random.choice(web_data)
            link = '{}'.format(nature[:-1]) + feeling_lucky.find('a')['href']
            text = feeling_lucky.find('h3').text.strip()
            return text[:100], link

        def google_ai(self):
            web_data = BeautifulSoup(requests.get(google_ai).text, 'html.parser').find_all(class_='post')
            feeling_lucky = random.choice(web_data)
            link = feeling_lucky.find('a')['href']
            text = feeling_lucky.find('a').text.strip()
            return text[:100], link

        def the_verge(self):
            web_data = BeautifulSoup(requests.get(the_verge).text, 'html.parser').find_all(
                class_='c-entry-box--compact__body')
            feeling_lucky = random.choice(web_data)
            link = feeling_lucky.find('a')['href']
            text = feeling_lucky.find('h2').text.strip()
            return text[:100], link

        def tech_crunch(self):
            web_data = BeautifulSoup(requests.get(tech_crunch).text, 'html.parser').find_all(class_='content')
            feeling_lucky = random.choice(web_data)
            link = feeling_lucky.find('a')['href']
            text = feeling_lucky.find('a').text.strip()
            return text[:100], link

        def business_insider(self):
            web_data = BeautifulSoup(requests.get(business_insider).text, 'html.parser').find_all(
                class_='col post-description')
            feeling_lucky = random.choice(web_data)
            link = feeling_lucky.find('a')['href']
            text = feeling_lucky.find('h3').text.strip()
            return text[:100], link

        def sc_news(self):
            web_data = BeautifulSoup(requests.get(sc_news).text, 'html.parser').find_all('article')
            feeling_lucky = random.choice(web_data)
            link = feeling_lucky.find('a')['href']
            text = feeling_lucky.find('h2').text.strip()
            return text[:100], link


    except IndexError:
        print("Index error")

    except AttributeError:
        print("Attribute error")


