import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('covid_19_data.csv')


data['ObservationDate'] = pd.to_datetime(data['ObservationDate'])


daily_country_cases = data.groupby(
    ['ObservationDate', 'Country/Region'])['Confirmed'].sum().reset_index()


daily_country_cases['Rolling_Avg'] = daily_country_cases.groupby(
    'Country/Region')['Confirmed'].rolling(window=7).mean().reset_index(drop=True)


hotspots = daily_country_cases[daily_country_cases['Confirmed']
   > daily_country_cases['Rolling_Avg']]


plt.figure(figsize=(10, 6))
for country in hotspots['Country/Region'].unique():
    country_data = hotspots[hotspots['Country/Region'] == country]
    plt.plot(country_data['ObservationDate'],
             country_data['Confirmed'], label=country)
plt.xlabel('Date')
plt.ylabel('Confirmed Cases')
plt.title('Outbreak Hotspots: Countries with Sudden Increases in Cases')
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()
