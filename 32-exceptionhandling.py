a=10
b=0

try:
    print('resources opened')
    print(a / b)
except ZeroDivisionError:
    print('Cannot divide number by 0')

try:
    k = int(input('Enter a number'))
    print(k)

except ValueError:
    print('Invalid input')


except Exception:
    print('Erroe occured')


finally:
    print('resources closed')






