import pandas as pd 

trades = pd.read_csv("C:\\Users\\chaud\\Downloads\\historical_data.csv")
sentiment = pd.read_csv("C:\\Users\\chaud\Downloads\\fear_greed_index.csv")

print(trades["Timestamp"].tail())
print(sentiment["timestamp"].head())


import pandas as pd


trades['datetime'] = pd.to_datetime(
    trades['Timestamp'],
    unit='ms'
)


sentiment['datetime'] = pd.to_datetime(
    sentiment['timestamp'],
    unit='s'
)

trades['date'] = trades['datetime'].dt.date
sentiment['date'] = sentiment['datetime'].dt.date


print(pd.to_datetime(1.750000e+12, unit='ms'))
print(pd.to_datetime(1517463000, unit='s'))


merged = pd.merge(
    trades,
    sentiment,
    on='date',
    how='left'
)

print(merged.shape)
print(merged.head())

print(merged.columns.tolist())


# 1. Trade count by sentiment
print(merged.groupby('classification').size())

# 2. Average PnL by sentiment
print(merged.groupby('classification')['Closed PnL'].mean())

# 3. Total PnL by sentiment
print(merged.groupby('classification')['Closed PnL'].sum())

# 4. Mean + Median PnL
print(
    merged.groupby('classification')['Closed PnL']
    .agg(['mean', 'median'])
)

# 5. Loss analysis
losses = merged[merged['Closed PnL'] < 0]

print(
    losses.groupby('classification')['Closed PnL']
    .agg(['count', 'sum', 'mean'])
)


# Win Rate by Sentiment
merged['Win'] = merged['Closed PnL'] > 0

win_rate = merged.groupby('classification')['Win'].mean() * 100
print(win_rate)

# Trade Volume by Sentiment
trade_volume = merged.groupby('classification').size()
print(trade_volume)

# Average Trade Size by Sentiment
print(merged.groupby('classification')['Size USD'].mean())  # agar column naam alag hai to replace karo

# PnL Distribution Summary
print(
    merged.groupby('classification')['Closed PnL']
    .describe()
)

# Extreme Fear vs Extreme Greed
print(
    merged.groupby('classification')['Closed PnL']
    .agg(['count','mean','median','sum'])
)




import seaborn as sns
import matplotlib.pyplot as plt

# Average PnL
sns.barplot(data=merged, x='classification', y='Closed PnL')
plt.show()

# Trade Count
sns.countplot(data=merged, x='classification')
plt.show()

# Boxplot
sns.boxplot(data=merged, x='classification', y='Closed PnL')
plt.show()


