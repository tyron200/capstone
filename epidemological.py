import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('covid_19_data.csv')


data['Case_Fatality_Rate'] = (data['Deaths'] / data['Confirmed']) * 100
data['Recovery_Rate'] = (data['Recovered'] / data['Confirmed']) * 100


daily_rates = data.groupby('ObservationDate')[
    ['Case_Fatality_Rate', 'Recovery_Rate']].mean().reset_index()


plt.figure(figsize=(10, 6))
plt.plot(daily_rates['ObservationDate'],
     daily_rates['Case_Fatality_Rate'], label='Case Fatality Rate')
plt.plot(daily_rates['ObservationDate'],
     daily_rates['Recovery_Rate'], label='Recovery Rate')
plt.xlabel('Date')
plt.ylabel('Rate (%)')
plt.title('Case Fatality Rate and Recovery Rate Over Time')
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()
