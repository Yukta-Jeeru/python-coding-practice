a=10

def something():
    a = 9
    print("Inside:",a)

    x=globals()['a']=20
    # globals()['a']=20

something()
print("Outside:", a)
print(a)