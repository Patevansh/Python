class Solution(object):
    def letterCombinations(self, digits):
        all=["2abc","3def","4ghi","5jkl","6mno","7pqrs","8tuv","9wxyz"]
        e=[]
        c=[]
        if int(digits)/10==0:
            for i in all:
                if digits==i[0]:
                    for j in range(1,len(i)):
                        c.append(i[j])
                    return c
        for i in digits:
            for j in all:
                if i==j[0]:
                    e.append(j)
        for i in range(len(e)):
            for j in range(len(e)):
                for m in range(1,len(e[i])):
                    for k in range(1,len(e[j])):
                        if [i]==[j]:
                            break
                        k=e[i][m]+e[j][k]
                        c.append(k)
        e=[]
        for i in range(int(len(c)/2)):
            e.append(c[i])
        return e
sol=Solution()
print(sol.letterCombinations("25"))