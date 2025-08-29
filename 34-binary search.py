def search(arr,target):
    low=-0
    high=len(arr)-1

    while low<=high:
        mid=(low+high)//2

        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1


arr=[2,4,6,8,10,12,14]
target_item=12

result=search(arr,target_item)

if result!=-1:
    print('Value found at index',result)

else:
    print('Value not found')