class Solution(object):
    def searchRange(self, nums, target):
        t=[]
        k=[]
        if target not in nums:
            return [-1,-1]
        for i in range(len(nums)):
            if nums[i]==target:
                t.append(i)
        if len(t)==1:
            t.append(t[0])
        elif len(t)>2:
            k.append(t[0])
            t.sort(reverse=True)
            k.append(t[0])
            t=k
        return t