nums = [22,11,22,44,34,23,22,11]

sorted(nums)
l = 0
curr = 0
maximunm= 0

for num in len(nums):
    if  nums[l] == nums[l+1]:
        curr += 1
        
