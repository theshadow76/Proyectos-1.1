# !pip install alpaca_trade_api
import alpaca_trade_api as tradeapi
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras import layers
import matplotlib.pyplot as plt
import time
# !pip install yfinance

import yfinance as yf
# !pip install pandas-datareader
import pandas_datareader as pdr
from datetime import datetime

api_key = ''
api_secret = ''
base_url = 'https://paper-api.alpaca.markets'
api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')

def get_sp500_symbols():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    sp500_table = pd.read_html(url, header=0)[0]
    symbols = sp500_table["Symbol"].tolist()
    return symbols

symbols = get_sp500_symbols()


stocks_owned = {symbol: 12000 for symbol in symbols}
timeframe = '1D'

# Train the model once, outside of the loop
X_all = []
y_all = []

# Train a model for each symbol and store it in a dictionary
models = {}

def update_stocks_owned(api, symbols):
    stocks_owned = {symbol: 0 for symbol in symbols}
    positions = api.list_positions()

    for position in positions:
        if position.symbol in stocks_owned:
            stocks_owned[position.symbol] = int(position.qty)

    return stocks_owned
stocks_owned = update_stocks_owned(api, symbols)

for symbol in symbols:
    print(f"Fetching data for symbol: {symbol}")  # Add this line to see the symbol value
    end = pd.Timestamp.now(tz='America/New_York') - pd.DateOffset(minutes=15)
    start = (end - pd.DateOffset(years=1)).isoformat()
    end = end.isoformat()
    bars = api.get_bars(symbol, tradeapi.rest.TimeFrame.Day, start, end).df

    # Preprocess the data
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(bars[['open', 'high', 'low', 'close', 'volume']].values)
    X = []
    y = []
    for i in range(60, len(scaled_data)):
        X.append(scaled_data[i - 60:i])
        y.append(scaled_data[i, 3])

    X_all.extend(X)
    y_all.extend(y)

X_all = np.array(X_all)
y_all = np.array(y_all)
X_train, X_test, y_train, y_test = train_test_split(X_all, y_all, test_size=0.2)

# Define the model
model = tf.keras.Sequential([
    layers.Flatten(input_shape=(60, 5)),
    layers.Dense(128, activation='relu'),
    layers.Dense(1)
])
model.compile(optimizer='adam', loss='mse')

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.1)

def get_open_sell_orders_qty(api, symbol):
    try:
        open_orders = api.list_orders(status='open')
        sell_orders = [order for order in open_orders if order.symbol == symbol and order.side == 'sell']
        return sum(int(order.qty) for order in sell_orders)
    except Exception as e:
        print(f"Error getting open sell orders for {symbol}: {str(e)}")
        return 0

def cancel_all_orders(api):
    open_orders = api.list_orders(status='open')
    for order in open_orders:
        api.cancel_order(order.id)

while True:
    for symbol in symbols:
        end = pd.Timestamp.now(tz='America/New_York') - pd.DateOffset(minutes=15)
        start = (end - pd.DateOffset(years=1)).isoformat()
        end = end.isoformat()
        bars = api.get_bars(symbol, tradeapi.rest.TimeFrame.Day, start, end).df

        # Preprocess the data
        scaler = MinMaxScaler()
        scaled_data = scaler.fit_transform(bars[['open', 'high', 'low', 'close', 'volume']].values)
        X = []
        y = []
        for i in range(60, len(scaled_data)):
            X.append(scaled_data[i - 60:i])
            y.append(scaled_data[i, 3])
        X = np.array(X)
        y = np.array(y)
        X_test_symbol = X

        # Make predictions
        predicted_prices = model.predict(X_test_symbol)

        # Inverse-transform the predicted prices
        predicted_prices_reshaped = predicted_prices.reshape(-1, 1)
        temp_X_test = np.copy(X_test_symbol)
        temp_X_test[:, -1, 3] = predicted_prices_reshaped[:, 0]
        predicted_prices_inverse = scaler.inverse_transform(temp_X_test.reshape(-1, 5))[:, 3]

        # Inverse-transform the target prices
        actual_prices_inverse = scaler.inverse_transform(X_test_symbol.reshape(-1, 5))[:, 3]

        # Define a prediction threshold (e.g., 0.01 for 1% change)
        threshold = 0.01

        # Iterate through the test data and make predictions
        for i in range(len(actual_prices_inverse)):
            actual_price = actual_prices_inverse[i]
            predicted_price = predicted_prices_inverse[i]

            # Calculate the price change ratio
            price_change_ratio = (predicted_price - actual_price) / actual_price

            order_qty = int(abs(price_change_ratio) * 2 + 1)  # Adjust the order quantity based on the predicted price change

            if price_change_ratio > threshold:
                # Buy the stock if the predicted price is higher than the threshold
                if stocks_owned[symbol] > 0:
                  print(f"Buy: {actual_price:.2f}, Predicted: {predicted_price:.2f}, Quantity: {order_qty}")
                  cancel_all_orders(api)
                  api.submit_order(
                      symbol=symbol,
                      qty=order_qty,
                      side='buy',
                      type='market',
                      time_in_force='day'
                  )
                stocks_owned[symbol] += order_qty
            elif price_change_ratio < -threshold:
                stocks_owned[symbol] = get_stock_position(api, symbol)
                open_sell_orders_qty = get_open_sell_orders_qty(api, symbol)
                available_qty = stocks_owned[symbol] - open_sell_orders_qty

                if available_qty > 1:
                    # Sell the stock if the predicted price is lower than the threshold
                    print(f"Sell: {actual_price:.2f}, Predicted: {predicted_price:.2f}, Quantity: {order_qty}")
                    cancel_all_orders(api)
                    api.submit_order(
                        symbol=symbol,
                        qty=min(order_qty, available_qty - 1),  # Don't sell more than the available stocks
                        side='sell',
                        type='market',
                        time_in_force='day'
                    )
                    stocks_owned[symbol] -= order_qty
                else:
                    print(f"Cannot sell {symbol} as no stocks owned.")
            else:
                # Hold the stock if the predicted price change is within the threshold
                print(f"Hold: {actual_price:.2f}, Predicted: {predicted_price:.2f}")

        # Sleep for some time before fetching new data and starting the next iteration
        sleep_duration = 1  # Sleep for 1 hour (in seconds)
        time.sleep(sleep_duration)
