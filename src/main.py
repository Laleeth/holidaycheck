import requests as req
import pandas as pd
from datetime import date, timedelta

def get_articles(query, start_date, api_key):
   
    to_date = date.today() - timedelta(days=1)
    api_url = f'https://content.guardianapis.com/search?q="{query}"&from-date={start_date}&to-date={to_date}&order-by=oldest&api-key={api_key}&type=article&page-size=50&show-fields=body&query-fields=headline'
    response = req.get(api_url).json()

    articles_data = []
    for page_num in range(1, response['response']['pages'] + 1):
        page_response = req.get(f"{api_url}&page={page_num}").json()
        articles_data.extend(page_response['response']['results'])


#Saving dataframe into CSV
    df = pd.DataFrame(articles_data)
    df.to_csv('justin_trudeau_articles.csv', index=False)
    return df

print("Fetching articles...")
df = get_articles(query="Justin Trudeau", start_date="2018-01-01", api_key="c04cc4b8-975c-4ee2-9fc1-334a7200935e")
print("Articles fetched successfully!")
