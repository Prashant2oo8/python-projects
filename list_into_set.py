
l = [139, 79, 105, 100, 89, 109]
print("Original list l:", l)
l_append = l.copy()
l_append.append(200)   
print("after append(200):", l_append)
l_insert = l.copy()
l_insert.insert(2, 999)          
print("after insert(2, 999):", l_insert)
l_extend = l.copy()
l_extend.extend([1,2,3])
print("after extend([1,2,3]):", l_extend)


set_l = set(l)
set_m = set(m)
print(" - set(l):", set_l)
print(" - set(m):", set_m)
print(" - union (set_l | set_m):", set_l | set_m)
print(" - difference (set_l - set_m):", set_l - set_m)
print(" - intersection (set_l & set_m):", set_l & set_m)
