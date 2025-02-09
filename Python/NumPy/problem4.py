import numpy as np

x = np.arange(1, 10)

arr1 = x[:4]   
arr2 = x[4:6]  
arr3 = x[6:]   

print(arr1)  # [1 2 3 4]
print(arr2)  # [5 6]
print(arr3)  # [7 8 9]

