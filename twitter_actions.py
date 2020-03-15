import tweepy
import random
from src.cloud_image import CloudImage

friends = []

class TwitterActions:
    def __init__(self, api, username):
        self.api = api
        self.username = username
        return

    def get_friend_list(self):
        try:
            for user in tweepy.Cursor(self.api.friends, screen_name=self.username).items():
                friends.append(user.screen_name )
        except tweepy.error.TweepError as e:
            print(e)

    def tweet_text(self, text):
        try:
            self.api.update_status(text, tweet_method='extended')
        except tweepy.error.TweepError as e:
            print(text, e)

    def tweet_with_link(self, text, link):
        try:
            self.api.update_status(text + ' ' + link, tweet_method='extended')
        except tweepy.error.TweepError as e:
            print(text, e)

    def like_tweets(self):
        random.shuffle(friends)
        for friend in friends:
            try:
                for tweet in tweepy.Cursor(self.api.user_timeline, screen_name='@' + friend, exclude_replies=True,
                                           include_rts=False).items(1):
                    self.api.create_favorite(tweet.id)
            except tweepy.error.TweepError as e:
                print(friend, e)



