def lstinfuc(lst):
    even=0
    odd=0

    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1

    return even,odd

lst=[2,4,6,5,7,9]
even,odd=lstinfuc(lst)

print('even:',even)
print('odd:',odd)
