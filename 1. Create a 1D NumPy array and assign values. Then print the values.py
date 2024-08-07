import numpy as np

values = input("Enter values for 1D array separated by spaces: ").split()
values = [float(value) for value in values]
array_1d = np.array(values)

print("1D NumPy Array:")
print(array_1d)


# Output:
# Enter values for 1D array separated by spaces: 1 2 3 4 5
# 1D NumPy Array:
# [1. 2. 3. 4. 5.]