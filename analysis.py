# This program outputs a summary of each variable to a single text file #

import pandas as pd.      #import modules#
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



df = pd.read_csv('iris.csv').  #loading the dataset#


df = pd.DataFrame(iris.csv, columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class'])
print (df.head(5))

print(df.describe()).  #to display stats about data#
print(type(df.decsribe())) 




# Saves a histogram of each variable to png files # 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris

df.plot.histogram

plt.show(). 

plt.savefig().   #saves the histogram to a png file# 



# Outputs a scatterplot of each pair of variables #

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris

df[['sepal length_width', 'petal length_width']].plot.scatterplot  

plt.show()
