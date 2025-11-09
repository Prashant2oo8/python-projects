
l = [139, 79, 105, 100, 89, 109]
print("Original list l:", l)
l_append = l.copy()
l_append.append(200)   
print(" - after append(200):", l_append)
l_insert = l.copy()
l_insert.insert(2, 999)          
print(" - after insert(2, 999):", l_insert)
l_extend = l.copy()
l_extend.extend([1,2,3])
print(" - after extend([1,2,3]):", l_extend)
print("\n2) DELETE using remove (what you might mean by 'rename') and del")
l_del_examples = l.copy()
l_remove = l_del_examples.copy()
l_remove.remove(100)
print(" - after remove(100):", l_remove)
l_del = l_del_examples.copy()
del l_del[1]
print(" - after del l[1]:", l_del)
renamed_list = l.copy()
print(" - renamed_list (alias of l):", renamed_list)
print("\n3) UPDATE, max, 2nd largest, min, 2nd smallest")
l_update = l.copy()
l_update[3] = 150
print(" - after updating index 3 to 150:", l_update)
max_val = max(l)
min_val = min(l)
unique_sorted = sorted(set(l))
second_largest = unique_sorted[-2] if len(unique_sorted) >= 2 else None
second_smallest = unique_sorted[1] if len(unique_sorted) >= 2 else None
print(" - max:", max_val)
print(" - 2nd largest:", second_largest)
print(" - min:", min_val)
print(" - 2nd smallest:", second_smallest)

print("\n4) MERGE (concatenate) with another list m = [10, 20, 139]")
m = [10, 20, 139]
merged = l + m
print(" - merged list (l + m):", merged)

print("\n5) COUNT even and odd numbers")
evens = sum(1 for x in l if x % 2 == 0)
odds  = sum(1 for x in l if x % 2 != 0)
print(" - evens:", evens, " odd(s):", odds)

print("\n6) LINEAR SEARCH function (returns index of first match or -1)")
def linear_search(arr, target):
    for i, v in enumerate(arr):
        if v == target:
            return i
    return -1

targets = [105, 42]
for t in targets:
    idx = linear_search(l, t)
    print(f" - linear_search(l, {t}) ->", idx if idx != -1 else "not found")

print("\n7) SORT in ascending and descending (non-destructive: create copies)")
asc = sorted(l)
desc = sorted(l, reverse=True)
print(" - ascending:", asc)
print(" - descending:", desc)

print("\n8) BINARY SEARCH on a sorted list (ascending)")
def binary_search(arr, target):
    lo, hi = 0, len(arr)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

sorted_l = asc
for t in [100, 105, 139]:
    print(f" - binary_search(sorted_l, {t}) ->", binary_search(sorted_l, t))

print("\n9) Convert to set and perform union, difference (minus), and intersection (&)")
set_l = set(l)
set_m = set(m)
print(" - set(l):", set_l)
print(" - set(m):", set_m)
print(" - union (set_l | set_m):", set_l | set_m)
print(" - difference (set_l - set_m):", set_l - set_m)
print(" - intersection (set_l & set_m):", set_l & set_m)

print("\n--- Final summary ---")
print("Original l:", l)
print("l after example append (not changing original):", l_append)
print("l after example insert (not changing original):", l_insert)
print("l after example extend (not changing original):", l_extend)
print("Merged (l + m):", merged)
print("Sorted ascending:", asc)
print("Sorted descending:", desc)