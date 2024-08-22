import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import dates as mdates  # This needs for date formatting
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import mean_squared_error, r2_score

# Importing tensorflow
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import plot_model

import numpy as np
from datetime import date , timedelta
from tensorflow.keras.models import load_model


print("Available 'IRFC' , 'CDSL'")
stock = input("Enter Stock Symbol to know predction :")
symbol = stock + ".csv"

#Get the Dataset
df=pd.read_csv(symbol)

#Print the shape of Dataframe  and Check for Null Values
print("Dataframe Shape: ", df. shape)

# Drop rows with null values in specific columns
df.dropna(subset=['Open', 'High' , 'Low' , 'Close' , 'Adj Close'], inplace=True)

#Set Target Variable
output_var = pd.DataFrame(df["Adj Close"])
#Selecting the Features
features = ["Open", "High", "Low", "Volume"]

#Scaling
scaler = MinMaxScaler()
feature_transform = scaler.fit_transform(df[features])
feature_transform= pd.DataFrame(columns=features, data=feature_transform, index=df.index)



#Splitting to Training set and Test set
timesplit= TimeSeriesSplit(n_splits=10)
for train_index, test_index in timesplit.split(feature_transform):
        X_train  = feature_transform[:len(train_index)]
        X_test = feature_transform[len(train_index): (len(train_index)+len(test_index))]
        y_train  = output_var[:len(train_index)].values.ravel()
        y_test = output_var[len(train_index): (len(train_index)+len(test_index))].values.ravel()

#Process the data for LSTM
trainX =np.array(X_train)
testX =np.array(X_test)
X_train = trainX.reshape(trainX.shape[0], 1, -1)
X_test = testX.reshape(testX.shape[0], 1, -1)

#Building the LSTM Model
lstm = Sequential()
lstm.add(LSTM(32, input_shape=(1, trainX.shape[1]), activation="relu", return_sequences=False))
lstm.add(Dense(1))
lstm.compile(loss="mean_squared_error", optimizer="adam")

history=lstm.fit(X_train, y_train, epochs=100, batch_size=8, verbose=1, shuffle=False)

y_pred= lstm.predict(X_test)

from tensorflow.keras.models import save_model
lstm.save('lstm.h5')

# Loading trained LSTM model
model = load_model('lstm.h5')

data = np.array(testX)
last_sequence = data[-1:]

# Reshape the input data to match the expected input shape of the model
last_sequence = last_sequence.reshape((last_sequence.shape[0], 1, last_sequence.shape[1]))

# Make prediction for the next day
prediction = model.predict(last_sequence)

tomorrow = today + timedelta(days=1)


prediction = y_pred[-1]
price = y_test[-1]

if(prediction < price):

  def draw_falling_market():
      # Generate data
      x = np.linspace(0, 10, 100)
      y = np.sin(x) - x/10  # Example downtrend data

      plt.figure(figsize=(10, 6))

      # Plot the downtrend line
      plt.plot(x, y, color='blue', linewidth=2)

      # Fill the area below the downtrend line
      plt.fill_between(x, y, min(y), color='red', alpha=0.3)

      # Adding labels and title
      plt.xlabel('Time')
      plt.ylabel('Market Trend')
      plt.title('Falling Market Signal')

      # Display the plot
      plt.grid(True)
      plt.show()

  # Call the function to draw the falling market
  draw_falling_market()

else:
  def draw_rising_market():
      # Generate data
      x = np.linspace(0, 10, 100)
      uptrend = np.sin(x) + x/10  # Example uptrend data

      plt.figure(figsize=(10, 6))

      # Plot the uptrend line
      plt.plot(x, uptrend, color='green', linewidth=2)

      # Fill the area above the uptrend line
      plt.fill_between(x, uptrend, max(uptrend), color='green', alpha=0.3)

      # Adding labels and title
      plt.xlabel('Time', fontsize=14)
      plt.ylabel('Market Trend', fontsize=14)
      plt.title('Rising Market Signal', fontsize=16)

      # Customize tick labels
      plt.xticks(fontsize=12)
      plt.yticks(fontsize=12)

      # Customize grid
      plt.grid(True, linestyle='--', alpha=0.5)

      # Remove top and right spines
      plt.gca().spines['top'].set_visible(False)
      plt.gca().spines['right'].set_visible(False)

      # Show the plot
      plt.show()

  # Call the function to draw the rising market
  draw_rising_market()

print("Prediction for ", tomorrow, prediction)

print("---------------------------------------INVEST AT YOUR OWN RISK--------------------------------------------")
