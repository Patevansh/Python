class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        prices.sort()
        a=prices[1]+prices[0]
        if money<a:
            return money
        else:
            return money-a