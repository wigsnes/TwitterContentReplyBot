import tweepy
import config
import json
import time
import random
import jsonpickle

# --- DEGUG --- #
DEBUG = True

if DEBUG:
    open('repliedTo.txt', 'w').write('')  # Clearing 'repliedTo.txt' if in debug mode
    TWEETS = jsonpickle.loads(open('mock/tweetsMock.json', 'r', encoding="utf8").read())
    USERS = jsonpickle.loads(open('mock/usersMock.json', 'r', encoding="utf8").read())
else:
    USERS = set(line.strip() for line in open('data/users.txt', 'r'))

# --- SETUP --- #

CONTENT = json.load(open('data/content.json', 'r', encoding="utf8"))
REPLIED_TO = set(int(line.strip()) for line in open('data/repliedTo.txt', 'r'))
repliedTo = open('data/repliedTo.txt', 'a')


# --- Twitter --- #

def setup():
    auth = tweepy.OAuthHandler(config.API_key, config.API_secret_key)
    auth.set_access_token(config.Access_token, config.Access_token_secret)
    return tweepy.API(auth)


def reply(api, user, tweet, tweet_id):
    api.update_status("@{} {}".format(user, tweet), tweet_id)
    REPLIED_TO.add(tweet_id)
    repliedTo.write(str(tweet_id) + "\n")


def getTweets(api, user, n):
    try:
        return api.user_timeline(screen_name=user, count=n)
    except tweepy.error.RateLimitError:
        print("Rate limit reached. Waiting 15min.")
        time.sleep(60 * 15)  # 15 min


def isProtected(api, user):
    U = api.get_user(user)
    return U.protected


# --- MOCK --- #

class mock:

    def update_status(self, tweet, tweet_id):
        pass

    def user_timeline(self, screen_name, count):
        return [Tweet(tweet, screen_name) for tweet in TWEETS[screen_name]]

    def get_user(self, user):
        return User(user)


class Tweet:
    def __init__(self, tweet, user_name):
        self.text = tweet["text"]
        self.id = random.randint(1000000000, 9999999999)
        self.user = User(user_name)
        self.retweeted = tweet["retweeted"]
        self.created_at = tweet["created_at"]


class User:
    def __init__(self, user_name, protected=False):
        self.name = user_name
        self.protected = protected


# --- HELPER FUNCTIONS --- #

def tweetMatchesContent(tweet):
    matches = list()
    for text, content in CONTENT.items():
        if str.lower(text) in str.lower(tweet):
            matches.append((text, content))
    if len(matches) != 0:
        matches.sort(key=lambda x: len(x[0]), reverse=True)
        return matches[0]
    else:
        return None


# --- MAIN --- #

def main():
    if DEBUG:
        api = mock()
    else:
        api = setup()

    for user in USERS:
        tweets = getTweets(api, user, 5)
        if len(tweets) == 0:
            print(user)
            continue
        ts = time.strftime('%m', time.strptime(tweets[0].created_at,'%Y-%m-%d %H:%M:%S'))
        if int(ts) < 8:
            print(user)

    while True:
        for user in USERS:
            tweets = getTweets(api, user, 5)
            checkTweets(api, user, tweets)
            
        if DEBUG:
            break
        repliedTo.flush()
        time.sleep(60)  # 1 min
        print(".")


def checkTweets(api, user, tweets):
    for tweet in tweets:
        if tweet.id in REPLIED_TO:
            continue
        if tweet.retweeted:
            continue

        content = tweetMatchesContent(tweet.text)
        if content != None:
            reply(api, user, content[1], tweet.id)
            print('---------------------------------------------')
            print('User:\t{}\nTweet:\t{}\nFound:\t{}\nReply:\t{}'.format(tweet.user.name, tweet.text.replace('\n', ''), content[0], content[1]))

if __name__ == '__main__':
    main()
