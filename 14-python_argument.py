# def person(name,age):
#     print(f'hello i am {name} and my age is {age}')
#
# person(age=21,name='Raj')

# def person(name,age):
#     print(f'hello i am {name} and my age is {age}')
#
# person('Raj',21)

#default arg
# def person(name,age=14):
#     print(f'hello i am {name} and my age is {age}')
#
# person('Raj')

#variable length arg
# def add(a,*b):
#     c=a
#     for i in b:
#         c=c+i
#
#     print(c)
# add(2,5,6,70)

#key worded variable length arg
def person(name,**data):
    print(name)
    # print(data)
    for i,j in data.items():
        print(i,j)

person('Ram',age=12,city='delhi',mobile=86376873)



