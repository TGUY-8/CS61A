def divisors(n):
    return [1] + [x for x in range(2, n) if n % x == 0]

[n for n in range(1000) if sum(divisors(n)) == n]
#[6, 28, 496]


