class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i]==target:
                return i
            elif i<len(nums)-1:
                if nums[i]<target and target<nums[i+1]:
                    return i+1
            elif target<nums[0]:
                return 0
        return len(nums)