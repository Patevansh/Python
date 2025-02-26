class Operations():
    arr=[]
    def __init__(self):
        for i in range(10):
            self.arr.append([])
    
    def arrin(self,val):
        t=val%10 
        self.arr[t].append(val)
        self.arr[t].sort()

    def arrshow(self):
        print("Array :",end=" ")
        for i in self.arr:
            for j in i:
                print(j,end=" ")
        print()

    def arrSearch(self,val):
        t=val%10
        ar=self.arr[t]
        for i in ar:
            if i==val:
                return i
        else:
            return -1
    

op=Operations()
while True:
    n=int(input("1)Insert\n2)Show all element\n3)Search\n4)Exit\nEnter your input:"))
    if n==1:
        op.arrin(int(input("Enter a number:")))
    elif n==2:
        op.arrshow()
    elif n==3:
        tem=op.arrSearch(int(input("Enter a number to search:")))
        if tem==-1:
            print("Nummber not found.")
        else:
            print("Number Found.")
    else:
        break

