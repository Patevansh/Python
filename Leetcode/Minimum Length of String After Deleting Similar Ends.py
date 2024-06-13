class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=len(s)
        if l==0:
            return 0
        if l==1:
            return 1
        if l==2:
            if s[0]==s[1]:
                return 0
        if(s[0]!=s[l-1]):
            return l
        else:
            if(s[1]==s[0]):
                return self.minimumLength(s[1:l])
            elif(s[l-1]==s[l-2]):
                return self.minimumLength(s[0:l-1])
            else:
                return self.minimumLength(s[i:l-1])
    
S=Solution()
print(S.minimumLength("cabaabac"))