import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("/Users/oliver/Desktop/打印/IBI/Practical7")
print(os.listdir())
dalys_data = pd.read_csv("dalys-rate-from-all-causes(1).csv")
print(dalys_data.head(5))
print(dalys_data.info())
print(dalys_data.describe())
a= dalys_data["Entity"] == "Afghanistan"
print(dalys_data[a].iloc[:,3])
print(dalys_data[a].iloc[:,3]==dalys_data.loc[0:29,"DALYs"])