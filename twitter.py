import tweepy
import config
import json
import time

# --- DEGUG --- #
DEBUG = True

if DEBUG:
    open('repliedTo.txt', 'w').write('')  # Clearing 'repliedTo.txt' if in debug mode

# --- SETUP --- #

USERS = set(line.strip() for line in open('users.txt', 'r'))
CONTENT = json.load(open('content.json', 'r', encoding="utf8"))
MOCK = json.load(open('mock.json', 'r', encoding="utf8"))
REPLIED_TO = set(int(line.strip()) for line in open('repliedTo.txt', 'r'))
repliedTo = open('repliedTo.txt', 'a')

# --- Twitter --- #

def setup():
    auth = tweepy.OAuthHandler(config.API_key, config.API_secret_key)
    auth.set_access_token(config.Access_token, config.Access_token_secret)
    return tweepy.API(auth)

def reply(api, tweet, tweet_id):
    api.update_status(tweet, tweet_id)

def getTweets(api, username, n):
    return api.user_timeline(screen_name=username, count=n)

# --- MOCK --- #

class mock:

    def update_status(self, tweet, tweet_id):
        pass

    def user_timeline(self, screen_name, count):
        return [Tweet(tweet) for tweet in MOCK[screen_name]]

class Tweet:
    def __init__(self, tweet):
        self.text = tweet["text"]
        self.id = tweet["id"]
        self.user = User(tweet["user"])

class User:
    def __init__(self, user):
        self.name = user["name"]

# --- HELPER FUNCTIONS --- #

def tweetContains(tweet):
    for text, content in CONTENT.items():
        if str.lower(text) in str.lower(tweet):
            return content
    return None

# --- MAIN --- #

def main():
    if DEBUG:
        api = mock()
    else:
        api = setup()

    while True:
        print(".")
        # Get latest tweets from users
        for user in USERS:
            tweets = getTweets(api, user, 5)

            # Check if tweets match list of content
            for tweet in tweets:
                if tweet.id in REPLIED_TO:
                    continue
                content = tweetContains(tweet.text)
                if content != None:
                    reply(api, content, tweet.id)
                    print('Replied to {} with content {}'.format(tweet.user.name, content))
                    REPLIED_TO.add(tweet.id)
                    repliedTo.write(str(tweet.id) + "\n")
                    continue
        repliedTo.flush()
        time.sleep(60) # 1 min

if __name__ == '__main__':
    main()
