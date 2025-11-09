l = [139, 79, 105, 100, 89, 109]

def linear_search(arr, target):
    for i, v in enumerate(arr):
        if v == target:
            return i
    return -1

targets = [105, 42]
for t in targets:
    idx = linear_search(l, t)
    print(f"linear_search(l, {t}) =", idx if idx != -1 else "not found")

asc = sorted(l)
desc = sorted(l, reverse=True)
print("ascending:", asc)
print("descending:", desc)

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
    print(f"binary_search(sorted_l, {t}) =", binary_search(sorted_l, t))
