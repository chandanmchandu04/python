import numpy as np
import pandas as pd

# Original list
l = [22, 344, 56, 667, 889]
l1 = np.array(l)
print("Array from list l:", l1)

# Create a 1x5 array of zeros
l2 = np.zeros((1, 5))
print("Array of zeros (1x5):", l2)

# Create a 4x7 array of random numbers
l3 = np.random.random((4, 7))
print("4x7 array of random numbers:", l3)

# Create an array of 50 evenly spaced numbers between 0 and 11
l4 = np.linspace(0, 11, num=50)
print("Array of 50 evenly spaced numbers between 0 and 11:", l4)

# Create a 1x3 array of ones
l5 = np.ones((1, 3))
print("Array of ones (1x3):", l5)

# Get the itemsize of an array created with arange
a1 = np.arange(10, dtype=np.int64)
a1_itemsize = a1.itemsize
print("Item size of array created with arange (dtype=int64):", a1_itemsize)

# Create a 3x4 array of squares of numbers from 0 to 11, then transpose it
a2 = np.arange(12, dtype=float).reshape(3, 4)
a2_squared_transposed = (a2 ** 2).T
print("Transposed array of squares of numbers from 0 to 11:\n", a2_squared_transposed)

#METHODS AND FUNCTIONS
arr1 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
print(arr1)

total_sum = arr1.sum()  # Total value in the array
print(total_sum)

min_value = arr1.min()  # Minimum value in the array
print(min_value)

max_value = arr1.max()  # Maximum value in the array
print(max_value)

mean_value = arr1.mean()  # Average of the elements in the array
print(mean_value)

std_dev = np.std(arr1)  # Standard deviation of the elements in the array
print(std_dev)

variance = np.var(arr1)  # Variance of the elements in the array
print(variance)

argument_max = np.argmax(arr1) #argmax is a function that returns the index of the maximum value in an array or function.
print(argument_max)

arr2 = np.array([[10, 11, 12],
                 [13, 14, 15],
                 [16, 17, 18]])
n = arr1 + arr2
print(n)

matmul = np.matmul(arr1, arr2) #Matrix multiplication
print(matmul)

n1 = arr1 @ arr2 #The '@' operator is a shorthand notation for matrix multiplication. It performs element-wise multiplication of two arrays or matrices.
print(n1)


