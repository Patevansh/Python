class Solution(object):
    def minimumAddedCoins(self, coins, target):
        """
        :type coins: List[int]
        :type target: int
        :rtype: int
        """
        ex=re=0
        coins.sort()
        for c in coins:
            while re<(c-1):
                re+=re+1
                ex+=1
            re+=c
        while re<target:
            re+=re+1
            ex+=1
        return ex