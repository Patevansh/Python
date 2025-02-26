
profit=[10,5,15,7,6,18,3]
weight=[2,3,5,7,1,4,1]
mw=15
wpk=[]
maxweight=0
for i in range(len(profit)):
    wpk.append([profit[i]/weight[i],weight[i]])

wpk.sort(reverse=True)
for i in range(len(wpk)):
    if wpk[i][1]<mw:
        print("Total remaining weight:",mw)
        print("Profit and weight adding:",wpk[i][0]*wpk[i][1] , wpk[i][1])
        maxweight+=(wpk[i][0]*wpk[i][1])
    else:
        print("Total remaining weight:",mw)
        print("Profit and weight adding:",wpk[i][0]*mw ,mw)
        maxweight+=(wpk[i][0]*mw)
        break
    mw-=wpk[i][1]

print(maxweight)