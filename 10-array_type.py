from array import *

vals=array('i',[45,8,-8,87])
print(vals)

print(vals.buffer_info())
print(len(vals))

vals.reverse()
print(vals)