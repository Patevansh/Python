class Solution(object):
    def longestPalindrome(self, s):
        a = 0
        b = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j] == s[i:j][::-1]:
                    if j - i > a:
                        a = j - i
                        b = s[i:j]
        return b

sol = Solution()
s = "babad"
print(sol.longestPalindrome(s))