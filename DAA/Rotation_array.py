arr=[1,2,3,4,5,6,7]
r=int(input("Enter a number:"))
l=len(arr)
# for i in range(r):
#     arr.append(arr.pop(0))
# print(arr)

for i in range(r):
    for j in range(l-1):
        arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)