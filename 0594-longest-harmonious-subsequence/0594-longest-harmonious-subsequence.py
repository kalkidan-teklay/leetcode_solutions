class Solution:
    def findLHS(self, nums: List[int]) -> int:
        max_length = 0
        freq = defaultdict(int)
        for ch in nums:
            freq[ch] += 1
        for i in range (len(nums)):
              if (nums[i - 1] + 1) in freq:
                sum = freq[nums[i-1]+1] + freq[nums[i-1]]
                max_length = max(max_length , sum)
        return max_length
        