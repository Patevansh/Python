class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        n=1
        while n==1:
            i=0
            k=[]
            n=0
            while i<len(intervals):
                for j in range(len(intervals)):
                    if j==i:
                        continue
                    if intervals[i][0]>=intervals[j][0] and intervals[j][1]>=intervals[i][0] and intervals[j][1]<=intervals[i][1]:
                        n=1
                        k.append([intervals[j][0],intervals[i][1]])
                        if len(intervals)==2:
                            intervals=[]
                            break
                        intervals.remove(intervals[i])
                        intervals.remove(intervals[j])
                        break
                    elif intervals[i][0]<intervals[j][0] and intervals[i][1]>intervals[j][1]:
                        intervals.pop(j)
            
                i+=1
            k=k+intervals
            intervals= k.copy()
        return intervals
sol=Solution()
p=[[1,4],[0,2],[3,5]]
print(sol.merge(p))