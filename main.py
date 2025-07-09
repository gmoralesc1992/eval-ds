
# Librerias
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np

# Data
data = pd.read_csv("data/data.csv")
data.info()

# Ajuste
# model = LinearRegression()
# model.fit(X, y)

# Predicción
# y_pred = model.predict(X)

# Metricas
# r2 = r2_score(y, y_pred)
# print(r2)
# rmse = mean_squared_error(y, y_pred)
# print(rmse)
