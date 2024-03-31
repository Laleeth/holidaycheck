import pandas as pd
from textblob import TextBlob

#Reading csv file
df = pd.read_csv('data/1_Extract_info_justin_trudeau_articles.csv')

text_column = 'fields'


def calculate_sentiment(text):
    blob = TextBlob(str(text))
    return blob.sentiment.polarity

df['sentiment_score'] = df[text_column].apply(calculate_sentiment)
output_csv = 'C:/Users/thoma/Desktop/Alpha/2024/Task/src/data/sentiment_Analysis_justin_trudeau_articles.csv'
df.to_csv(output_csv, index=False)

print(f"Sentiment scores saved to {output_csv}")
