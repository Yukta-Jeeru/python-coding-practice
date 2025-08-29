def searchitem(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return (i)

    return -1

arr=[2,4,6,8]
targetitem=8

result=searchitem(arr,targetitem)

if result!=-1:
    print('Found at index',result)

else:
    print('Value not found')


### **Dry Run Table**
#
# | Step | `i` (index) | `arr[i]` (value) | Compare `arr[i] == targetitem` | Action Taken             | Returned Value (`result`) |
# | ---- | ----------- | ---------------- | ------------------------------ | ------------------------ | ------------------------- |
# | 1    | 0           | 2                | `2 == 8` → False               | Continue loop            | —                         |
# | 2    | 1           | 4                | `4 == 8` → False               | Continue loop            | —                         |
# | 3    | 2           | 6                | `6 == 8` → False               | Continue loop            | —                         |
# | 4    | 3           | 8                | `8 == 8` → True                | `return 3` (index found) | `result = 3`              |
#
# ---
#
# ### **What happens in the `if` check?**
#
# * `result` now equals `3`
# * The condition `if result != -1:` → `3 != -1` → **True** → `"Found at index 3"` is printed.
#
# ---
#
# ### **Why `if result == targetitem` fails**
#
# If you change the check to:
#
# ```python
# if result == targetitem:
# ```
#
# You are now comparing:
#
# * `result` → **3** (index)
# * `targetitem` → **8** (value you searched for)
#
# `3 == 8` → **False** → `"Value not found"` is printed — even though it’s in the array.


