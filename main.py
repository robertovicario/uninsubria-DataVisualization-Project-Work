import pandas as pd
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates
from scipy.stats import linregress

# Load and process data
bitcoin_df = pd.read_csv('data/btc_prices_2021.csv', parse_dates=['Timestamp'])

start_date = '2021-05-01'
end_date = '2021-05-31'
filtered_df = bitcoin_df.set_index('Timestamp').loc[start_date:end_date]

resampled_df = filtered_df.resample('D').agg({'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last', 'Volume': 'sum'}).dropna()
highest_value = resampled_df['High'].max()
lowest_value = resampled_df['Low'].min()

resampled_df['Date'] = resampled_df.index.map(mdates.date2num)
ohlc_data = resampled_df[['Date', 'Open', 'High', 'Low', 'Close']].reset_index(drop=True).values

# Perform linear regression on the closing prices
dates = resampled_df['Date']
closing_prices = resampled_df['Close']
slope, intercept, _, _, _ = linregress(dates, closing_prices)
regression_line = slope * dates + intercept

# Plot candlestick chart with regression line
fig, ax = plt.subplots(figsize=(10, 6))

candlestick_ohlc(ax, ohlc_data, width=0.5, colorup='green', colordown='red')
ax.axhline(highest_value, color='green', linestyle='--', linewidth=1, label=f'Highest: {highest_value}')
ax.axhline(lowest_value, color='red', linestyle='--', linewidth=1, label=f'Lowest: {lowest_value}')
ax.plot(dates, regression_line, color='blue', linestyle='--', linewidth=1, label='Regression Line')

# Format the x-axis
ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d'))

# Add titles and labels
plt.title('May 2021: Tesla Episode')
plt.xlabel('May')
plt.ylabel('Price (USD)')
plt.legend()

plt.tight_layout()
plt.show()
