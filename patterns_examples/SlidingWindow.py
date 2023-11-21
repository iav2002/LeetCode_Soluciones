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