count = 0
with open ("file1.txt", "r") as f:
    data = f.read()
    value = data.split(",")
    print(type(value))
    print(value)
    for i in value:
        if int(i.strip())%2==0: 
            print(i)
            count +=1
        else:
            continue
print(count)