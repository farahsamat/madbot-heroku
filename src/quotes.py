import requests
import random
from bs4 import BeautifulSoup

goodreads_quotes = 'https://www.goodreads.com/quotes/'
gr_tags = ['tag/philosophy',
        'tag/science',
        'tag/education',
        'tag/inspirational',
        'tag/time',
        'tag/life',
        'tag/wisdom']

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


def random_quote(url, tags,  html_item):
    web_data = BeautifulSoup(requests.get(url+ '{}'.format(random.choice(tags))).text, 'html.parser').find_all(class_='{}'.format(html_item))
    feeling_lucky = random.choice(web_data)
    return feeling_lucky

class Quotes:
    try:
        def __init__(self):
            return

        def good_reads(self):
            text = '#goodreads ' + random_quote(goodreads_quotes, gr_tags, 'quoteDetails').find(class_='quoteText').text.replace('\n', '').strip()
            return text

        def brainy(self):
            check_link = random_quote(brainy_quotes, bq_tags, 'clearfix').find('a')['href']
            return '#brainyquote ', brainy_quotes[:-1]+check_link

        def good_housekeeping(self):
            text_items = random_quote(goodhousekeeping_quotes, gh_tags, 'slideshow-slide-content').text.strip().splitlines()
            text = '#goodhousekeeping ' + text_items[-1] + ' - ' + text_items[0]
            return text

        def keep_inspiring(self):
            text = '#keepinspiringme ' + random_quote(keepinspiring_quotes, ki_tags, 'author-quotes').text
            return text

    except IndexError:
        print("Index error")