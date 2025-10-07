a = tuple(map(int, input("Enter first tuple: ").split(',')))
b = tuple(map(int, input("Enter second tuple: ").split(',')))
inter = tuple(set(a) & set(b))
print(inter)
