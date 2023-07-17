Hello Major League Hacking!

Here is a twitter API I have written in python since I recently made a project within Swift.

Below is the provided steps of what the code snipet does.

1. The code sets up the necessary credentials for accessing the Twitter API. You need to replace the placeholder values with your actual Twitter API credentials.
2. The get_tweet_sentiment() function takes a tweet as input and performs sentiment analysis on it using TextBlob. It calculates the polarity of the tweet's sentiment and returns a string indicating whether the sentiment is positive, neutral, or negative.
3. The analyze_tweets() function takes a query and a count as input. It uses the Tweepy library to retrieve tweets from Twitter based on the provided query. It then iterates over the retrieved tweets, performs sentiment analysis on each tweet using get_tweet_sentiment(), and prints the tweet along with its sentiment.
4. In the usage example, the query variable represents the search query you want to analyze, such as 'MLH Hacking'. The count variable specifies the number of tweets you want to analyze.
5. Lastly, the analyze_tweets() function is called with the given query and count, which triggers the retrieval and sentiment analysis of tweets. The results are printed to the console.
