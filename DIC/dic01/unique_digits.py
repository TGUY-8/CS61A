def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    num , cnt = 0 , 0
    while n:
        digit= n%10
        if not (has_digit(num, digit)):
            cnt += 1
        num , n = num*10 + digit, n // 10
    return cnt

def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    "*** YOUR CODE HERE ***"
    while n:
        digit , n = n % 10, n // 10
        if k == digit:
            return True
    return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()