class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y=str(x)
        if y==y[::-1]:
            return True
        else:
            False