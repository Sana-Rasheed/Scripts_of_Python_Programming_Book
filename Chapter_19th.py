
# Example 1
import numpy as np
mat = np.array([[1,2,3], [4,5,6], [7,8,9]])
print('The shape of mat is:', mat.shape) 
# Output: The shape of mat is: (3, 3)

# Example 2
# It can be reshaped to any shape that is consistent with the data size
new_mat = mat.reshape(1,9)
print('The shape of new_mat is:', new_mat.shape)
# Output: The shape of new_mat is: (1, 9)

# Example 3
# you can try transposing it as well.                                 
trans_new_mat = new_mat.T
print('The transposed shape of new_mat is:', trans_new_mat.shape)
# Output: The transposed shape of new_mat is: (9, 1)

# Example 4
# you can create diagonal matrices, identity matrices
diag = np.diag([1,2,3,4])
identity = np.identity(10) # creates a 10 x 10 matrix with ones at diagonals and rest zeros 

# Example 5
# you can create arrays of random numbers or sequences 
seq = np.arange(start=0, stop=100, step=5) # creates an array starting from 0, with a step size of 5 till 100. [0,5,10,....,90,95]

# Example 6
# If you only pass np.random.rand(10), it creates a 1D vector of length 10                            
rands_1d = np.random.rand(10)
rands_2d = np.random.rand(10, 10) # creates 10x10 matrix with random numbers. 


# Example 7
my_array = np.array([1,3,5,7,23,6,2,31,5]) 
# you can find min and max and min as well as the index of max number or min number                              
print('The max is {} at index {}'.format(my_array.max(), my_array.argmax()))                    
# Output:The max is 31 at index 7
print('The min is {} at index {}'.format(my_array.min(), my_array.argmin()))
# Output:  The min is 1 at index 0

# Example 8
import time 
# you can perform dot products of matrices in a matter of seconds 
my_mat = np.random.rand(1000, 1000)
another_mat = np.random.rand(1000, 1000)     
start = time.time()
# make sure the dimensions agree!
dot_mul = my_mat.dot(another_mat)
end = time.time()
print('It took {} seconds to calculate dot product!'.format(round(end-start, 4)))
# Output: It took 11.0579 seconds to calculate dot product!

start = time.time()
prod = my_mat * another_mat
end = time.time()
print('It took {} seconds to manully calculate dot product!'.format(round(end-start, 4)))
# Output: It took 0.026 seconds to calculate dot product!
 
# Example 9
import numpy as np # linear algebra 
import numpy.linalg as la 
my_mat = np.array([[1,2], [3,4]])

# calculate determinant
det = la.det(my_mat)
print('Det: ', det)
                                  
inverse_mat = la.inv(my_mat)
# calculate inverse of a matrix. Inv = adj(matrix)/det(matrix). NOTE: Make sure its not SINGULAR!
print('Inverse_mat: ', inverse_mat)

# calculate eigen values. NOTE: make sure the matrix is SQUARE  [eigen values do not exit     
# for matrix whose dimensions are mxn where m!=n]   
eig_values, eig_vectors = la.eig(my_mat)                           
print('Eigen values: ', eig_values, eig_vectors)

# calculate cholesky factorization. NOTE: make sure matrix is Positive Definite!
cholesky = la.cholesky(np.array([[7,2], [2,1]]))
print('Cholesky: ', cholesky)

# calculate rank of a matrix. Rank of a matrix is the number of linearly
# independent columns/rows in a matrix.#   
rank = la.matrix_rank(my_mat)   
print('Rank: ', rank)


