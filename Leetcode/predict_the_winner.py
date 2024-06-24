global p1,p2
p1=p2=0
class Solution():
    def ptw(self,ar,l,r,t):
        global p1,p2
        if l==r:
            return ar[r]
        if t!=1:
            t=1
            tl=self.ptw(ar,l+1,r,t)
            tr=self.ptw(ar,l,r-1,t)
            if tl>tr:
                p2+=ar[l]
                return ar[l]
            else:
                p2+=ar[r]
                return ar[r]
        else:
            t=2
            tl=self.ptw(ar,l+1,r,t)
            tr=self.ptw(ar,l,r-1,t)
            if tl>tr:
                p1+=ar[l]
                return ar[l]
            else:
                p1+=ar[r]
                return ar[r]
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        global p1,p2
        l=0
        r=len(nums)-1
        t=1
        self.ptw(nums,l,r,t)
        if p1>=p2:
            return True 
        else:
            return False

a=[5,10,4,6]
s=Solution()
print(s.predictTheWinner(a))
print(p1,p2)