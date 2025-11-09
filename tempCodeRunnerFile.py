num = int(input("enter the no of rows: "))
for i in range(0, num):
    for j in range(i):
        print(end=" ")
    
    for j in range(0, 2*num-2*i-1):
        print("*", end=" ")