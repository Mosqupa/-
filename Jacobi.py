import numpy as np
import copy

def jacobi(A:np.array, x0:np.array, b:np.array) -> np.array:
     x0 = x0.astype(np.float64) # 把x0数组的数变成float型
     height = x0.shape[0] # 获取数组行数
     print("iteration times = 0 , original vector : ", x0)
     x1 = np.zeros(3)
     for i in range(height): # i取0,1,2
          sum = float(0)
          for j in range(height): # sum获取除当前待计算的x之外的aij*xj之和
               if j!=i:
                    sum += A[i][j]*x0[j]
          x1[i] = (b[i]-sum)/A[i][i] # 完成更新
     times = 1
     print("iteration times =", times, ", result : ", x1)
     while np.abs(np.max(np.abs(x0))-np.max(np.abs(x1))) > 10 ** -4:
          times += 1
          x0 = copy.deepcopy(x1)
          for i in range(height): # i取0,1,2
               sum = float(0)
               for j in range(height): # sum获取除当前待计算的x之外的aij*xj之和
                    if j!=i:
                         sum += A[i][j]*x0[j]
               x1[i] = (b[i]-sum)/A[i][i] # 完成更新
          print("iteration times =", times, ", result : ", x1)
     return x0

x0 = np.array([0,0,0])
A = np.array([[ 5, 2, 1],
              [-1, 4, 2],
              [ 2,-3, 10]])
b = np.array([-12,20,3])
jacobi(A, x0, b)