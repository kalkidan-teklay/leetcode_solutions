class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq = [0] * len(nums)
        left, right = 0, len(nums) -1
        for i in range(len(nums)-1, -1, -1):
            if abs(nums[right]) > abs(nums[left]):
                sq[i] = nums[right]  ** 2
                right -=1
            else:
                sq[i] = nums[left] **2
                left +=1
        return sq
