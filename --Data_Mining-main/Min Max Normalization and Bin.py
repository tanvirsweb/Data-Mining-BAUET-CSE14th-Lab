import numpy as np 
import pandas as pd 

import pandas as pd

df = pd.read_csv("../input/kmean-data/kmean_data.csv")

df

from sklearn import preprocessing

x = df.values #returns a numpy array
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
df = pd.DataFrame(x_scaled)

df

import pandas as pd
import numpy as np
df = pd.read_csv("../input/kmean-data/kmean_data.csv")
X = df.to_numpy()
new_max =int(input())
new_min=int(input())
def NormalizeData(data):
    return ((data - np.min(data)) / (np.max(data) - np.min(data)))*(new_max-new_min)+new_min

scaled_x = NormalizeData(X)

print(scaled_x)


import numpy as np 
import math 
import pandas as pd

df = pd.read_csv("../input/kmean-data/kmean_data.csv")
columns = ['x']
df1 = pd.DataFrame(df, columns=columns)
data = df1.to_numpy()

newarr = np.array_split(data_1d, 10)

print(newarr)
print("\n")

b1=np.zeros((10,3)) 
b2=np.zeros((10,3)) 
b3=np.zeros((10,3))

for i in range (0,30,3): 
  k=int(i/3) 
  mean=(data_1d[i] + data_1d[i+1] + data_1d[i+2] )/3
  for j in range(3): 
    b1[k,j]=mean 
print("-----------------Mean Bin:----------------- \n",b1)

for i in range (0,30,3): 
  k=int(i/3) 
  for j in range (3): 
    b2[k,j]=data[i+1] 
print("-----------------Median Bin :----------------- \n",b2)


for i in range (0,30,3): 
  k=int(i/3) 
  for j in range (3): 
    if (data_1d[i+j]-data_1d[i]) < (data_1d[i+2]-data_1d[i+j]): 
      b3[k,j]=data_1d[i] 
    else: 
      b3[k,j]=data_1d[i+2]   
print("-----------------Boundary Bin:----------------- \n",b3)