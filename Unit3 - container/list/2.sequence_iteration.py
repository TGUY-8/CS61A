def count_occur_(s, value):
    total, index = 0, 0
    while index < len(s):
        if s[index] == value:
            total += 1
        index += 1
    return total

#for-iteration
def count_occur(s, value):
    total = 0
    for elem in s:
        if elem == value:
            total += 1
    return total

#sequence unpacking
pairs = [[1,2], [2,2], [2,3], [4,4]]
same_count = 0
for x, y in pairs:
    if x == y:
        same_count += 1