num=int(input("Enter a number:"))
countnum=0
nums=[]
k=num
while(k!=0):
    countnum+=1
    nums.append(k%10)
    k=int(k/10)
print("Number of digits : ",countnum)
out=0
print("Divisible numbers:")
for i in nums:
    if i==0:
        continue
    if num%i==0:
        print(i)
        out+=1
print("Total divisible number:",out)
    