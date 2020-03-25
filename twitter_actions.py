import tweepy
import random
import time

friends = []

INTERVAL = 60 * 60 * 0.11
MINI_INTERVAL = 60 * 60 * 0.055
MICRO_INTERVAL = 60 * 60 * 0.0099
sleep_time = [INTERVAL, MINI_INTERVAL, MICRO_INTERVAL]

def time_out():
    pause = random.choice(sleep_time) * random.randint(1, 10)
    sleep_text = ["BRB", "Later, alligator!", "See u in a bit", "Will be back in approximately {} mins".format(round(pause/60))]
    print(pause, 'seconds')
    if pause > 1799:
        return random.choice(sleep_text), time.sleep(pause)
    else:
        return '', time.sleep(pause)

class TwitterActions:
    def __init__(self, api, username):
        self.api = api
        self.username = username
        return

    def get_friend_list(self):
        try:
            for user in tweepy.Cursor(self.api.friends, screen_name=self.username).items():
                friends.append(user.screen_name )
            t, s = time_out()
            if len(t) != 0:
                self.api.update_status(t, tweet_method='extended')
        except tweepy.error.TweepError as e:
            print(e)

    def tweet_text(self, text):
        try:
            self.api.update_status(text, tweet_method='extended')
            t, s = time_out()
            if len(t) != 0:
                self.api.update_status(t, tweet_method='extended')
        except tweepy.error.TweepError as e:
            print(text, e)

    def tweet_with_link(self, text, link):
        try:
            self.api.update_status(text + ' ' + link, tweet_method='extended')
            t, s = time_out()
            if len(t) != 0:
                self.api.update_status(t, tweet_method='extended')
        except tweepy.error.TweepError as e:
            print(text, e)

    def like_tweets(self):
        random.shuffle(friends)
        for friend in friends:
            try:
                for tweet in tweepy.Cursor(self.api.user_timeline, screen_name='@' + friend, exclude_replies=True,
                                           include_rts=False).items(1):
                    self.api.create_favorite(tweet.id)
                t, s = time_out()
                if len(t) != 0:
                    self.api.update_status(t, tweet_method='extended')
            except tweepy.error.TweepError as e:
                print(friend, e)



