nums = list(map(int, input("Enter numbers (end with -1): ").split(',')))
pos = [n for n in nums if n > 0]
neg = [n for n in nums if n < 0]

if pos:
    print("avg positive number is", sum(pos)//len(pos))
if neg:
    print("avg negative number is", sum(neg)//len(neg))
