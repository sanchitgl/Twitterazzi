from NLP.func.get_keywords import *
from NLP.func.understand_sentiment import *
import re

def analyse_tweet(tweet):
    entities, keywords = show_ents(tweet)

    return entities, keywords

def get_tweet_sent(tweet):
    tweet = re.sub('@[A-Za-z0–9]+', '', tweet) #Removing @mentions
    tweet = re.sub('#', '', tweet) # Removing '#' hash tag
    tweet = re.sub('RT[\s]+', '', tweet) # Removing RT
    polarity, subjectivity = run_vader(tweet)

    return polarity, subjectivity 