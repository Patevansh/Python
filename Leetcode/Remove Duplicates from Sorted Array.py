class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        k=len(nums)-1
        i=0
        m=0
        while k>i:
            if nums[i]==nums[i+1]:
                nums.remove(nums[i])
                k-=1
            else:
                i+=1
        for i in range(len(nums)):
            m+=1
        return m