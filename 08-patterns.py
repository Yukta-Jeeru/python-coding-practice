for i in range(4):
    for j in range(4):
        print('#', end=' ')

    print()

for i in range(1,5):        #we can put range 4
    for j in range(i):      #i+1
        print('#', end=' ')

    print()

for i in range(1,5):    #range 4
    for j in range(4-i):
        print('#', end=' ')

    print()
