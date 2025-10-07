num = 6
s = sum(i for i in range(1, num) if num % i == 0)

if s == num:
    print("It is a perfect number")
else:
    print("It is not a perfect number")
