class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i=0
        k=""
        if needle in haystack:
            for j in range(len(haystack)):
                m=int(j+len(needle))
                k=haystack[j:m]
                if needle in k:
                    return j
        else:
            return -1