def sum_naturals(n):
    total , k = 0, 1
    while k <= n:
        total , k = total + k , k + 1
    return total
#python-style sum-up function

def sum_cubes(n):
    total , k = 0 , 1
    while k <= n:
        total , k = total + k*k*k , k + 1
    return total

def pi_sum(n):
    total , k = 0 , 1
    div_1 , div_2 = 4*k-3, 4*k-1
    while k <= n:
        total , k = total + 8/(div_1*div_2), k + 1
    return total

#These three functions shared same underlying patterns
#Only different for the behavior of k
# def <name> (n):
#     total, k = 0 , 1
#     while k <= n:
#         total , k = total + <term>(k), k+1
#     return total

