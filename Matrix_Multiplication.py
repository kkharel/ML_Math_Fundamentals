# Matrix Multiplication

def matrix_multiply(matrix_a, matrix_b):
  
  row_a, column_a = len(matrix_a), len(matrix_a[0])
  row_b, column_b = len(matrix_b), len(matrix_b[0])
  
  if column_a != row_b:
    raise ValueError("Matrix Dimension not compatible for multiplication")
  
  # result matrix
  matrix_c = [[0*len(matrix_a) for i in range(column_b)] for j in range(row_a)]
  
  for i in range(row_a):
    for j in range(column_b):
      for k in range(column_a):
        matrix_c[i][j] += matrix_a[i][k] * matrix_b[k][j]
        
  return matrix_c


mat1 = [[1,2,3],[4,5,6]]
mat2 = [[7,8],[9,10],[11,12]]

matrix_multiply(mat1, mat2)
     
     
# Sparse Matrix Multiplication -- (most of the entries in a matrix are zero)

def sparse_matrix_multiplication(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b): # not valid matrix multiplication
        return [[]]

    matrix_c = [] # initialize empty matrix c

    for i in range(len(matrix_a)): # for row in matrix a
        arr = [] # initialize empty arr
        for j in range(len(matrix_b[0])): # for column in matrix b
            arr.append(0) # append 0 to array for every column in matrix b
        matrix_c.append(arr) # append array to matrix c for every row in matrix a

    for i in range(len(matrix_c)): # for every row in matrix c
        for j in range(len(matrix_c[0])): # for every column in matrix c
            for k in range(len(matrix_b)): # used to perform dot product during matmul. Iterates over common dimension (number of columns) of matrix a and matrix b. k represents index of common dimension
                if matrix_a[i][k] == 0 or matrix_b[k][j] == 0:  # check if either element in matrix_a or matrix_b is zero
                    continue    
                matrix_c[i][j] += matrix_a[i][k] * matrix_b[k][j]
        
    return matrix_c



mat1 = [[1,0,0],[0,1,0],[1,0,0]]
mat2 = [[1,2,2],[2,1,3],[-1,-2,-5]]

sparse_matrix_multiply(mat1,mat2)

# using library
import numpy as np
def sparse_matrix_multiplication(matrix_a, matrix_b):
    try:
        return (np.dot(np.array(matrix_a), np.array(matrix_b))).tolist()
    except:
        return [[]]
