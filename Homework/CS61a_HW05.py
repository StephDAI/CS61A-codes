def hailstone(n):
    """
    Yields the elements of the hailstone sequence starting at n.
    At the end of the sequence, yield 1 infinitely.

    >>> hail_gen = hailstone(10)
    >>> [next(hail_gen) for _ in range(10)]
    [10, 5, 16, 8, 4, 2, 1, 1, 1, 1]
    >>> next(hail_gen)
    1
    """
    "*** YOUR CODE HERE ***"
    if n==1: 
        yield 1
        yield from hailstone(1)
    elif n%2==1:
        yield n 
        yield from hailstone(3*n+1)
    elif n%2==0:
        yield n
        yield from hailstone(n//2)
hail_gen = hailstone(10)
# print([next(hail_gen) for _ in range(10)])
# print(next(hail_gen))
def merge(a, b):
    """
    Return a generator that has all of the elements of generators a and b,
    in increasing order, without duplicates.

    >>> def sequence(start, step):
    ...     while True:
    ...         yield start
    ...         start += step
    >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    a_val, b_val = next(a), next(b)
    while True:
        if a_val == b_val:
            yield a_val
            yield from merge(a,b)
        elif a_val < b_val:
            "*** YOUR CODE HERE ***"
            yield a_val
            a_val = next(a)
        else:
            "*** YOUR CODE HERE ***"
            yield b_val
            b_val = next(b)

def sequence(start, step):
    while True:
        yield start
        start += step
# a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
# b = sequence(3, 2)
# result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
# print([next(result) for _ in range(10)])
def stair_ways(n):
    """
    Yield all the ways to climb a set of n stairs taking
    1 or 2 steps at a time.

    >>> list(stair_ways(0))
    [[]]
    >>> s_w = stair_ways(4)
    >>> sorted([next(s_w) for _ in range(5)])
    [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]]
    >>> list(s_w) # Ensure you're not yielding extra
    []
    """
    "*** YOUR CODE HERE ***"
    if n==0: yield []
    elif n==1:yield [1]
    else:
        for i in stair_ways(n-1):
            yield i+[1]
        for i in stair_ways(n-2):
            yield i+[2]

# print(list(stair_ways(0)))
# s_w = stair_ways(4)
# print(sorted([next(s_w) for _ in range(5)]))
# print(list(s_w))
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
def yield_paths(t,value):
    if label(t) == value:
        yield [label(t)]
    for b in branches(t):
        for path in yield_paths(b,value):
            yield [label(t)] +list(path) 
t1 = tree(1, [tree(2, [tree(3), tree(4, [tree(6)]), tree(5)]), tree(5)])
print(next(yield_paths(t1, 6)))#[1, 2, 4, 6]
path_to_5 = yield_paths(t1, 5)
print(sorted(list(path_to_5)))#   [[1, 2, 5], [1, 5]]
t2 = tree(0, [tree(2, [t1])])
path_to_2 = yield_paths(t2, 2)
print(sorted(list(path_to_2)))#    [[0, 2], [0, 2, 1, 2]]