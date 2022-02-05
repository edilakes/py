import tweepy
from textblob import TextBlob

consumer_key = 'vgkuVAgWVKfXVz9A21YELUWIX'
consumer_secret = 'kh6DKLXohp9VPu30e6baucyuV6PnkUExI0H4brp80NfEKIkPBR'

access_token = '193302246-8DSUCCMsgtXPlAWHYLWkoB3k9acfbSXRSuqKOKoJ'
access_token_secret = 'HGiARcG5zEYYW8HHRwr0bZRIsPEcmeZ2F9y3plyrfCOPa'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search_tweets('Rayan')

sumatorio_sentiment = 0

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    n = public_tweets.count
    sumatorio_sentiment = sumatorio_sentiment + analysis.sentiment.polarity
    print(analysis.sentiment)
mean_polarity = sumatorio_sentiment / n
print ("la media de polaridad es:",mean_polarity)