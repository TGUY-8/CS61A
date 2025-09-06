def tree(label,  branches = []):
    for branch in branches:
        assert is_tree(branches), 'branches must be a tree'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(branch):
    return not is_tree(branch)

def fib_tree(n):
    if n <= 1:
        return n
    else:
        return 
    
def is_leaf(tree):
    return type(tree) == list and len(tree) == 1

def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        return sum( [count_leaves(branch) for branch in branches(tree)] )
    
def leaves(tree):
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum( [leaves(branch) for branch in branches(tree)], [] )
    
def incremented_leaves(t):
    if is_leaf(t):
        return [label(tree) + 1]
    else:
        return tree(label(t), [incremented_leaves(branch) for branch in branches(t)])
    
def incremented_tree(t):
    return tree(label(t) + 1, [incremented_tree(branch) for branch in branches()])

def print_tree(t, indent = 0):
    print('  ' * indent + str(label(t)))
    for branch in branches(t):
        print_tree(branch, indent + 1)

def count_paths(t):
    if is_leaf(t):
        return 1
    else:
        return sum([count_paths(branch) for branch in branches(t)])
    
def count_paths_to_total(tree, total):
    if total < label(tree) or is_leaf(tree) and total != label(tree):
        pass
    elif total == label(tree):
        return 1
    else:
        return sum([ count_paths_to_total(branch, total - label(tree)) for branch in branches(tree)])