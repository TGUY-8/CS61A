def f(s = []):
    s.append(5)
    return len(s)

print(f())
print(f())
print(f())