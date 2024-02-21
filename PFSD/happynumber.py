def happynum(n):
    sum = 0
    if n==1:
        return "Happy number"
    elif n<10:
        return "Non Happy number"
    else:
        while n!=0:
            temp=n%10
            n=n//10
            sum=sum+(temp**2)
        return happynum(sum)
n=int(input("Enter a number:"))
print(happynum(n))