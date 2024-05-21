# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
N=10000 #totoal number of population
beta=0.3 #infection probability contact
gamma=0.05#recovery probability 
Infected=1 #initial infected people
Susceptible=9999 #initial susceptible people
Recovered=0
# Lists to keep track of the number of people in each category over time
S=[Susceptible]
I=[Infected]
R=[Recovered]
# Run the simulation for 1000 time points
for i in range(1,1001):
    # Calculate the infection rate based on the current number of infected individuals
    infect_rate=Infected/N
    # Randomly determine the number of new infections
    New_I=sum(np.random.choice(range(2),Susceptible,p=[1-beta*infect_rate,beta*infect_rate]))
     # Update the number of infected and susceptible individuals
    Infected+=New_I
    Susceptible-=New_I
    # Randomly determine the number of new recoveries
    New_R=sum(np.random.choice(range(2),Infected,p=(1-gamma,gamma)))
    # Update the number of recovered and infected individuals
    Recovered+=New_R
    Infected-=New_R
    # Record the current state
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
