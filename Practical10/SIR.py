# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
N=10000 #totoal number of population
beta=0.3 #infection probability contact
gamma=0.05#recovery probability 
Infected=1 #initial infected people
Susceptible=9999 #initial susceptible people
Recovered=0
S=[Susceptible]
I=[Infected]
R=[Recovered]
for i in range(1,1001):
    infect_rate=Infected/N
    New_I=sum(np.random.choice(range(2),Susceptible,p=[1-beta*infect_rate,beta*infect_rate]))
    Infected+=New_I
    Susceptible-=New_I
    New_R=sum(np.random.choice(range(2),Infected,p=(1-gamma,gamma)))
    Recovered+=New_R
    Infected-=New_R
    S.append(Susceptible)
    I.append(Infected)
    R.append(Recovered)
plt.plot(S,label="Susceptible")
plt.plot(I,label="Infected")
plt.plot(R,label="Recovered")
plt.xlabel("Time")
plt.ylabel("Number of people")
plt.legend()
plt.title("SIR Model")
plt.show()
