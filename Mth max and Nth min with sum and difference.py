arr = [14, 16, 87, 36, 25, 89, 34]
M, N = 1, 3
arr.sort()
nth_min = arr[N-1]
mth_max = arr[-M]

print(f"{M}st Maximum Number =", mth_max)
print(f"{N}rd Minimum Number =", nth_min)
print("Sum =", mth_max + nth_min)
print("Difference =", mth_max - nth_min)
