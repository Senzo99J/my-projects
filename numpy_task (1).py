import numpy as np
#Create 2D array with float data type
#np.array((1,0,0),(0,1,0),(0,0,1), dtype=float) doesn't create a 2D correctly
# You need square brackets for 2D array
identity_2D = np.array([[1, 0, 0],[0, 1, 0],[0, 0, 1]], dtype=float)

# Difference between a = np.array([0,0,0]) and a = np.array([[0,0,0]])
a1 = np.array([0, 0, 0]) # Creates a 1D array with shape(3,)
a2 = np.array([[0, 0, 0]]) # Creates a 2D array with shape(1, 3)

# Creating a 3D array with linspace, and indexing to obtain specific elements
arr = np.linspace(1, 48, 48).reshape(3, 4, 4)

# Indexing and slicing to obtain specific
# 20.0
element_20 = arr[1, 0, 3]
print("Element at arr [0, 1, 2]:", element_20)

# [9, 10, 11, 12]
sub_array_1 = arr[0, 2, :]
print("Subarray arr[0, 2, :]:",sub_array_1)

# A 4x4
sub_array_2 = arr[2, :, :]
print("Subarray arr[2, :, :]:\n",sub_array_2)

# 2x2 
sub_array_3 = arr[0, 2:4, 2:4]
print("Subarray arr[0, 2:4, 2:4]:\n",sub_array_3)

# [5, 6], [21, 22], [37, 38]
sub_array_4 = arr[:, 1, 0:2]
print("Subarray arr[:, 1, 0:2]:",sub_array_4)

# [36, 35], [40, 39], [44, 43], [48, 47]
sub_array_5 = arr[2, :, ::-1]
print("Subarray arr[2, :, ::-1]:",sub_array_5)

# [13, 9, 5, 1],[29, 25, 21, 17],[45, 41, 37, 33]
sub_array_6 = arr[:, :, 0]
print("Subarray arr[:, :, 0]:\n",sub_array_6)

# [[1, 4], [45, 48]]
sub_array_7 = arr[:, 0, 0:2]
print("Subarray arr[:, 0, 0:2]:",sub_array_7)

# [[25, 26, 27, 28],[29, 30, 31, 32],[33, 34, 35, 36],[37, 38, 39, 40]]
sub_array_8 = arr[1, :, :]
print("Subarray arr[1:, :, :]:",sub_array_8 )

# Use flatten and reshape
flattened_array = arr.flatten()
reshaped_array = flattened_array.reshape(3, 4, 4)

print("Reshaped array(3x4x4)\n",reshaped_array)