nums = [4, 54, 29, 71, 59, 98, 23]

def is_prime(n):
    if n < 2: 
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

prime_count = sum(1 for x in nums if is_prime(x))
composite_count = sum(1 for x in nums if x > 1 and not is_prime(x))

print("Composite numbers =", composite_count)
print("Prime numbers =", prime_count)
