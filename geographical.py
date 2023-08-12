import geopandas as gpd
import matplotlib.pyplot as plt


data = pd.read_csv('covid_19_data.csv')


country_daily_cases = data.groupby(
    ['Country/Region', 'ObservationDate'])['Confirmed'].sum().reset_index()

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))


world = world.merge(country_daily_cases, how='left',
    left_on='name', right_on='Country/Region')


fig, ax = plt.subplots(1, 1, figsize=(15, 10))
world.boundary.plot(ax=ax)
world.plot(column='Confirmed', ax=ax, legend=True,
  legend_kwds={'label': "Confirmed Cases"})
plt.title('Change in COVID-19 Cases Over Time by Country')
plt.show()
