[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://twitterazzi.streamlit.app/)
# Twitterazzi : See what your Favourite Influencers are tweeting about!

Twitterazzi is an app that allows users to get an overview of the topics a particular twitter user has tweeted about in the past month. 

It retrieves tweets of the provided user id from twitter api and returns entities and keywrods found within the tweets. Which can then be used to filter out the tweets that contained any of the words.

1. Input a valid Twitter ID eg.- 'billgates': 
<img src="https://user-images.githubusercontent.com/105559691/171844916-9e138a27-ed5a-4d3e-8e04-1c95a343f5c9.png" width="700"/>
2. Output in the form of word cloud:
<img src="https://user-images.githubusercontent.com/105559691/171841269-b8cb529c-7098-4693-81ba-517e128f675a.png" width="700"/>

3. Choose and filter tweets on respective entities found - Mentions, Organizations & Locations:

<img src="https://user-images.githubusercontent.com/105559691/171841482-ec800ccd-83a6-475a-89c0-7a18fc57cf24.png" width="700"/>

4. Find User's overall sentiment and filter tweets accordingly. The app uses Vader's Sentiment Analyzer for detecting the polarity in tweets.
<img src="https://user-images.githubusercontent.com/105559691/200685278-b41965bb-7e50-4190-9e59-06a69774e403.png" width="700"/>


5. Choose and filter tweets (in a chronological order) on any of the keywords found:
<img src="https://user-images.githubusercontent.com/105559691/171842542-4cc9fb11-e02c-4569-b0a0-1dc3e2d4af55.png" width="600"/>
<img src="https://user-images.githubusercontent.com/105559691/171842850-a25c6cc1-f644-4233-ab84-24431464af85.png" width="600"/>
