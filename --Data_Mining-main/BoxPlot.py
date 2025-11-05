# Import libraries
import matplotlib.pyplot as plt
import numpy as np
 
 
# Creating dataset
np.random.seed(10)
data = np.random.normal(100, 20, 200)
 
fig = plt.figure(figsize =(10, 7))
 
# Creating plot
plt.boxplot(data)
 
# show plot
plt.show()

import pandas as pd

df = pd.read_csv("../input/iris-dataset/iris.csv")

df

df.head(10)

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
df=df.head(10)
df.boxplot(by ='petal.width', column =['petal.length'], grid = True)