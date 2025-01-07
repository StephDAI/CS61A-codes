def gen_fib():
    n, add = 0, 1
    while True:
        yield n
        n, add = n + add, n

#print(next(filter(lambda n: n > 2024,gen_fib())))

def differences(t):
    a = next(t)
    def helper(it, a1):
        try:
            b = next(it)
            yield b-a1
            yield from helper(it, b)
        except:
            return 
    yield from helper(t,a)

#print(next(differences(iter([39, 100]))))
def partition_gen(n, m):
    """Yield the partitions of n using parts up to size m.

    >>> for partition in sorted(partition_gen(6, 4)):
    ...     print(partition)
    1 + 1 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 3
    1 + 1 + 2 + 2
    1 + 1 + 4
    1 + 2 + 3
    2 + 2 + 2
    2 + 4
    3 + 3
    """
    assert n > 0 and m > 0
    if n == m:
        yield str(m)
    if n - m > 0:
        "*** YOUR CODE HERE ***"
        for i in partition_gen(n-m,m):
            yield i +  " + " + str(m)
    if m > 1:
        yield from partition_gen(n,m-1)

for partition in sorted(partition_gen(6, 4)):
    print(partition)