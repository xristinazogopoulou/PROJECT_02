import json 
import matplotlib.pyplot as plt
import numpy as np

c = open('rowws.json')
rowws = json.load(c)

f = open('uspop.json')
uspop = json.load(f)

#print(rowws)
year_x = []
population_y= []
population_u=[]
year_u=[]

data = rowws[1]
for i in range(len(data)):
    #print(data[i])
    population_y.append(float(data[i]['value']))
    year_x.append(int(data[i]['date']))

data= uspop[1]
for i in range (len(data)):
    population_u.append(float(data[i]['value']))
    year_u.append(int(data[i]['date']))

population_u = population_u[1:]
year_u = year_u[1:]

print(year_x)
print(population_y)
print(population_u)
plt.plot(year_x,population_y, label='India')
plt.plot(year_u,population_u, label='US')

plt.xlabel('Year')
plt.ylabel('Population')

plt.xticks(np.arange(1960, 2021, step=10))
plt.yticks(np.arange(180671000, 1390004385, step=100000000))
plt.legend()
plt.title('Population in India and the U.S. from 1960 to 2020')
plt.show()

import pandas as pd
df = pd.read_csv('gdpp.csv')
print(df)

x = df.Year
y = df['GDP per capita (current US$)']

fig, ax = plt.subplots()
ax.bar(x,y)
plt.title('India GDP Per Capita From 1960 to 2020')
plt.ylabel('GDP Per Capita (current US$, in thousands)')
plt.xlabel('Year')
plt.xticks(rotation=45,fontsize=7, color='black')
plt.yticks(fontsize = 7)
plt.yticks(np.arange(min(y), max(y), step= 100))
plt.xticks(np.arange(1960, 2021, step=5))
plt.show()







