class Solution():
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        for i in s:
            for j in t:
                if i==j:
                    t=t.replace(j,"",1)
                    s=s.replace(i,"",1)
        if s==t:
            return True
        else:
            return False
s="anagram"
t="nagaram"
sol=Solution()
print(sol.isAnagram(s,t))