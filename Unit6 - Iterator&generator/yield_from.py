def a_then_b(a, b):
    yield from a
    yield from b

list(a_then_b([1, 2], [3, 4]))
#[1, 2, 3, 4]

def countdown(k):
    if k <= 0:
        yield "Blast off"
    else:
        yield k
        yield from countdown(k - 1)

def prefixes(s):
    if s:
        yield from prefixes(s[:-1])
        yield s

def prefixes_(s):
    if s:
        yield s
        yield from prefixes_(s[:-1])

def substring(s):
    if not s:
        return 
    else:
        yield from prefixes(s)
        yield from substring(s[1:])

def list_prefixes(s):
    if not s:
        return []
    else:
        return [s] + list_prefixes(s[:-1])
    
def list_substring(s):
    if not s:
        return []
    else:
        return list_prefixes(s) + list_substring(s[1:])