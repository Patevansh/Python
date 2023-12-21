class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=1
        while True:
            if i in nums:
                i+=1
            else:
                return i