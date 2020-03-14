import requests
import random
from bs4 import BeautifulSoup

goodreads_quotes = 'https://www.goodreads.com/quotes/'
gr_tags = ['philosophy',
        'science',
        'education',
        'inspirational',
        'time',
        'life',
        'wisdom']

brainy_quotes = 'https://www.brainyquote.com/'
bq_tags = ['topics/leadership-quotes',
           'topics/life-quotes',
           'topics/success-quotes',
           'quote_pictures',
           'topics/funny-quotes',
           'authors/lao-tzu-quotes',
           'authors/confucius-quotes']

goodhousekeeping_quotes = 'https://www.goodhousekeeping.com/'
gh_tags = ['life/g5080/life-quotes/',
           'health/wellness/g2401/inspirational-quotes/',
           'life/relationships/g5055/friendship-quotes/',
           'life/parenting/g25412857/family-quotes/',
           'health/wellness/g4894/motivational-fitness-diet-quotes/',
           'life/parenting/g28541976/best-kids-quotes/']

keepinspiring_quotes = 'https://www.keepinspiring.me/'
ki_tags = ['famous-quotes/',
           'education-quotes/',
           'inspiring-space-quotes/',
           '20-positive-attitude-quotes/',
           '20-quotes-to-build-trust/',
           '24-quotes-moving-on-forward-thinking/']

class Quotes:
    try:
        def __init__(self):
            return

        def good_reads(self):
            web_data = BeautifulSoup(requests.get(goodreads_quotes + 'tag/{}'.format(random.choice(gr_tags))).text,
                                     'html.parser').find_all(class_='quoteDetails')
            text = '#goodreads ' + random.choice(web_data).find(class_='quoteText').text.replace('\n', '').strip()
            return text

        def brainy(self):
            web_data = BeautifulSoup(requests.get(brainy_quotes + '{}'.format(random.choice(bq_tags))).text,
                                     'html.parser').find_all(class_='clearfix')
            text_items = [item.text for item in random.choice(web_data).find_all('a')]
            text = '#brainyquote ' + ' - '.join(text_items)
            return text

        def good_housekeeping(self):
            web_data = BeautifulSoup(requests.get(goodhousekeeping_quotes + '{}'.format(random.choice(gh_tags))).text, 'html.parser').find_all(class_='slideshow-slide-content')
            feeling_lucky = random.choice(web_data)
            text_items = feeling_lucky.text.strip().splitlines()
            text = '#goodhousekeeping ' + text_items[-1] + ' - ' + text_items[0]
            return text

        def keep_inspiring(self):
            web_data = BeautifulSoup(requests.get(keepinspiring_quotes + '{}'.format(random.choice(ki_tags))).text, 'html.parser').find_all(class_='author-quotes')
            feeling_lucky = random.choice(web_data)
            text = '#keepinspiringme ' + feeling_lucky.text
            return text

    except IndexError:
        print("Index error")