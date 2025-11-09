val = int(input('enter any value:'))
sum = 0
temp= val
digit = len(str(val))

while temp>0:
    rem=temp%10
    sum+=rem**digit
    temp//=10

if sum == val:
    print(f"{val} is a armstrong number")
else:
    print(f"{val} is not armstrong number")






