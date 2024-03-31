import pandas as pd
from sqlalchemy import create_engine


df = pd.read_csv('C:/Users/thoma/Desktop/Alpha/2024/Task/src/data/1_Extract_info_justin_trudeau_articles.csv')

print("Your correct until df")

# Connect to MySQL database
engine = create_engine('mysql+mysqlconnector://root:Lalith1509.@localhost/hoho')

# Save DataFrame to MySQL
df.to_sql('table_name', con=engine, if_exists='replace', index=False)
