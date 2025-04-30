class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_Area = 0
        left, right = 0, len(height)-1
        for i in range(len(height)):
            width = right - left
            if height[left] >= height[right]:
                area = height[right] * width
                right -=1
            else:
                area = height[left] * width
                left+= 1
            max_Area = max(max_Area, area)
        return max_Area
        