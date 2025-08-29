from array import *
# vals=array('i',[56,87,44,77])
#
# newArr=array(vals.typecode,(a for a in vals))
#
# for e in newArr:
#     print(e)

# vals=array('i',[5,7,4,7])
#
# newArr=array(vals.typecode,(a*a for a in vals))
#
# for e in newArr:
#     print(e)

#Array values from user
arr=array('i',[])

total_vals=int(input('Enter the total values:'))

for i in range(total_vals):
    x=int(input('Enter the value:'))
    arr.append(x)
print(arr)

val=int(input('enter the value for search '))

k=0
for e in arr:
    if e==val:
        print(k)

    k+=1

print(arr.index(val))



