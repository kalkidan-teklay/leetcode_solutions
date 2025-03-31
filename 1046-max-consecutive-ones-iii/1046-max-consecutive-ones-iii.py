class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        flip = 0
        max_length = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                flip += 1
            while flip > k:
                if nums[left] == 0:
                    flip -= 1 
                left += 1  
            max_length = max(max_length, right - left + 1)
        
        return max_length
