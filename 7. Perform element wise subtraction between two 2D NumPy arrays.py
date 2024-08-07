import numpy as np

rows1 = int(input("Enter the number of rows for the first 2D array: "))
cols1 = int(input("Enter the number of columns for the first 2D array: "))

print("Enter the values for the first 2D array, row by row:")
values1 = []
for _ in range(rows1):
    row = input().split()
    row = [float(value) for value in row]
    values1.append(row)

array_2d_1 = np.array(values1)

rows2 = int(input("Enter the number of rows for the second 2D array: "))
cols2 = int(input("Enter the number of columns for the second 2D array: "))

print("Enter the values for the second 2D array, row by row:")
values2 = []
for _ in range(rows2):
    row = input().split()
    row = [float(value) for value in row]
    values2.append(row)

array_2d_2 = np.array(values2)

array_2d_subtracted = array_2d_1 - array_2d_2

print("Element-wise subtraction of the two 2D NumPy arrays:")
print(array_2d_subtracted)

# Output:
# Enter the number of rows for the first 2D array: 3
# Enter the number of columns for the first 2D array: 3
# Enter the values for the first 2D array, row by row:
# 1 2 3
# 4 5 6
# 7 8 9
# Enter the number of rows for the second 2D array: 3
# Enter the number of columns for the second 2D array: 3
# Enter the values for the second 2D array, row by row:
# 1 2 3
# 4 5 6
# 7 8 9
# Element-wise subtraction of the two 2D NumPy arrays:
# [[ 0.  0.  0.]
#  [ 0.  0.  0.]
#  [ 0.  0.  0.]]