class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=""
        b=""
        c=t=0
        for i in range(len(s)-1):
            a+=s[i]
            for j in range(i+1,len(s)):
                b+=s[j]
            for m in range(len(a)):
                if m<=len(a) and a[m]=="0":
                    t+=1
            for m in range(len(b)):
                if m<=len(b) and b[m]=="1":
                    t+=1
            if c<t:
                c=t
            t=0
            b=""
        return c