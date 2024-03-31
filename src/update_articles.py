

 # For demonstration, let's assume we fetch data for the last 7 days
from main import get_articles
from datetime import date, timedelta

def update_articles(query, start_date, api_key):

   
    start_date = date.today() - timedelta(days=7)
    get_articles(query, start_date, api_key)

# Update articles
print("Checking for updates...")
update_articles(query="Justin Trudeau", start_date="2018-01-01", api_key="c04cc4b8-975c-4ee2-9fc1-334a7200935e")
print("Update checked successfully!")
