class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p)==1 and len(s)>1:
            return False
        for i in range(len(s)-1):
            if i>=len(p):
                return False
            if p[i+1]=="*":
                if p[i]==".":
                    while p[i+1]!=s[i]:
                        s=s.replace(s[i],"",1)
                elif s[i]!=p[i]:
                    p.replace(p[i],"",1)
                elif s[i]==p[i]:
                    while s[i]==p[i]:
                        if len(s)==1:
                            return True
                        s=s.replace(s[i],"",1)
                else:
                    return False
            elif p[i]==s[i]:
                continue
            elif p[i]==".":
                continue
            else:
                return False
        return True
sol=Solution()
print(sol.isMatch("aa","a*"))