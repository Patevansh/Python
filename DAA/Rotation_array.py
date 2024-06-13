arr=[1,2,3,4,5,6,7]
r=int(input("Enter a number:"))
for i in range(r):
    arr.append(arr[0])
    arr.remove(arr[0])
print(arr)