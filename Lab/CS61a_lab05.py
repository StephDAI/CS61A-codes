def group_by(s, fn):
    """Return a dictionary of lists that together contain the elements of s.
    The key for each list is the value that fn returns when called on any of the
    values of that list.

    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
    """
    grouped = {}
    for i in s:
        key = fn(i)
        if key in grouped:
            grouped[key].append(i)
        else:
            grouped[key] = [i]
    return grouped

# print(group_by([12, 23, 14, 45], lambda p: p // 10))
# print(group_by(range(-3, 4), lambda x: x * x))
def count_occurrences(t, n, x):
    if n ==0:return 0
    if next(t) == x: return 1+count_occurrences(t,n-1,x)
    else: return count_occurrences(t,n-1,x)

# s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
# print(count_occurrences(s, 10, 9)) #3
# t = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
# print(count_occurrences(t, 3, 10))#2
# u = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
# print(count_occurrences(u, 1, 3))  # Only iterate over 3
# print(count_occurrences(u, 3, 2) ) # Only iterate over 2, 2, 2
# print(list(u))                     # [1, 2, 1, 4, 4, 5, 5, 5]
# v = iter([4, 1, 6, 6, 7, 7, 6, 6, 2, 2, 2, 5])
# print(count_occurrences(v, 6, 6))#2

def repeated(t,k):
    cnt = 1
    last = next(t)
    for i in t:
        if i==last:
            cnt+=1
        else:
            last = i
            cnt = 1
        if cnt == k: return i
    return "blast"    

# s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
# print(repeated(s, 2))#9
# print(repeated(s,5))
# t = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
# print(repeated(t, 3))#8
# u = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
# print(repeated(u, 3))#2
# print(repeated(u, 3))#5
# v = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
# print(repeated(v, 3))#2

def tree(label, branches=[]):
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

def print_tree(tree):
    def helper(tree,k):
        print(label(tree))
        for branch in branches(tree):
            print(k*"   ",end='')
            helper(branch,k+1)
    helper(tree,1)

def sprout_leaves(t, leaves):
    l = []
    for leave in leaves:
        l.append([leave])
    if is_leaf(t):
        return [label(t)]+l
    else:
        for i in range(len(branches(t))):
            t[i+1] = sprout_leaves(branches(t)[i],leaves)
        return t
        
# t1 = tree(1, [tree(2), tree(3)])
# print_tree(t1)
# new1 = sprout_leaves(t1, [4, 5])
# print_tree(new1)
t2 = tree(1, [tree(2, [tree(3)])])
print_tree(t2)
new2 = sprout_leaves(t2, [6, 1, 2])
print_tree(new2)