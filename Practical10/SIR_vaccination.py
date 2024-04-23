# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
N=10000 #totoal number of population
beta=0.3 #infection probability contact
gamma=0.05#recovery probability 
Vac_rate=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
all_I=[]#create a list to store I lists for each vaccination rate
for vac in Vac_rate:
    Infected=1 #initial infected people
    Susceptible=int((1-vac)*N-Infected) #initial susceptible people
    Recovered=0
    I=[Infected]
    for i in range(1,1001):
        infect_rate=Infected/N
        New_I=sum(np.random.choice(range(2),max(0,Susceptible),p=[1-beta*infect_rate,beta*infect_rate]))
        #use max() to avoid negative suspecible when vac=1
        Infected+=New_I
        Susceptible-=New_I
        New_R=sum(np.random.choice(range(2),Infected,p=(1-gamma,gamma)))
        Recovered+=New_R
        Infected-=New_R
        I.append(Infected)
    all_I.append(I)
for index,I in enumerate(all_I):
    plt.plot(I, label=f"{int(Vac_rate[index]*100)}%")
plt.xlabel("Time")
plt.ylabel("Number of Infected People")
plt.legend()
plt.title("SIR Model with Different Vaccination Rates")
plt.show()