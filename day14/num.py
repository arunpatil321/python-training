# What is NumPy in python?
# NumPy is the fundamental package for scientific computing in Python. ...
# NumPy arrays facilitate advanced mathematical and other types of operations on
# large numbers of data. Typically, such operations are executed more efficiently and with less code
# than is possible using Python's built-in sequences.

# Why Use NumPy?
# In Python we have lists that serve the purpose of arrays, but they are slow to process.
# NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
# The array object in NumPy is called ndarray, it provides a lot of supporting
# functions that make working with ndarray very easy.
# Arrays are very frequently used in data science, where speed and resources are very important

#numpy creating array:
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# print(arr)
# print(type(arr))

#numpy creating array indexing
# import numpy as np
# arr = np.array([1, 2, 3, 4])
# print(arr[3])
# adding
# import numpy as np
# arr = np.array([1, 2, 3, 4])
# print(arr[0] + arr[2])
#numpy creating array slicing
# Slicing arrays
# Slicing in python means taking elements from one given index to another given index.
# We pass slice instead of index like this: [start:end].
# We can also define the step, like this: [start:end:step].
# If we don't pass start its considered 0
# If we don't pass end its considered length of array in that dimension
# If we don't pass step its considered 1
# Example
# Slice elements from index 1 to index 5 from the following array:

# import numpy as np
#
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
#
# print(arr[1:5])

#2type slicing
# import numpy as np
#
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
#
# print(arr[1:5:2])

