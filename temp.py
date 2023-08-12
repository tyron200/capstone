import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('covid_19_data.csv')

data['ObservationDate'] = pd.to_datetime(data['ObservationDate'])

daily_cases = data.groupby('ObservationDate')['Confirmed'].sum().reset_index()

plt.figure(figsize=(10, 6))
plt.plot(daily_cases['ObservationDate'], daily_cases['Confirmed'], marker='o')
plt.xlabel('Date')
plt.ylabel('Confirmed Cases')
plt.title('Changes in Number of Confirmed Cases Over Time')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()
