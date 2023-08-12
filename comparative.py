import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('covid_19_data.csv')


daily_country_cases = data.groupby(
    ['ObservationDate', 'Country/Region'])['Confirmed'].sum().reset_index()


countries_of_interest = ['China', 'Italy', 'United States', 'India']


plt.figure(figsize=(10, 6))
for country in countries_of_interest:
    country_data = daily_country_cases[daily_country_cases['Country/Region'] == country]
    plt.plot(country_data['ObservationDate'],
             country_data['Confirmed'], label=country)
plt.xlabel('Date')
plt.ylabel('Confirmed Cases')
plt.title('Comparative Analysis of Confirmed Cases by Country')
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()
