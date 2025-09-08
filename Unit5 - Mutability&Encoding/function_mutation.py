four = [1, 2, 3, 4]

def ppop(s):
    s.pop()
    s.pop()

ppop(four)

len(four)
#2

# non-mutable -> copy, mutable -> reference

def another_ppop(s = []):
    four.pop()
    four.pop()

another_ppop()

print(len(four))