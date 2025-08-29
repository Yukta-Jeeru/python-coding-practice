def count_up_to(n):

    nums=1
    while nums<=n:
        yield nums
        nums += 1



for nums in count_up_to(5):
    print(nums)