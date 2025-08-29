from numpy import *

arr=array([
    [1,2,3,4],
    [5,6,7,8]
])

# arr2=arr.flatten()
arr3=arr.reshape(2,2,2)
print(arr3)

m1=matrix('1,2,3;6,7,8;2,3,4')
m2=matrix('1,2,3;4,5,6;2,3,5')
m3=m1*m2;
print(m3)