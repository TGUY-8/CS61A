def summation(n, func):
    total, k = 0 , 1
    while k <= n:
        total , k = total + func(k) , k + 1
    return total

def constant(n):
    return n

def sum(n):
    return summation(n, constant)

def cube_area(n):
    return n*n*n

def sum_cubes(n):
    return summation(n, cube_area)

def pi_simulate(n):
    return 8 / ((4*n-1)*(4*n-3))

def pi_sum(n):
    return summation(n, pi_simulate)

