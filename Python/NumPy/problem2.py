import numpy as np
arr1 =np.array([[1,2,3] , [4,5,6]])
arr2 = arr1.ravel(order='F')
print (arr1)
print("*" * 20)
print (arr2)