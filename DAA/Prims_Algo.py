dic={ 0: [[1, 2], [3, 6]],
 1: [[0, 2], [2, 3], [3, 8], [4, 5]],
 2: [[1, 3], [4, 7]],
 3: [[0, 6], [1, 8]],
 4: [[1, 5], [2, 7]]}
arr=[]
pq=[(0,0,-1)]
sumMin=0
mst=[]
while pq:
    ar=min(pq)
    pq.remove(ar)
    cr=ar[1]
    we=ar[0]
    pa=ar[2]
    if cr in arr:
        continue
    for i in range(len(dic[cr])):
        if dic[cr][i][1]==pa:
            continue
        pq.append((dic[cr][i][1],dic[cr][i][0],cr))
    arr.append(cr)
    if pa!=-1:
        mst.append((pa,cr))
        sumMin+=we
print(mst)
print(sumMin)