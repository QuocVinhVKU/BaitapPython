def is_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return "YES"
    return "NO"

n = int(input())
print(is_prime(n))