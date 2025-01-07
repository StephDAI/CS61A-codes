from operator import add, mul, sub
square = lambda x:x**2
identity = lambda x:x
triple = lambda x:x**3
increment = lambda x:x+1

def product(n,term):
    Sum = 1
    for i in range(1,n+1):
        Sum *= term(i)
    return Sum
#print(product(3,square))

def accumulate(combiner, base, n, term):
    """Return the result of combining the first n terms in a sequence and base.
    The terms to be combined are term(1), term(2), ..., term(n).  combiner is a
    two-argument commutative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
    19
    >>> accumulate(lambda x, y: 2 * (x + y), 2, 3, square)
    58
    >>> accumulate(lambda x, y: (x + y) % 17, 19, 20, square)
    16
    """
    tot = base
    for i in range(1,n+1):
        tot = combiner(tot,term(i))
    return tot
#print(accumulate(mul, 2, 3, square))

def compose1(func1, func2):
    """Return a function f, such that f(x) = func1(func2(x))."""
    def f(x):
        return func1(func2(x))
    return f

def make_repeater(func, n):
    """Return the function that computes the nth application of func.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times!
    5
    """
    "*** YOUR CODE HERE ***"
    '''if(n == 0): return identity
    f,i = func,n-1
    while(i > 0):
        f = compose1(f,func)
        i -= 1
    return f'''
    return accumulate(compose1, identity, n, lambda x:func)

#print (make_repeater(square, 1)(5))
def zero(f):
    return lambda x: x

def successor(n):
    return lambda f: lambda x: f(n(f)(x))

def one(f):
    return lambda x: f(x)

def two(f):
    return lambda x: f(f(x))

def church_to_int(n):
    return n(lambda y: y+1)(0)

three = successor(two)
#print(church_to_int(zero)," ",church_to_int(one)," ",church_to_int(two)," ",church_to_int(three))\

def add_church(m,n):
    return lambda f: lambda x: m(f)(n(f)(x))

#print(church_to_int(add_church(zero, one)))

def mul_church(m,n):
    func = m
    num = church_to_int(n)
    def helper(k,f):
        if k==0 : return zero
        elif k == 1: return f
        else:
            f = add_church(f,m)
            return helper(k-1,f)
    return helper(num,func)



#print(church_to_int(mul_church(zero,three)))

def pow_church(m,n):
    func = m
    num = church_to_int(n)
    def helper(k,f):
        if k==0 : return one
        elif k == 1: return f
        else:
            f = mul_church(f,m)
            return helper(k-1,f)
    return helper(num,func)

print(church_to_int(pow_church(two,mul_church(two,three))))