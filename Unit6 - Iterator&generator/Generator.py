def plus_minus(x):
    yield x
    yield -x

t = plus_minus(3)
next(t) #3
next(t) #-3

#A generator function is a function that yields values instead of returning them
#A Generator is a special case of iterator

def evens(start, end):
    even = start + (start % 2)
    while even < end:
        yield even
        even += 2