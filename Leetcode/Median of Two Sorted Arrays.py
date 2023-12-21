class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        c=nums1+nums2
        c.sort()
        l=int(len(c)/2)-1
        if len(c)%2==0:
            k=int(c[l])+int(c[l+1])
            m=k/2
        else:
            m=c[l]
        return m
sol=Solution()
nums1=[1,2,3]
nums2=[4,5,6]
print(sol.findMedianSortedArrays(nums1,nums2))