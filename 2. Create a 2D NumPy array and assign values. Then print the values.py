import numpy as np

rows = int(input("Enter the number of rows for the 2D array: "))
cols = int(input("Enter the number of columns for the 2D array: "))

print("Enter the values for the 2D array, row by row:")
values = []
for _ in range(rows):
    row = input().split()
    row = [float(value) for value in row]
    values.append(row)

array_2d = np.array(values)

print("2D NumPy Array:")
print(array_2d)

# Output:
# Enter the number of rows for the 2D array: 3
# Enter the number of columns for the 2D array: 3
# Enter the values for the 2D array, row by row:
# 1 2 3
# 4 5 6
# 7 8 9
# 2D NumPy Array:
# [[1. 2. 3.]
#  [4. 5. 6.]
#  [7. 8. 9.]]
