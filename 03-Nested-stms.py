x=int(input('Enter a number:'))
y=x % 2

if y==0:
    print('It is an even number')
    if x<0:
        print('Its negative')
    else:
        print('Its positive')

else:
    print('It is an odd number')
    if x<0:
        print('Its negative')
    else:
        print('Its positive')