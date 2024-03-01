lucky=int(input("Enter your lucky number(0-9):"))
for i in range(10):
    if i==lucky:
        for j in range(10):
            print(i*10+j)
        continue
    print(i*10+lucky)