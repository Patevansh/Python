def Searcharr(arr,l,r,t):
    m=int((r+l)/2)
    if arr[m]==t:
        return m
    elif r<l:
        return l
    elif arr[m]>t:
        return Searcharr(arr,l,m-1,t)
    else:
        return Searcharr(arr,m+1,r,t)
arr=[1,3,4,6,8,10]
r=len(arr)
t=7
print(Searcharr(arr,0,r,t))