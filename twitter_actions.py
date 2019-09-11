import tweepy
import textwrap
import random
import re
from src.text_summary import TextSummary
from src.cloud_image import CloudImage
from gensim.summarization import summarize


class TwitterActions:
    def __init__(self, api, username):
        self.api = api
        self.username = username
        return

    def tweet_quote(self, quote):
        try:
            self.api.update_status(quote, tweet_method='extended')
        except tweepy.error.TweepError as e:
            print(quote, e)

    def tweet_news(self, text, link):
        try:
            self.api.update_status(text + ' ' + link, tweet_method='extended')
        except tweepy.error.TweepError as e:
            print(text, e)

    def tweet_lifestyle(self, text, link):
        try:
            self.api.update_status(text + ' ' + link, tweet_method='extended')
        except tweepy.error.TweepError as e:
            print(text, e)

    def tweet_sc_tech(self, text, link):
        try:
            self.api.update_status(text + ' ' + link, tweet_method='extended')
        except tweepy.error.TweepError as e:
            print(text, e)

    def tweet_summary(self, url):
        whole_passage = TextSummary()
        text = whole_passage.page(url)
        text_summary = summarize(text)
        image = CloudImage()
        if len(text_summary) <= 280:
            try:
                self.api.update_status('1/1\n', url + '\n', text_summary, tweet_mode='extended')
            except tweepy.error.TweepError as e:
                print(url, e)
        else:
            text_chunks = textwrap.wrap(text_summary, 275)
            try:
                self.api.update_status(url)
                tweet = self.api.user_timeline(screen_name=self.username, count=1)[0]
                for i in range(len(text_chunks)):
                    self.api.update_status('{}/{}\n'.format(i + 1, len(text_chunks)) + text_chunks[i], tweet.id,
                                           tweet_mode='extended')
                self.api.update_with_media(image.word_cloud(text_summary), tweet.id)
            except tweepy.error.TweepError as e:
                print(e)

    def like_tweets(self):
        friends = [user.screen_name for user in tweepy.Cursor(self.api.friends, screen_name=self.username).items()]
        random.shuffle(friends)
        for friend in friends:
            try:
                for tweet in tweepy.Cursor(self.api.user_timeline, screen_name='@' + friend, exclude_replies=True,
                                           include_rts=False).items(1):
                    self.api.create_favorite(tweet.id)
            except tweepy.error.TweepError as e:
                print(friend, e)

    def view_trend(self):
        trends_result = self.api.trends_place(1)
        trends = [trend["name"] for trend in trends_result[0]["trends"]]
        feeling_lucky = random.choice(trends)
        image = CloudImage()
        text = [tweet.text.replace(feeling_lucky, '') for tweet in tweepy.Cursor(self.api.search, q=feeling_lucky, include_entities=False, result_type='recent', count=100).items() if (not tweet.retweeted) and ('RT @' not in tweet.text)]
        raw_text = ' '.join(text)
        clean_text = re.sub(r"http\S+", "", raw_text) #remove urls
        clean_text = re.sub(r"@\S+", "", clean_text) #remove mentions
        clean_text = re.sub(r"#\S+", "", clean_text) #remove hashtag
        try:
            self.api.update_with_media(image.word_cloud(clean_text), feeling_lucky + " in #wordcloud")
        except tweepy.error.TweepError as e:
            print(e)
