class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        common = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j] and nums1[i] not in common:
                    common.append(nums1[i])
        return common
        