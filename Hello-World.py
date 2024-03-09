import numpy as np

A = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

B = np.array([[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])

print(np.multiply(A[ 0,:], B[ 1,: ]))

print("----------")

print(np.multiply(A[1,:], B[0,:]))
