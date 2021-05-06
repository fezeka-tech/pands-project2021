// This program outputs a summary of each variable to a single text file//

import pandas as pd

irisData= irisdata.scv #work on chanhing file to csv for analysis#

df = pd.DataFrame(irisData, columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class'])
print (df.head(5))

print(df.describe())
print(type(df.decsribe())) 
