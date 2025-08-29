def counting_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0 or m < 1:
        return 0
    else:
        return counting_partitions(n - m, m) + counting_partitions(n, m - 1)
    
#devide all the possible partitions into two parts - containing exact m and not containing m