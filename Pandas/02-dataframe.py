# Sample program for pandas DataFrame and Series
import numpy as np
import pandas as pd

myarray = np.array([[1, 2, 3], [4, 5, 6]])

rownames = ['R1', 'R2']
colnames = ['C1', 'C2', 'C3']

#DataFrame
mydataframe = pd.DataFrame(myarray, index=rownames, columns=colnames)

print(mydataframe)


myarray2 = np.array([7, 8, 9])
rownames2 = ['R1', 'R2', 'R3']

#Series
myseries = pd.Series(myarray2, index=rownames2)

print(myseries)

#You can access the data in a series like a NumPy array and like a dictionary, for example:
print(myseries[0])
print(myseries['R1'])