arr=[]
s=int(input("Enter the size of array:"))
for i in range(s):
    arr.append(int(input(f'Enter {i+1} element:')))
k=int(input("Enter number position to reverse:"))
if k>=s:
    print("index not found")
"""m=arr[0:k]
n=arr[k:s]
arr=n+m"""
i=s-1
while i!=k-1:
    arr.insert(0,arr.pop(i))
    k+=1
print(arr)

