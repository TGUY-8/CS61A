#{<key exp> : <value exp> for <item> in <iter exp> if <filter exp>}
#~Add a new frame with the current frame as its parent
#~Create an empty result dictionary that is the value of the expression
#~For each element in the iterable value of <iter exp>: A. Bind <item> to that element in the new frame from step 1 B.If <filter exp> evaluates to a true value , then add to the result dictionary an entry that pairs the value of <key exp> to the value of <value exp>

{x*x : x + 1 for x in [1, 2, 3, 4, 5] if x > 2}

def index(keys, values, match):
    return {k:[v for v in values if match(k, v)] for k in keys}