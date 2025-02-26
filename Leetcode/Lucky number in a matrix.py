class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans=[]
        temp=[]
        l=len(matrix)
        for i in range(l):
            for j in range(len(matrix[0])):
                if i==0:
                    temp.append([matrix[i][j]])
                else:
                    temp[j].append(matrix[i][j])
        for i in range(l):
            for j in range(len(temp)):
                if min(matrix[i])==max(temp[j]):
                    ans.append(min(matrix[i]))
        return ans