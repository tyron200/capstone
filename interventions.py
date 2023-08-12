import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('covid_19_data.csv')


data['ObservationDate'] = pd.to_datetime(data['ObservationDate'])


intervention_date = pd.to_datetime('2020-03-15')


pre_intervention_data = data[data['ObservationDate'] < intervention_date]
post_intervention_data = data[data['ObservationDate'] >= intervention_date]


pre_intervention_daily = pre_intervention_data.groupby('ObservationDate')[
    'Confirmed'].sum()
post_intervention_daily = post_intervention_data.groupby('ObservationDate')[
    'Confirmed'].sum()


plt.figure(figsize=(10, 6))
plt.plot(pre_intervention_daily.index,
 pre_intervention_daily.values, label='Pre-Intervention')
plt.plot(post_intervention_daily.index,
 post_intervention_daily.values, label='Post-Intervention')
plt.axvline(x=intervention_date, color='red',
    linestyle='--', label='Intervention Date')
plt.xlabel('Date')
plt.ylabel('Confirmed Cases')
plt.title('Impact of Intervention on Confirmed Cases')
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()
