class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
       nums.sort()
       if len(nums) == 1:
            return 0
       diff = nums[k-1] - nums[0]
       min_diff = diff
       for i in range(0, len(nums)-k + 1 ):      
            diff = nums[i + k - 1] - nums[i]
            min_diff = min(diff, min_diff)
       return min_diff  
        