l = [139, 79, 105, 100, 89, 109]

m = [10, 20, 139]
merged = l + m
print("merged list (l + m):", merged)



evens = sum(1 for x in l if x % 2 == 0)
odds  = sum(1 for x in l if x % 2 != 0)
print("evens:", evens)
print(" odds:", odds)
