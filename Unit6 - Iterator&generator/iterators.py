l = [3, 4, 5, 6]
t = iter(s)
next(t)
#3
next(t)
#4
list(t)
#[5, 6]

d = {'one':1, 'two':2, 'three':3}
k = iter(d)
v = iter(d.values())
i = iter(d.iterm())

