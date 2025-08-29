from math import sqrt

def improve(update , close, guess = 1):
    while not close(guess):
        guess = update(guess)
    return guess

def golden_update(guess):
    return 1/guess + 1

def approx_eq(x , y , tolerance = 1e - 15):
    return abs(x - y) < tolerance

def square_close_to_successor(guess):
    return approx_eq(guess * guess, guess , guess + 1)

phi = 1/2 + sqrt(5) / 2

def improve_test():
    approx_phi = improve(golden_update, square_close_to_successor)
    assert approx_eq(phi, approx_phi)

#Two problem of this approach
#1.Global frame bacomes clutterd with names of small functions
#2.We are constrained by particular funtion signatures

#nested definitions

def average(x, y):
    return (x + y) / 2

def sqrt_update(x, a):
    return average(x , a/x)
#two arguments , incompatible with improve

def sqrt(a):
    def sqrt_update(x):
        return average(x, a/x)
    def sqrt_approx(x):
        return approx_eq(x*x , a)
    return improve(sqrt_update, sqrt_approx)

