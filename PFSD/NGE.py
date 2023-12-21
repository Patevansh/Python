def maxele(li,e):
  a=b=-1
  for i in range(len(li)):
    if li[i]==e:
      a=i
      b=e
    elif a!=-1:
      if b<li[i]:
        b=li[i]
  if b==e:
    return -1
  return b
li=[]
print("NGE FINDER")
while True:
  k=int(input("1)Add element in list\n2)Find NGE\nEnter your option:"))
  if k==1:
    el=int(input("Enter element:"))
    li.append(el)
  elif k==2:
    break
  else:
    print("Wrong input\n")
for i in li:
  print(f'{i} -- {maxele(li,i)}')