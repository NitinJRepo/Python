# Sample program for pandas DataFrame and Series
import numpy as np
import pandas as pd

myarray = np.array([[1, 2, 3], [4, 5, 6]])

rownames = ['R1', 'R2']
colnames = ['C1', 'C2', 'C3']

#DataFrame
mydataframe = pd.DataFrame(myarray, index=rownames, columns=colnames)

print(mydataframe)