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
    row_a, column_a = len(matrix_a), len(matrix_a[0])
    row_b, column_b = len(matrix_b), len(matrix_b[0])

    if column_a != row_b:
        raise ValueError("Matrix Multiplication not valid")

    sparse_a = get_dict(matrix_a)
    sparse_b = get_dict(matrix_b)

    matrix_c = [[0*len(matrix_b[0]) for _ in range(column_b)] for _ in range(row_a)]

    for (i, k) in sparse_a:
        for j in range(column_b):
            if (k, j) in sparse_b:
                matrix_c[i][j] += sparse_a[(i, k)] * sparse_b[(k, j)]

    return matrix_c

def get_dict(matrix):
    dictionary = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                dictionary[(i, j)] = matrix[i][j]
    return dictionary



mat1 = [[1,0,0],[0,1,0],[1,0,0]]
mat2 = [[1,2,2],[2,1,3],[-1,-2,-5]]

sparse_matrix_multiply(mat1,mat2)

    
