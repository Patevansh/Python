arr=[]
di={
    1:[2,3],
    2:[1,5],
    3:[1,4,6],
    4:[3],
    5:[2,7],
    6:[3,7],
    7:[5,6]
}
t=[[1,-1]]
flag=False
while t:
    q=t.pop()
    curr=q[0]
    parent=q[1]
    cur_adj=di[q[0]]
    if q[1]!=-1:
        di[q[0]].remove(q[1])
    for i in cur_adj:
        if i in arr:
            print("Loop Detected")
            flag=True
            break
        t.append([i,curr])
        arr.append(i)
    if flag:
        break
    if len(t)==0:
        print("No loop detected")

