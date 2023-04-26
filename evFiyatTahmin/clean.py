import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from sklearn.preprocessing import normalize
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error

import tkinter
import tkinter.messagebox

df = pd.read_csv("kendi-kendine/evFiyatTahmin/ev_fiyat_tahmini.csv", sep=";")
X, y = df['MetreKare'].to_numpy().reshape((-1, 1)), df['fiyatlar'].to_numpy().reshape((-1, 1))

# Define number of folds
k = 5

# Initialize k-fold cross-validation
kf = KFold(n_splits=k)

# Initialize model
model = LinearRegression()

# Initialize array to store performance metrics
mse_scores = np.zeros(k)

# Loop over k folds
for i, (train_index, test_index) in enumerate(kf.split(X)):
    
    # Split dataset into training and test sets
    X_train, y_train = X[train_index], y[train_index]
    X_test, y_test = X[test_index], y[test_index]
    
    # Fit model to training set
    model.fit(X_train, y_train)
    
    # Predict on test set
    y_pred = model.predict(X_test)
    
    # Calculate mean squared error
    mse_scores[i] = mean_squared_error(y_test, y_pred)

# Calculate average performance
mse_mean = np.mean(mse_scores)

# Train model on full dataset
model.fit(X, y)

def predict_price(value):
    return model.predict([[value]])[0][0]

def on_button_click():
    value = slider.get()
    price = predict_price(value)
    tkinter.Label(text=f"Metrekare Fiyatı = {price:.2f} \n ortalama kare hatası = {mse_mean:.3f} \n score = {model.score(X,y)}").pack()

Anapencere = tkinter.Tk()
Anapencere.title("metrekare fiyat tahmini")

grafik = sns.regplot(x="MetreKare", y="fiyatlar", color="green" , data=df,line_kws={"color": "blue"})
canvas = FigureCanvasTkAgg( grafik.figure , master=Anapencere)
canvas.draw()
canvas.get_tk_widget().pack()

slider = tkinter.Scale(Anapencere, from_=10, to=600, orient=tkinter.HORIZONTAL, length=200, resolution=5)
slider.pack()

tkinter.Button(Anapencere, text='hesapla',command=on_button_click).pack()

Anapencere.mainloop()
                     

