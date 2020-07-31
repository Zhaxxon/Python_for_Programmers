import tweepy

key = 'random_key'
secret = 'random_secret'
access_token = 'access_token'
access_secret = 'super_secret'

auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

my_tweets = api.user_timeline()

for tweet in my_tweets:
    print(tweet.text)


api.update_status('I just tweeted using Python')
api.update_with_media(filename, 'I can tweet files with Python')