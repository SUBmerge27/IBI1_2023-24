import matplotlib.pyplot as plt #import library
requested_activity="Classes" #Define a revisable variable to represent the activity requested by the user
uni={"Sleeping":8, "Classes":6, "Studying":3.5,\
    "TV":2, "Music":1, "Others":3.5 }   #create a dic called uni to show the average time of uni students spending on each activitiy
print(f"Average time spent on {requested_activity} is {uni[requested_activity]} hours")
Activities=[] #initialize an empty list
Activities.extend(uni.keys())  #pick the keys in uni out to form a list
Time=[]
Time.extend(uni.values())    #pick the values in uni out to form a list
others_and_else=[0,0,0,0,0,0.1]       #pick "others" out
plt.figure()
plt.pie(Time,labels=Activities,startangle=90,explode=others_and_else)      #create a pie chart
plt.show()
others=uni["Others"]
print(f"Average time spent on 'others' is {others} hours")