uk_popu=[0.56,0.62,0.04,9.7] #The population of 4 uk cities (unit:million)
uk_cities=["Edinburgh","Glasgow","Stirling","London"] #The name of 4 uk cities
cn_popu=[0.58,8.4,29.9,22.2]  #The population of 4 China cities (unit:million)
cn_cities=["Haining","Hangzhou","Shanghai","Beijing"] #The name of 4 China cities
import numpy as np
import matplotlib.pyplot as plt
width=0.5
plt.figure()     #make a bar chart of 4 uk cities
plt.bar(uk_cities,uk_popu,width)
plt.show()
plt.figure()     #make a bar chart of 4 uk cities
plt.bar(cn_cities,cn_popu,width)
plt.show()
uk_popu.sort() #reorder 4 uk cities from small to big
cn_popu.sort() #reorder 4 China cities from small to big
print(uk_popu)
print(cn_popu)
