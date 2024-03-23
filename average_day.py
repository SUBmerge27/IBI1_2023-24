uni={"Sleeping":8, "Classes":6, "Studying":3.5,\
    "TV":2, "Music":1, "Others":3.5 }      #create a dic called uni to show the average time of uni students spending on each activitiy
import matplotlib.pyplot as plt
Activities=[]
Activities.extend(uni.keys())             #pick the keys in uni out to form a list
Time=[]
Time.extend(uni.values())    #pick the values in uni out to form a list
others_and_else=[0,0,0,0,0,0.1]       #pick "others" out
plt.figure()
plt.pie(Time,labels=Activities,startangle=90,explode=others_and_else)      #create a pie chart
plt.show()
others=uni["Others"]
print(others)