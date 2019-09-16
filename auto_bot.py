import tweepy
import os
import random
import time
from twitter_actions import TwitterActions
from src.quotes import Quotes
from src.websites import Websites
from os import environ


os.system('cls' if os.name == 'nt' else 'clear')
INTERVAL = 60 * 60 * 1
MINI_INTERVAL = 60 * 60 * 0.1
MICRO_INTERVAL = 60 * 60 * 0.01
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
        get_quote = Quotes()
        link = [get_quote.brainy(),
                get_quote.good_reads(),
                get_quote.good_housekeeping(),
                get_quote.keep_inspiring()]
        random.shuffle(link)

        scrape = Websites()
        news = [scrape.ny_times(),
                scrape.nine_news(),
                scrape.the_star(),
                scrape.abc(),
                scrape.bbc(),
                scrape.malaysia_kini(),
                scrape.song_of_style(),
                scrape.bag_snob(),
                scrape.sc_news(),
                scrape.the_verge()]
        random.shuffle(news)

        blogs = [scrape.towards_data_science(),
                 scrape.nature(),
                 scrape.google_ai(),
                 scrape.tech_crunch()]
        random.shuffle(blogs)
        _, url = random.choice(blogs) #for summary

        for q, n, b in zip(link, news, blogs):
            mad_bot.tweet_quote(q)
            pause = random.choice(sleep_time)
            print(int(pause), "seconds")
            time.sleep(pause)
            text, url = n
            mad_bot.tweet_news(text, url)
            pause = random.choice(sleep_time)
            print(int(pause), "seconds")
            time.sleep(pause)
            text, url = b
            mad_bot.tweet_sc_tech(text, url)
            pause = random.choice(sleep_time)
            print(int(pause), "seconds")
            time.sleep(pause)

        mad_bot.like_tweets_and_RT()
        pause = random.choice(sleep_time)
        print(pause, "seconds")
        time.sleep(pause)

        mad_bot.tweet_summary(url)
        pause = random.choice(sleep_time)
        print(pause, "seconds")
        time.sleep(pause)
