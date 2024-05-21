a=5 #set the density of the first day to be 5
n=1 #initialize the first day of leaving the lab
while a in range(1,90): #make sure the density ranges from 1 to 90
   a=2*a #the density doubles each day
   if a<=90:
        n+=1 #add one day for holiday
print(f"On day{n} the cell density goes over 90%") 

