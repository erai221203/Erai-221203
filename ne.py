import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset = pd.read_csv('C:\\Users\\91638\\Desktop\\Documents\\datasets\\data science.csv')
dataset.describe()
print(dataset)
dataset.plot(x='car_name', y='disp', style='o')
plt.title('age vs BMI')
plt.xlabel('age')
plt.ylabel('BMI')
plt.show()
