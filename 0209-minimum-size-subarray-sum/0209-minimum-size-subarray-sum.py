class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_size = float("inf")
        left = 0
        current_sum = 0
        for i in range (len(nums)):
            current_sum += nums[i]
            while current_sum >= target:
                min_size = min(min_size, i - left + 1)
                current_sum -= nums[left]
                left += 1
        return 0 if min_size == float("inf") else min_size
    
        