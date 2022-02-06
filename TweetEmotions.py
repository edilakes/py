from PersonalData import *
import tweepy
from textblob import TextBlob


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search_tweets('Putin')

sumatorio_sentiment = 0

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    n = public_tweets.count
    sumatorio_sentiment = sumatorio_sentiment + analysis.sentiment.polarity
    print(analysis.sentiment)
mean_polarity = sumatorio_sentiment / n
print ("la media de polaridad es:",mean_polarity)