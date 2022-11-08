from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

def run_texblob(tweet):
    tweet_pol = TextBlob(tweet).sentiment.polarity
    tweet_sub = TextBlob(tweet).sentiment.subjectivity

    return tweet_pol, tweet_sub

def run_vader(tweet):
    analyzer = SentimentIntensityAnalyzer()
    sent_dict = analyzer.polarity_scores(tweet)
    return sent_dict['compound'], 'NA'

