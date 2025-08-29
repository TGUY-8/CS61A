def composel(f , g):
    return lambda x : f(g(x))

f = composel(lambda x : x*x , lambda x : x + 1)

print(f(12))

#lambda function has no intrinsic name, but otherwise it behaves like any other function

