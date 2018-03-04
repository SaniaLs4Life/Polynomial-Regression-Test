import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



data = pd.read_csv("data.csv")

X = data["x"]
Y = data["y"]

X = np.array(X)
Y = np.array(Y)


a,b,c,d  = np.polyfit(X, Y, 3)
z = np.arange(3)

plt.scatter(X,Y)
plt.plot(z, a*z*z*z+b*z*z+c*z+d)
plt.show()