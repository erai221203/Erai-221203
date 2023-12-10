# To enable plotting graphs in Jupyter notebook
#matplotlib inline 
# Numerical libraries
import numpy as np   

# Import Linear Regression machine learning library

# to handle data in form of rows and columns 
import pandas as pd    

# importing ploting libraries
import matplotlib.pyplot as plt   
import matplotlib.style
plt.style.use('classic')

#importing seaborn for statistical plots

# reading the CSV file into pandas dataframe
df = pd.read_csv("car-mpg.csv")  
# Check top few records to get a feel of the data structure
df.head(50)
print(df)
