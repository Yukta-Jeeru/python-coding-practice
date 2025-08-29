def factorial(n):

    f=1
    for i in range(1,n+1):
        f=f*i
    return f

x=5
result=factorial(x)
print(result)

#with recursion
def factorialwithrec(n):
    if n==0:
        return 1

    return n * factorialwithrec(n-1)

result=factorialwithrec(5)
print(result)