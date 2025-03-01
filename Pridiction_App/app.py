from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import yfinance as yf
from sklearn.ensemble import RandomForestRegressor

app = Flask(__name__)

# Load historical data
ticker_symbol = 'TSLA'
tesla_data = yf.Ticker(ticker_symbol)
historical_data = tesla_data.history(period='10y')

# Prepare data for prediction
historical_data['Date'] = historical_data.index
historical_data['Date'] = pd.to_datetime(historical_data['Date']).map(pd.Timestamp.timestamp)
X = historical_data[['Date']]
y = historical_data['Close']

# Train the model
model = RandomForestRegressor()
model.fit(X, y)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    date_str = request.form['date']
    date = pd.to_datetime(date_str).timestamp()
    prediction = model.predict(np.array([[date]]))[0]
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
    @app.route('/')
    def index():
        return render_template('index.html')