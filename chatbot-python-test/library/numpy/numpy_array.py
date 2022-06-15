import numpy as np

arr1 = np.array([1, 2, 3])
print(arr1)
print(type(arr1))

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

# 행렬 덧셈
arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6], [7, 8]])
arr5 = arr3 + arr4
print(arr5)

# 일반적인 행렬 곱과 행렬 스칼라 곱은 다르다!
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[1, 2], [3, 4], [5, 6]])
C = np.matmul(A, B)
print(C)