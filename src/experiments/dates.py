import csv
from datetime import datetime, timedelta

#Generating list of dates in order to match the output
current_date = datetime.now().date()
start_date = datetime(2018, 1, 1).date()  
dates = [start_date + timedelta(days=i) for i in range((current_date - start_date).days)]

csv_file = 'dates.csv'

with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date'])
    writer.writerows([[date.strftime('%Y-%m-%d')] for date in dates])  

print(f"Dates saved to {csv_file}")
