k=[]
t=int(input("Enter number of inputs:"))
for i in range(t):
  m=int(input(f"Enter {i+1} number:"))
  k.append(m)
print(f'Average of numbers is {sum(k)/len(k)}')