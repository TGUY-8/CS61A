#Many built-in Python sequence operations return iterators that compute results lazily(not util u call next on the itearable)
#map(func, iterable)
#filter(pred, iterable)
#zip(fitst_iter, second_iter)
#reversed(sequence)

def double(x):
    print('**', x, '=>', 2*x, '**')
    return 2*x

m = map(double, [1, 2, 3])
next(m)
next(m)

def largerThan10(x):
    return x >= 10

k = map(double, [3, 4, 5, 6])
i = filter(largerThan10, k)
next(k)
next(k)
next(k)