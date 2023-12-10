
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
import seaborn as sns

mpg_df = pd.read_csv("sample.csv")  

# Check top few records to get a feel of the data structure
mpg_df.head(50)
