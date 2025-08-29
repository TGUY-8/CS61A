def sum_digits(n):
    if n <= 10:
        return n
    else:
        new_n , split = n // 10 , n % 10
        return split + sum_digits(new_n)
    
    