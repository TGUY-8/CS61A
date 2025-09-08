#function composition
def composal(f, g):
    k = 2
    def h(x):
        print(k)
        return f(g(x))
    return h

def square(x):
    return x*x

def successor(x):
    return x + 1

k = 1


square_successor = composal(square, successor)

print(square_successor(12))

#Order when searching for certain variable names:LEGB
#L - Local
#E - Enclosing -> parent
#G - Global
#B - Built-in