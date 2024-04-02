import os     #import modules for later manipulation
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("/Users/submerge/IBI1_2023-24/Practical7") #change to the directory with the .csv file
print(os.getcwd())
dalys_data = pd.read_csv("dalys-rate-from-all-causes(1).csv")#import the .csv file
x=dalys_data.iloc[0:100:10,3]
print(x)#show the fourth column (the DALYs) from every 10th row
#starting from the first row, for the first 100 rows
a=dalys_data.loc[:,"Entity"]=="Afghanistan"#a Boolean to show DALYs for all rows corresponding to Afghanistan
print(dalys_data[a].iloc[:,3])
print(dalys_data[a].iloc[:,3]==dalys_data.loc[0:29,"DALYs"])


china_data=dalys_data[dalys_data['Entity']=="China"].iloc[:,[0,2,3]]
china_data['Year'] = china_data['Year'].astype(str)#"Year"like 2019 in the dataframe is not a string but a int
china_2019=china_data[china_data["Year"]=="2019"].iloc[:,2]
mean_all=np.mean(china_data['DALYs'].astype(float))#the mean of DALYs of China all time
mean_2019=np.mean(china_2019.astype(float))#the mean of DALYs of China in 2019
if mean_2019>mean_all:#compare 2 means
    print("2019 was above the mean")
if mean_2019<mean_all:
    print("2019 was below the mean")
else:
    print("2019 was equal to the mean")


plt.plot(china_data.Year, china_data.DALYs, 'b+')#use blue plus sign as gauge points
plt.xticks(china_data.Year,rotation=-90)#Rotate scale labels to make it easier to read
plt.show()


uk_data = dalys_data[dalys_data['Entity'] == 'United Kingdom']#Asking one other question
plt.plot(uk_data.Year,uk_data.DALYs)
plt.show()