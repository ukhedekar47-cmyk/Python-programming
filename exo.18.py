print("UIN: 251P107,NAME: Aryan Khedekar")

import numpy as np 
arr1 = np.array([10, 20, 30, 40, 50])
print("1D Array: ", arr1)


print("First element: ", arr1[0])
print("Last element: ", arr1[-1])
print("Elements from index 1 to 3: ", arr1[1:4])



arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array: \n", arr2)

print("Element at row 0, column 1: ", arr2[0,1])
print("First row: ", arr2[0, :])
print("Second column: ", arr2[:, 1])




arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7,8]]])
print("\n3D Array: \n", arr3)


print("Element: ", arr3[1, 0, 1])
print("First matrix: \n", arr3[:, 0, :])

arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr .reshape(2,3) 
print("\nOriginal Array: ", arr)
print("Resahaped (2x3): \n", reshaped) 