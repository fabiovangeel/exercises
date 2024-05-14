from itertools import count


def is_prime(n):
    return n >= 2 and all(n % i != 0 for i in range(2, n))


def primes():
    return (n for n in count(2) if is_prime(n))
