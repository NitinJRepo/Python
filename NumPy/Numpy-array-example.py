#NumPy array
# access values

import numpy

mylist = [[1, 2, 3], [3, 4, 5]]

myarray = numpy.array(mylist)

print(myarray)
print("Shape of array", myarray.shape)

print("First row: ", myarray[0])
print("Last row: ", myarray[-1])

print("Specific row and column: ", myarray[0, 2])
print("Whole column: ", myarray[:, 2])

# arithmetic
myarray1 = numpy.array([2, 2, 2])
myarray2 = numpy.array([3, 3, 3])

print("Addition: ", myarray1 + myarray2)
print("Multiplication: ", myarray1 * myarray2)
