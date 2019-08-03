# A pseudo-random number is a computer-generated random number.
# These numbers are not random, and are in fact completely determined by the algorithm. If you run the same code again, you’ll get the exact same numbers.  
# computers and algorithms process inputs into outputs. The outputs of computers depend on the inputs.
# So just like any output produced by a computer, pseudo-random numbers are dependent on the input.
#
# The numpy.random.seed function provides the input (i.e., the seed) to the algorithm that generates pseudo-random numbers in NumPy.
# Importantly, numpy.random.seed doesn’t exactly work all on its own.
# The numpy.random.seed function works in conjunction with other functions from NumPy.
# Specifically, numpy.random.seed works with other functions from the numpy.random namespace.
# Example: numpy.random.randint
#
# np.random.seed() makes your code repeatable also makes is easier to share.
# 

import numpy as np

np.random.seed(1)
var = np.random.randint(low = 1, high = 10, size = 50)

print(var)