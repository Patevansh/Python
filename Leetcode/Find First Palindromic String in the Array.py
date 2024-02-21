class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for i in words:
            if self.palin(i):
                return i
        return ""
    def palin(self,y):    
        if y==y[::-1]:
            return True
        else:
            return False