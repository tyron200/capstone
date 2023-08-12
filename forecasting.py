import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Load the data
data = pd.read_csv('covid_19_data.csv')

# Group by date, calculate the sum of confirmed cases
daily_cases = data.groupby('ObservationDate')['Confirmed'].sum().reset_index()

# Set date as the index
daily_cases.set_index('ObservationDate', inplace=True)

# Fit ARIMA model
model = ARIMA(daily_cases, order=(5, 1, 0))
model_fit = model.fit()

# Forecast future cases
forecast_steps = 30
forecast, stderr, conf_int = model_fit.forecast(steps=forecast_steps)

# Create a line plot
plt.figure(figsize=(10, 6))
plt.plot(daily_cases.index, daily_cases['Confirmed'], label='Observed')
plt.plot(pd.date_range(
    start=daily_cases.index[-1], periods=forecast_steps + 1, freq='D')[1:], forecast, label='Forecast')
plt.fill_between(pd.date_range(start=daily_cases.index[-1], periods=forecast_steps + 1, freq='D')[
                 1:], forecast - 1.96 * stderr, forecast + 1.96 * stderr, color='gray', alpha=0.2)
plt.xlabel('Date')
plt.ylabel('Confirmed Cases')
plt.title('Forecasting Future Confirmed Cases using ARIMA')
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()
