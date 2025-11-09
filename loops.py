#n = int(input("enter any no: "))
# i = 1
# while i <=10:
#     print(i*i)
#     i+=1
# num = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while i<len(num):
#     print(num[i])
#     i+=1

# tup = (1,4,9,16,25,36,49,64,81,100)
# n = int(input("enter any no u want to search: "))
# i = 0 
# while i<len(tup):
#     if (n==tup[i]):
#         print("number is found at ",i)
#     else:
#         print("finding")
# #     i+=1
# t = ("c","d","a","a","b","b","a")
# for ch in t:
# #     print(ch)
# lst = (1,4,9,16,25,36,49,64,81,100)
# n = int(input("enter any no u want to search: "))
# idx = 0
# for e in lst:
#     if (n==e):
#         print("element found at", idx)
# #     idx+=1
n = int(input("enter any no : "))
# for i in range(1,11):
# #     print(i*n)
# count = 0
# i = 0
# while(i<=n):
#     count+=i
#     i+=1
# print(count)
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)
