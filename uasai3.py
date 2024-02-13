# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14VhGC5HchEOaFDsFT8Q5_PE0gco9Xyyz
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('train.csv')

print(df.head())

X = df[['Pclass','SibSp', 'Fare']]

y = df['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=24)

linear_reg = LinearRegression()
linear_reg.fit(X_train, y_train)

y_pred = linear_reg.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")

plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_test, y=y_pred)
plt.xlabel('Actual House Prices')
plt.ylabel('Predicted House Prices')
plt.title('Predictions vs Actual Values')
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))

# Contoh data (ganti dengan data sesuai kebutuhan)
y_test = [1, 2, 3, 4, 5]
y_pred = [1.2, 2.3, 2.8, 3.9, 4.5]

# Menggunakan scatterplot dengan parameter hue=None
sns.scatterplot(x=y_test, y=y_pred, hue=None)

plt.xlabel('Actual House Prices')
plt.ylabel('Predicted House Prices')
plt.title('Predictions vs Actual Values')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_test, y=y_pred, alpha=0.5, s=50, hue=y_test)
plt.xlabel('Actual House Prices')
plt.ylabel('Predicted House Prices')
plt.title('Predictions vs Actual Values with Frequency')
plt.legend(title='Frequency', loc='upper right')
plt.show()

from sklearn.model_selection import train_test_split
from tensorflow.keras.datasets import mnist

(X, y), (_, _) = mnist.load_data()

X = X.reshape((X.shape[0], -1))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train = X_train.reshape((X_train.shape[0], 28, 28))
 X_test = X_test.reshape((X_test.shape[0], 28, 28))

from sklearn.model_selection import train_test_split
from tensorflow.keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape((len(x_train), -1)) / 255.0
x_test = x_test.reshape((len(x_test), -1)) / 255.0

x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.2, random_state=42)

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()
model.add(Dense(128, activation='relu', input_shape=(784,)))
model.add(Dense(10, activation='softmax'))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10, batch_size=32, validation_data=(x_val, y_val))

import numpy as np
y_pred_probs = model.predict(x_test)
y_pred = np.argmax(y_pred_probs, axis=1)
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")