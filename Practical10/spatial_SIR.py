# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
beta=0.3 #define basic parameters: beta means infection probability contact
gamma=0.05 #recovery probability
# make array of all susceptible population
population = np.zeros((100,100))
outbreak = np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]]=1#select one to be infected randomly.
plt.figure(figsize=(6,4),dpi=150)
plt.imshow(population,cmap="viridis",interpolation="nearest")
plt.title("Select One to be Infected Randomly.")
plt.show()
plt.clf()
for time in range(1,101): 
    infectedIndex = np.where(population==1)# find infected points
    for i in range(len(infectedIndex[0])):# loop through all infected points
        # get x, y coordinates for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        # infect each neighbour with probability beta
        # # infect all 8 neighbours (this is a bit finicky, is there a better way?):
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                if (xNeighbour,yNeighbour) != (x,y):# don't infect yourself! (Is this strictly necessary?)
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:# make sure I don't fall off an edge
                        if population[xNeighbour,yNeighbour]==0:# only infect neighbours that are not already infected!
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
    recover=np.random.choice([0,1],len(infectedIndex[0]),p=[1-gamma,gamma]) #randomly choose infected to recover
    population[infectedIndex[0][recover==1],infectedIndex[1][recover==1]]=2  
    if time in [10, 50, 100]:
        plt.imshow(population,cmap="viridis",interpolation="nearest")
        plt.title(f"Spaticial SIR model results for {time} repaeats.")
        plt.show()
 
   