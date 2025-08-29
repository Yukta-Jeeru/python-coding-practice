def sort_items(num):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if num[j]<num[j+1]:
                temp=num[j]
                num[j]=num[j+1]
                num[j+1]=temp

arr=[1,6,4,7,3]
sort_items(arr)

print(arr)