import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
a=pd.read_csv("C:\\Users\\91638\\Desktop\\Documents\\datasets\\hi.csv")
x=a('x')
y=a('y')
x_seq=np.linspace(min(x),max(x),300,reshape(-1,1))
degree=9
polyreg=make_pipeline(PolonomialFeatures(degree),LinearRegression())
polyreg.fit(x,y)
plt.figure()
plt.scatter(x, y)
plt.title('poly')
plt.plot(x_seq,polyreg.predict(x_seq))
plt.show()
