
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

