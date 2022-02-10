# import numpy as np #filter methods 
# arr = np.array([41, 42, 43, 44])
# x = [True, False, True, False]
# newarr = arr[x]
# print(newarr)

import numpy as np
arr = np.array([41, 42, 43, 44])
# Create an empty list
filter_arr = []
# go through each element in arr
for element in arr:
#   # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

#search method find the index values
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 4, 4])
# x = np.where(arr == 2)
# print(x)
#
# # Find the indexes where the values are even:
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# x = np.where(arr%2 == 0)
# print(x)
#
# # Find the indexes where the values are odd:
#
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# x = np.where(arr%2 == 1)
# print(x)

# Split the array in 3 parts:
#
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6,])
# newarr = np.array_split(arr, 3)
# print(newarr)
#
# # Split the array in 4 parts:
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6])
# newarr = np.array_split(arr, 4)
# print(newarr)

# Sorting means putting elements in an ordered sequence.
# Ordered sequence is any sequence that has an order corresponding
# to elements, like numeric or alphabetical, ascending or descending.
# The NumPy ndarray object has a function called sort(),that will sort a specified array.

# sort an array
# import numpy as np
# arr = np.array([3, 2, 0, 1])
# print(np.sort(arr))
# # Sort the array alphabetically:
# import numpy as np
# arr = np.array(['banana', 'cherry', 'apple'])
# print(np.sort(arr))

