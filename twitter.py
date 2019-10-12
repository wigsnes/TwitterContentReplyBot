import tweepy
import config
import json
import time
import random
import jsonpickle

# --- DEGUG --- #
DEBUG = True


# --- SETUP --- #
if DEBUG:
    open('repliedTo.txt', 'w').write('')  # Clearing 'repliedTo.txt' if in debug mode
    TWEETS = jsonpickle.loads(open('mock/tweetsMock.json', 'r', encoding="utf8").read())
    USERS = jsonpickle.loads(open('mock/usersMock.json', 'r', encoding="utf8").read())
    REPLIED_TO = set()
else:
    USERS = set(line.strip() for line in open('data/users.txt', 'r'))
    REPLIED_TO = set(int(line.strip()) for line in open('data/repliedTo.txt', 'r'))

repliedTo = open('data/repliedTo.txt', 'a')
CONTENT = json.load(open('data/content.json', 'r', encoding="utf8"))


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
        return api.user_timeline(screen_name=user, count=n, tweet_mode="extended")
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

    def user_timeline(self, screen_name, count, tweet_mode):
        return [Tweet(tweet, screen_name) for tweet in TWEETS[screen_name]]

    def get_user(self, user):
        return User(user)


class Tweet:
    def __init__(self, tweet, user_name):
        self.id = tweet["id"]
        self.text = tweet["full_text"]
        self.user = User(tweet["user"])
        self.created_at = tweet["created_at"]
        self.retweet = tweet["in_reply_to_user_id"] != None
        self.favorite_count = tweet["favorite_count"]
        self.retweet_count = tweet["retweet_count"]


class User:
    def __init__(self, user):
        self.id = getValue("id",user)
        self.name = getValue("name",user)
        self.screen_name = getValue("screen_name",user)
        self.followers_count = getValue("followers_count",user)
        self.verified = getValue("verified",user)
        self.protected = getValue("protected",user)
        self.created_at = getValue("created_at",user)
        self.location = getValue("location",user)
        self.friends_count = getValue("friends_count",user)
        self.listed_count = getValue("listed_count",user)
        self.coordinates = getValue(["status","place", "bounding_box", "coordinates"], user)
        self.country = getValue("country",user)
        self.country_code = getValue("country_code",user)

def getValue(val, elem):
    if isinstance(val, list):
        if len(val) == 1:
            return elem[val]
        if val[0] in elem:
            return getValue(val[1:], elem[val[0]])
        return None

    if val in elem:
        return elem[val]
    return None


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
        if tweet.retweet:
            continue

        content = tweetMatchesContent(tweet.text)
        if content != None:
            reply(api, user, content[1], tweet.id)
            print('---------------------------------------------')
            print('User:\t{}\nTweet:\t{}\nFound:\t{}\nReply:\t{}'.format(tweet.user.name, tweet.text.replace('\n', ''), content[0], content[1]))

if __name__ == '__main__':
    main()
