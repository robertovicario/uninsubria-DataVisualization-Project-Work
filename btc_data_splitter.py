import pandas as pd

# Caricare il dataset da un file CSV
bitcoin_df = pd.read_csv('data/btc_prices.csv', parse_dates=['Timestamp'], date_parser=lambda x: pd.to_datetime(x, unit='s'))

# Creare il subset con soli prezzi del 2021
prices_2021 = bitcoin_df[(bitcoin_df['Timestamp'] >= '2024-01-01') & (bitcoin_df['Timestamp'] <= '2024-11-30')]


prices_2021.to_csv('btc_prices_2024.csv', index=False)
