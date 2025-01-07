def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

t2 = tree(5, [tree(6), tree(7)])
t1 = tree(3, [tree(4), t2])

def has_path(t,p):
    if label(t) == p[0]:
        if len(p) == 1: return True
        else:
            for i in branches(t):
                delete = p.pop(0)
                if has_path(i, p): return True
                p.insert(0,delete)
            return False
    else:
        return False

def has_path_better_vers(t,p):
    if p == [label(t)]: return True
    elif label(t) != p[0]: return False
    else:
        for i in branches(t):
            if has_path_better_vers(i, p[1:]): return True
        return False

def find_path(t,x):
    if label(t) == x: return [x]
    elif label(t) != x and is_leaf(t): return None
    else:
        for i in branches(t):
            if find_path(i, x) != None: return [label(t)] + find_path(i,x)
        return None

print(find_path(t1,5) )
print(find_path(t1, 4)  )    
print(find_path(t1, 6)  )   
print(find_path(t2, 6) )
print(find_path(t1, 2))

