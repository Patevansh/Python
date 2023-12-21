class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            for i in range(len(nums)):
                if target==nums[i]:
                    return i
        else:
            return -1