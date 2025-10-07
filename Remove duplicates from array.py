arr = list(map(int, input("Enter array elements: ").split(',')))
unique = list(dict.fromkeys(arr))
print("duplicate array =", unique)
