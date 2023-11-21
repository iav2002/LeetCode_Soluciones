# def check_for_target(nums, target):
#     left = 0
#     right = len(nums) - 1

#     while left < right:
#         # curr is the current sum
#         if nums[left] + nums[right] == target:
#             return True
#         elif nums[left] + nums[right]> target:
#             right -= 1
#         elif nums[left] + nums[right]:
#             left += 1
    
#     return False


# ## Combining two sorted arrays in O(n) instead of using 0(n log N)
# def combine(arr1, arr2):
#     # ans is the answer
#     ans = []
#     i = j = 0
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] < arr2[j]:
#             ans.append(arr1[i])
#             i += 1
#         else:
#             ans.append(arr2[j])
#             j += 1
    
#     while i < len(arr1):
#         ans.append(arr1[i])
#         i += 1
    
#     while j < len(arr2):
#         ans.append(arr2[j])
#         j += 1
    
#     return ans

def sortedSquares(nums: list[int]):
    numero = nums[0]
    ans = []
    for i in nums:
        square =  numero * numero
        ans.append(square)

    return ans

nums = [2,2,3,4,5,6]

print(sortedSquares(nums))