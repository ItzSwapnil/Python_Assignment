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

constant = float(input("Enter a constant value to subtract from all elements: "))

array_2d_subtracted = array_2d - constant

print("2D NumPy Array after subtracting constant:")
print(array_2d_subtracted)

# Output:
# Enter the number of rows for the 2D array: 3
# Enter the number of columns for the 2D array: 3
# Enter the values for the 2D array, row by row:
# 1 2 3
# 4 5 6
# 7 8 9
# Enter a constant value to subtract from all elements: 10
# 2D NumPy Array after subtracting constant:
# [[-9. -8. -7.]
#  [-6. -5. -4.]
#  [-3. -2. -1.]]