# Вывести на экран 1001 простое число.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def first_n_primes(n):
    primes = []
    num = 1
    while len(primes) < n:
        num += 1
        if is_prime(num):
            primes.append(num)
    return primes

primes = first_n_primes(1001)

for prime in primes:
    print(prime)