nums=[2,4,6,8]
#
it=iter(nums)
# # print(it)
#
print(next(it))
print(next(it))
print(next(it))
print(next(it))

class counter:

    def __init__(self,start,end):
        self.start=start
        self.end=end

    def __iter__(self):
        return self

    def __next__(self):
        nums = self.start
        if self.start<=self.end:

            self.start+=1
            return nums

        else:
            raise StopIteration

for nums in counter(1,5):
    print(nums)

