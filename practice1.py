# def length_list(lst):
#     for i in lst:
#         print(i,end=" ")

# lst = [1,2,3,4,5,1,2,1,2,1]
# # length_list(lst)
# usd = 100

# def converter(usd):
#     print("inr = ", 83*usd)  

# converter(usd)

# def check(n):
#     if n%2==0 :
#         print("even")
#     else:
#         print("odd")


# num = int(input("enter any no : "))
# check(num)


def printElement (lst, idx):
    if idx==len(lst):
        return
    print(lst[idx])

    printElement (lst, idx + 1)    


lst = [1,2,3,4,5,1,2,1,2,1]
printElement(lst, 0)
