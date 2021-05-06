// This program outputs a summary of each variable to a single text file//

import pandas as pd

irisData= irisdata.scv #work on chanhing file to csv for analysis#

df = pd.DataFrame(irisData, columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class'])
print (df.head(5))

print(df.describe())
print(type(df.decsribe())) 




#saves a histogram of each variable to png files# 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris

df.plot.histogram

plt.show(). # finalise and check does code run#
