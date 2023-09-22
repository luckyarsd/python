import numpy as np
x = np.array([1,2,3,4])  # Creation of array
print(x)
print(type(x))



import numpy as np
l = []
for i in range(0,6):
  x= int(input("Enter: "))
  l.append(x)
array = np.array(l)
array = array.reshape([2,3])
print(array)



import numpy as np
y = np.array([[1,2,3] ,[4,5,6]]) # creation of 2-d arrays
print(y)



import numpy as np
y = np.array([[[1,2,3] ,[4,5,6]]]) # creation of 3-d arrays
print(y)



import numpy as np
y = np.array([[1,2,3] ,[4,5,6]], ndmin=10) # creation of n-d arrays using ndmin function
print(y)



import numpy as np
x = np.array([[[1,2,3] ,[4,5,6]]]) # creation of 3-d arrays
print(x)
print(x.ndim)
print()
y = np.array([1,2,3,4], ndmin=10)  # creation of n-d arrays using ndmin function
print(y)
print(y.ndim)# Checking the dimensions of arrays


import numpy as np
zero = np.zeros(4)    # Here np.zero(4) will create zeros matrix with 1 row( default) & 4 columns
print(zero)



import numpy as np
zero = np.zeros([3,4] , dtype=int)   # Here np.zero(4) will create zeros matrix with 3 rows & 4 columns
print(zero)

print()
import numpy as np
zero = np.zeros([3,4] , dtype=float)   # Here dtype is float means all element of matrices are in float datatypes
print(zero)

print()
import numpy as np
zero = np.zeros([3,4] , dtype=complex)   # Here dtype is float means all element of matrices are in complex datatypes
print(zero)



import numpy as np
once = np.ones(4)     # Here np.ones(4) will create singular matrix with 1 row( default) & 4 columns
print(once)


import numpy as np
once = np.ones([3,4])     # Here np.ones(4) will create singular matrix with with 3 rows & 4 columns
print(once)



import numpy as np
identity = np.identity(4)   # Here np.identity(4) will create singular matrix with with 4 rows & 4 columns (it always creats square matrice)
print(identity)



import numpy as np
empty = np.empty([2,2]) # Here np.empty will create empty matrix with order 2*2
print(empty)



import numpy as np
arange = np.arange(6)    # Here np.arange will cretae a matrices with range from 0 to 5 (0 t n-1)
arange = arange.reshape([2,3])   #Here reshape function is used to reshape the matrix
print(arange)



import numpy as np
full = np.full([2,2] , 10)   # Here np.full functon will fill the matrix element with given number
print(full)
print()
full2 = np.full([3,3] , np.inf)   # Here np.full functon will fill the matrix element with inf
print(full2)



import numpy as np
arange = np.arange(6)
arr = np.ones_like(arange)  # Like function creates a matrix as same order of passes variable with given like identifier
print(arange)
print()
print(arr)
