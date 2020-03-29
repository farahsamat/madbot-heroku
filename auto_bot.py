import tweepy
import random
from twitter_actions import TwitterActions
from src.quotes import Quotes
from src.websites import Websites
from src.covid import CovidUpdates
from os import environ

bbc = 'https://www.bbc.com'
ny_times = 'https://www.nytimes.com/'
the_star = 'https://www.thestar.com.my'
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

confirmed_case = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
death_case = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'


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

        get_quote = Quotes()
        qotd = [get_quote.brainy(),
                get_quote.good_reads(),
                get_quote.good_housekeeping(),
                get_quote.keep_inspiring()]
        random.shuffle(qotd)

        scrape = Websites()
        websites = [scrape.web(abc, 'doctype-article', abc[:-6], 'a', 'abcnews'),
                scrape.web(nine, 'feeds', nine, 'h3', 'ninenews'),
                scrape.web(bbc, 'media-list__item media-list__item--1', bbc, 'a', 'bbcnews'),
                scrape.web(ny_times, 'css-1qiat4j eqveam63', ny_times[:-1], 'h2', 'nytimes'),
                scrape.web(the_star, 'col-sm-3 in-sec-story', the_star, 'h2', 'thestarMY'),
                scrape.web(malaysia_kini, 'jsx-2856008738 titleStoryCard', malaysia_kini[:-1], 'h3', 'malaysiakini'),
                scrape.web(tds,
                           'col u-xs-size12of12 js-trackPostPresentation u-paddingLeft12 u-marginBottom15 u-paddingRight12 u-size4of12',
                           tds, 'h3', 'towardsdatascience'),
                scrape.web(nature, 'app-featured-row__item', nature[:-1], 'h3', 'nature'),
                scrape.web(google_ai, 'post', google_ai, 'a', 'googleAI'),
                scrape.web(tech_crunch, 'content', tech_crunch, 'a', 'techcrunch'),
                scrape.web(the_verge, 'c-entry-box--compact__body', the_verge, 'h2', 'theverge'),
                scrape.web(business_insider, 'col post-description', business_insider, 'a', 'businessinsider'),
                scrape.web(sc_news, 'post-item-river__title___J3spU', sc_news, 'a', 'sciencenews')]
        random.shuffle(websites)

        breaking_news = CovidUpdates()
        confirmed = breaking_news.get_dataframe(confirmed_case)
        death = breaking_news.get_dataframe(death_case)
        mad_bot.tweet_text(breaking_news.generate_text(confirmed, death))

        mad_bot.get_friend_list()
        mad_bot.like_tweets()

        for q, w in zip(qotd, websites):
            mad_bot.tweet_text(q)
            text, url = w
            mad_bot.tweet_with_link(text, url)









