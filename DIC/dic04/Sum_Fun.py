def sums(n, m):
    """Return lists that sum to n containing positive numebers up to m that
    have no adjacent repeats

    >>> sums(5, 1)
    []
    >>> sums(5, 2)
    [[2, 1, 2]]
    >>> sums(5, 3)
    [[1, 3, 1], [2, 1, 2], [2, 3], [3, 2]]
    >>> sums(5, 5)
    [[1, 3, 1], [1, 4], [2, 1, 2], [2, 3], [3, 2], [4, 1], [5]]
    
    """
    if n < 0:
        return []
    elif n == 0:
        return [[]]
    result = []
    for k in range(1, m + 1):
        result += [[k] + rest for rest in sums(n - k, m) if rest == [] or k != rest[0]]
    return result