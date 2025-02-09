import numpy as np

arr1 = np.ones((10 ,10 ,3))
arr2 = arr1.reshape(-1 , 150 )

print(arr2.shape)
