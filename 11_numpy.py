import numpy as np

# Install numpy
# sudo pip3 install numpy

# NumPy is a Python library used for working with arrays.
# It is often used with the `matplotlib` library.
# It also has functions for working in domain of linear algebra, fourier transform, and matrices.
# In Python we have lists that serve the purpose of arrays, but they are slow to process.
# NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
# NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.
# The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.
# Arrays are very frequently used in data science, where speed and resources are very important.

# Nested Arrays
# Creating 2 dimensional array object
# Has 2 rows and 3 columns (shape).
arr = np.array([[1, 2, 3], [4, 2, 5]])
print(arr)

# Printing type of arr object
print("Array is of type: ", type(arr))

# Printing array dimensions (axes)
print("No. of dimensions: ", arr.ndim)

# Printing shape of array
print("Shape of array: ", arr.shape)

# Printing size (total number of elements) of array
print("Size of array: ", arr.size)

# Printing type of elements in array
print("Array stores elements of type: ", arr.dtype)

print("\n")
# Creating a one dimensional array
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# numpy.arrange() function creates an evenly spaced array with a given step size.
# This is analogous to the range() function you have used to create lists.

# Create a sequence of integers
# from 0 to 30 with steps of 5
f = np.arange(0, 30, 5)
print("A sequential array with steps of 5:\n", f)

# Starting point defaults to 0
# 30 is the end point.
# Step size defaults to 1
print("A sequential array with 30 items default steps of 1:")
f = np.arange(30)
print(f)

# You can get the length of a list with len() and use that to create an array.
my_list = [4, 5, 9, 2, 0]
print("\nThe length of my_list:", len(my_list))
my_npArray = np.arange(len(my_list))
print("my_npArray is:", my_npArray)
