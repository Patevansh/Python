class Solution():
    def destCity(self, paths):
        if len(paths)==0:
            return paths[0][1]
        i=e=0
        j=len(paths)
        while True:
            for k in range(len(paths)):
                if paths[i][1]==paths[k][0]:
                    i=k
                    e=0
                else:
                    e+=1
                    if e==j:
                        return paths[i][1]
sol=Solution()
paths =[["qMTSlfgZlC","ePvzZaqLXj"],["xKhZXfuBeC","TtnllZpKKg"],["ePvzZaqLXj","sxrvXFcqgG"],["sxrvXFcqgG","xKhZXfuBeC"],["TtnllZpKKg","OAxMijOZgW"]]
print(sol.destCity(paths))