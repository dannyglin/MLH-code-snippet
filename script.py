import tweepy
from textblob import TextBlob

# Set up Twitter API credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def get_tweet_sentiment(tweet):
    analysis = TextBlob(tweet)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return 'Positive'
    elif polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

def analyze_tweets(query, count):
    tweets = tweepy.Cursor(api.search, q=query, lang='en').items(count)

    for tweet in tweets:
        print(f'Tweet: {tweet.text}')
        sentiment = get_tweet_sentiment(tweet.text)
        print(f'Sentiment: {sentiment}\n')

# Usage example
query = 'MLH Hacking'
count = 10
analyze_tweets(query, count)