import tweepy
import random
import time
from twitter_actions import TwitterActions
from src.quotes import Quotes
from src.websites import Websites
from os import environ

bbc = 'https://www.bbc.com'
ny_times = 'https://www.nytimes.com/'
the_star = 'https://www.thestar.com.my/'
malaysia_kini = 'https://www.malaysiakini.com/'
abc = 'https://www.abc.net.au/news/'
nine = 'https://www.9news.com.au/'
tds = 'https://towardsdatascience.com/'
nature = 'https://www.nature.com/'
google_ai = 'https://ai.googleblog.com/'
the_verge = 'https://www.theverge.com/'
tech_crunch = 'https://techcrunch.com/'
business_insider = 'https://www.businessinsider.com.au/'
sc_news = 'https://www.sciencenews.org/all-stories'

INTERVAL = 60 * 60 * 0.11
MINI_INTERVAL = 60 * 60 * 0.055
MICRO_INTERVAL = 60 * 60 * 0.0099
sleep_time = [INTERVAL, MINI_INTERVAL, MICRO_INTERVAL]

if __name__ == "__main__":
    username = environ["USERNAME"]
    consumer_key = environ['KEY']
    consumer_secret = environ['SECRET']
    access_token = environ['TOKEN']
    access_token_secret = environ['TOKEN_SECRET']
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    mad_bot = TwitterActions(api, username)

    while True:
        mad_bot.get_friend_list()

        get_quote = Quotes()
        link = [get_quote.brainy(),
                get_quote.good_reads(),
                get_quote.good_housekeeping(),
                get_quote.keep_inspiring()]
        random.shuffle(link)

        scrape = Websites()
        news = [scrape.web(abc, 'doctype-article', abc[:-6], 'a', 'abcnews'),
                scrape.web(nine, 'feeds', '', 'h3', 'ninenews'),
                scrape.web(bbc, 'media-list__item media-list__item--1', bbc, 'a', 'bbcnews'),
                scrape.web(ny_times, 'css-1qiat4j eqveam63', ny_times[:-1], 'h2', 'nytimes'),
                scrape.web(the_star, 'col-sm-3 in-sec-story', '', 'h2', 'thestarMY'),
                scrape.web(malaysia_kini, 'jsx-2856008738 titleStoryCard', malaysia_kini[:-1], 'h3', 'malaysiakini'),
                ]
        random.shuffle(news)

        sc_tech = [scrape.web(tds, 'col u-xs-size12of12 js-trackPostPresentation u-paddingLeft12 u-marginBottom15 u-paddingRight12 u-size4of12', '', 'h3', 'towardsdatascience'),
                   scrape.web(nature, 'app-featured-row__item', nature[:-1], 'h3', 'nature'),
                   scrape.web(google_ai, 'post', '', 'a', 'googleAI'),
                   scrape.web(tech_crunch, 'content', '', 'a', 'techcrunch'),
                   scrape.web(the_verge, 'c-entry-box--compact__body', '', 'h2', 'theverge'),
                   scrape.web(business_insider, 'col post-description', '', 'a', 'businessinsider'),
                   scrape.web(sc_news, 'post-item-river__title___J3spU', '', 'a', 'sciencenews')]
        random.shuffle(sc_tech)

        for q, n, a in zip(link, news, sc_tech):
            mad_bot.tweet_quote(q)
            pause = random.choice(sleep_time)*random.randint(1,10)
            print(int(pause), "seconds")
            time.sleep(pause)

            text, url = n
            mad_bot.tweet_news(text, url)
            pause = random.choice(sleep_time)*random.randint(1,10)
            print(int(pause), "seconds")
            time.sleep(pause)

            text, url = a
            mad_bot.tweet_sc_tech(text, url)
            pause = random.choice(sleep_time)*random.randint(1,10)
            print(int(pause), "seconds")
            time.sleep(pause)

        mad_bot.like_tweets()
        pause = random.choice(sleep_time)*random.randint(1,10)
        print(pause, "seconds")
        time.sleep(pause)



