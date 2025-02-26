str=" ababcabcababbd "
pattern=" ababd"
l=len(str)
m=len(pattern)
ap=[]
for i in pattern:
    t=-1
    for j in range(len(ap)):
        if i==ap[j][0]:
            t=j
            break
    ap.append([i,t+1])
i=1
j=0
tm=0
print(ap)
while j<m-1:
    if str[i]==ap[j+1][0]:
        i+=1
        j+=1
    else:
        if tm==0:    
            if j<=0:
                j=ap[j][1]
            tm=1
        else:
            tm==0
            i+=1
    if i==l:
        print("Not",end=" ")
        break
print("Found")