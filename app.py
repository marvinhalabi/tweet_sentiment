import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
import tweepy
from dotenv import load_dotenv
import nltk
from wordcloud import WordCloud

# Load environment variables
load_dotenv()

# Twitter API credentials
API_KEY = os.getenv('TWITTER_API_KEY')
API_SECRET = os.getenv('TWITTER_API_SECRET')
ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

# Authenticate to Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Function to fetch tweets
def fetch_tweets(query, count=100):
    try:
        tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en", tweet_mode='extended').items(count)
        tweets_list = [[tweet.created_at, tweet.full_text] for tweet in tweets]
        tweets_df = pd.DataFrame(tweets_list, columns=['Date', 'Tweet'])
        return tweets_df
    except Exception as e:
        st.error(f"Error: {e}")
        return None

# Function to preprocess text
def preprocess_text(text):
    tokens = nltk.word_tokenize(text.lower())
    tokens = [token for token in tokens if token not in nltk.corpus.stopwords.words('english')]
    return ' '.join(tokens)

# Function to analyze sentiment
def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

# Main function to run the Streamlit app
def main():
    st.set_page_config(page_title="twitter", layout="wide")
    st.title("Tweet Sentiment Analysis")
    st.write("Analyze the sentiment of tweets based on a search query.")

    query = st.text_input("Enter a search query:")
    tweet_count = st.slider("Number of tweets to fetch:", 50, 500, 100)

    if st.button("Fetch Tweets"):
        with st.spinner("Fetching tweets..."):
            tweets_df = fetch_tweets(query, tweet_count)
            if tweets_df is not None:
                st.write(f"Fetched {tweets_df.shape[0]} tweets.")
                tweets_df['Tweet'] = tweets_df['Tweet'].apply(preprocess_text)
                tweets_df['Sentiment'] = tweets_df['Tweet'].apply(analyze_sentiment)

                st.write("### Sample of fetched tweets:")
                st.write(tweets_df.head())

                st.write("### Sentiment Distribution")
                sentiment_count = tweets_df['Sentiment'].value_counts()
                plt.figure(figsize=(10, 6))
                sns.barplot(x=sentiment_count.index, y=sentiment_count.values, palette="viridis")
                plt.xlabel("Sentiment")
                plt.ylabel("Number of Tweets")
                plt.title("Sentiment Distribution")
                st.pyplot(plt)

                st.write("### Word Cloud of Tweets")
                all_words = ' '.join([text for text in tweets_df['Tweet']])
                wordcloud = WordCloud(width=800, height=400, random_state=21, max_font_size=110).generate(all_words)

                plt.figure(figsize=(10, 6))
                plt.imshow(wordcloud, interpolation="bilinear")
                plt.axis('off')
                st.pyplot(plt)

if __name__ == '__main__':
    main()