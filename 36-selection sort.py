def sort(num):

    n = len(num)
    for i in range(n):
        minpos=i
        for j in range(i,n): #current pos to n
            if num[j]<num[minpos]:
                minpos=j

        temp=num[i]
        num[i]=num[minpos]
        num[minpos]=temp

num=[5,3,8,6,7,2]
sort(num)

print(num)
