# argmax() returns the position of the largest value. 

import numpy as np

A = np.matrix([[1,2,3,33],[4,5,6,66],[7,8,9,99]])
print("Input matrix: \n", A)

print("np.argmax(A) = ", np.argmax(A))  # 11, which is the position of 99

print("np.argmax(A[:,:]) = ", np.argmax(A[:,:]))  # 11, which is the position of 99

print("np.argmax(A[:1]) = ", np.argmax(A[:1]))  # 3, which is the position of 33 (from  resulted matrix: [[1,2,3,33]])

print("np.argmax(A[:,2]) = ", np.argmax(A[:,2]))  # 2, which is the position of 9 (from resulted matrix: [[3],[6],[9]])

print("np.argmax(A[1:,2]) = ", np.argmax(A[1:,2]))  # 1, which is the position of 9 (from resulted matrix: [[6],[9]])

