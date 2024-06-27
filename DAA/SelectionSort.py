arr=[3,5,9,2,1,7,0]
l=len(arr)
for i in range(l):
    temp=i
    for j in range(i+1,l):
        if arr[i]>arr[j]:
            if arr[temp]>arr[j]:
                temp=j
    arr[i],arr[temp]=arr[temp],arr[i]
print(arr)

            