import tweepy
import config
import json

def getUserInfo(api, user):
    user = api.get_user(user)
 
    print('Name: ' + user.name)
    print('Location: ' + user.location)
    print('Friends: ' + str(user.friends_count))

def setup():
    auth = tweepy.OAuthHandler(config.API_key, config.API_secret_key)
    auth.set_access_token(config.Access_token, config.Access_token_secret)

    return tweepy.API(auth)

def tweet(api, tweet):
    api.update_status(tweet)

def reply(api, tweet, tweet_id):
    api.update_status(tweet, tweet_id)

def getTweets(api, username, n):
    return api.user_timeline(screen_name=username, count=n)

contents = [
    {"text":"Was A Good Day", "content":"https://www.youtube.com/watch?v=h4UqMyldS7Q"}
]
def tweetContains(tweet):
    for elem in contents:
        if str.lower(elem["text"]) in str.lower(tweet):
            return elem["content"]
    return None
###########################################################################

def main():
    api = setup()
    # Get latest tweets from user
    user = "AlphaBetaWhisky"
    tweets = getTweets(api, user, 5)

    # Check if tweets match list of content
    for tweet in tweets:
        content = tweetContains(tweet.text)
        if content != None:
            reply(api, content, tweet.id)
            print("Replied to %s with content %s".format(tweet.user.name, content))

if __name__ == "__main__":
    main()