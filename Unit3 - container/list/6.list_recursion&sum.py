def sum_list(s):
    if not s:
        return 0
    else:
        return s[0] + sum_list(s[1:])
    
#actually equals to Python built-in function - sum
#sum(iterable[, start]) -> value (start is optional and by default is 0)
#return sum of the iterable numbers plus the optional argument start
sum([[1, 2], [3, 4]])
#Type error "int" + "list"
sum([[1, 2], [3, 4]], [])
#correct

#max(iterable[, key=func]) -> value
#max(a,b,c....[, key=func]) -> value
max([1, 2, 3, 4])
#4
max([1,2,3,4], key = lambda x: (x - 3)*(2 - x))
#return max return value

#all(iterable) —> bool
#return True if bool(x) is True for all x in the iterable , notablly, return True if iterable is empty
