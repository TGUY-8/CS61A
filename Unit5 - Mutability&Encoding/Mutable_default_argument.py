def f(s = []):
    s.append(5)
    return len(s)

print(f())
print(f())
print(f())

#Mutable defualt argument
#everytime you call f with default argument, it refers to the object with the same identity which indicates every mutation you made will permantly change its state
