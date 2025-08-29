def split(n):
    return n // 10, n % 10

def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return last + sum_digits(all_but_last)
    
def lumn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return last + lumn_sum_double(all_but_last)
    
def lumn_sum_double(n):
    all_but_last, last = split(n)
    lumn_digit = sum_digits(2 * last)
    if n < 10:
        return lumn_digit
    else:
        return lumn_digit + lumn_sum(all_but_last)
    
