import numpy as np
import pandas as pd

l = [22, 344, 56, 667, 889]
l1 = np.array(l)
print(l1)
l2 = np.zeros((1,5))
print(l2)
l3 = np.random.random((4, 7)) 
print(l3)
l4 = np.linspace(0, 11)
print(l4)
l5 = np.ones((1, 3))
print(l5)
a1 = np.arange(10, dtype=np.int64)
a1 = a1.itemsize
print(a1)
a2 = np.arange(12, dtype=float).reshape(3,4)
a2 = a2**2
a2 = a2.T
print(a2)

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