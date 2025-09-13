def yield_partitions(n, m):
    if n > 0 and m > 0:
        for p in yield_partitions(n - m, m):
            yield [m] + p
        yield from yield_partitions(n, m - 1)

def list_partitions(n, m):
    if n == 0:
        return [[]]
    if n < 0 or m == 0:
        return []
    with_m = [[m] + p for p in list_partitions(n - m, m)]
    without_m = list_partitions(n, m - 1)
    return with_m + without_m