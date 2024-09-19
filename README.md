# Tweet Sentiment Analysis 🐦

Welcome to the Tweet Sentiment Analysis project! This Streamlit app lets you analyze the sentiment of tweets based on your search query. It fetches tweets, processes the text, analyzes sentiment, and visualizes the results with charts and word clouds.

## Features 🌟

- **Fetch Tweets**: Get tweets based on your search query.
- **Sentiment Analysis**: Classify tweets as Positive, Neutral, or Negative.
- **Visualizations**: View sentiment distribution and a word cloud of tweet content.

## Installation 🔧

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/marvinhalabi/tweet_sentiment.git
    ```

2. **Navigate to the Project Directory**:

    ```bash
    cd tweet_sentiment
    ```

3. **Create and Activate a Virtual Environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

4. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Set Up Environment Variables**:

    Create a `.env` file in the root directory with your Twitter API credentials:

    ```plaintext
    TWITTER_API_KEY=your_twitter_api_key
    TWITTER_API_SECRET=your_twitter_api_secret
    TWITTER_ACCESS_TOKEN=your_twitter_access_token
    TWITTER_ACCESS_TOKEN_SECRET=your_twitter_access_token_secret
    ```

## Usage 🚀

1. **Run the Streamlit App**:

    ```bash
    streamlit run app.py
    ```

2. **Open the App**: Visit `http://localhost:8501` in your browser.

3. **Enter a Search Query**: Type in what you want to search for and adjust the number of tweets to fetch. Click "Fetch Tweets" to start analyzing!

## Code Overview 📝

- **Fetching Tweets**: Uses Tweepy to get tweets based on your query.
- **Preprocessing**: Cleans up text by removing stopwords.
- **Sentiment Analysis**: Analyzes sentiment with TextBlob.
- **Visualization**: Displays sentiment distribution and generates a word cloud.

## Contributing 🤝

Contributions are welcome! Feel free to open issues or submit pull requests.

