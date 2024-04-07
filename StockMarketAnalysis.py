import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries

# Function to fetch stock data from Alpha Vantage
def fetch_stock_data(symbol, api_key):
    ts = TimeSeries(key=api_key, output_format='pandas')
    data, _ = ts.get_daily(symbol=symbol, outputsize='full') 
    return data

# Function to calculate moving average
def calculate_moving_average(data, window):
    return data['4. close'].rolling(window=window).mean()

# Main function
def main():
    api_key = ' PAI8AJYVRV3U88HA'
    symbol = 'AMZN'  # Example stock symbol (Amazon)

    # Fetch stock data
    stock_data = fetch_stock_data(symbol, api_key)

    # Calculate 50-day and 200-day moving averages
    stock_data['50MA'] = calculate_moving_average(stock_data, window=50)
    stock_data['200MA'] = calculate_moving_average(stock_data, window=200)

    # Plot stock prices and moving averages
    plt.figure(figsize=(12, 6))
    plt.plot(stock_data.index, stock_data['4. close'], label='Stock Price')
    plt.plot(stock_data.index, stock_data['50MA'], label='50-day MA')
    plt.plot(stock_data.index, stock_data['200MA'], label='200-day MA')
    plt.title(f'{symbol} Stock Price and Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
