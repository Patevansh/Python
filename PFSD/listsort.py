import random
l=[]
def list_gen(n):
    for i in range(n):
        l.append(int(random.random()*100))
    print("\n",l)
n=int(input("Enter number of digits in list:"))
list_gen(n)
l.sort()
print("\n",l)
l.sort(reverse=True)
print("\n",l)
print("\nAvg=",sum(l)/len(l))