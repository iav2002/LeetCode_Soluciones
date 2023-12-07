# The version of Sliding Window (commmon)
# left: the leftmost index of our current window
# right: the rightmost index of our current window
# curr: the sum of our current window
# ans: the length of the longest valid window we have seen so far

def find_length(nums, k):
    # curr is the current sum of the window
    left = curr = ans = 0
    for right in range(len(nums)):
        curr += nums[right]
        while curr > k:
            curr -= nums[left]
            left += 1
        ans = max(ans, right - left + 1)
    
    return ans

# finding the subArray of products that is less than K
def numSubarrayProductLessThanK(self, nums: [int], k: int) -> int:
    if k <= 1:
        return 0

    ans = left = 0
    curr = 1

    for right in range(len(nums)):
        curr *= nums[right]
        while curr >= k:
            curr //= nums[left] 
            left += 1
        ans += right - left + 1

    return ans

#SlidingWindowFixed
def find_best_subarray(nums, k):
    curr = 0
    for i in range(k):
        curr += nums[i]
    
    ans = curr
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i - k]
        ans = max(ans, curr)
    
    return ans

# 643. Maximum Average Subarray I, only divide ans in K
# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000

    def findMaxAverage(nums : [], k : int) -> float:
        curr = 0
        for i in range(k):
            curr += nums[i]

        ans = curr

        for i in range(k, len(nums)):
            
            
            curr += nums[i] - nums[i - k]
            ans = max(ans, curr)

        return ans/k



