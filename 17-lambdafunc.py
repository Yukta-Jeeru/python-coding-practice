from functools import reduce

f=lambda a,b:a+b
result=f(2,5)
print(result)

#filtering
nums=[2,3,4,5,6,7]

even=list(filter(lambda n:n%2==0,nums))
doubles=list(map(lambda n:n**2,even))
total=reduce(lambda a,b:a+b,even)
total1=reduce(lambda a,b:a+b,doubles)
print(even)
print(doubles)
print(total)
print(total1)
