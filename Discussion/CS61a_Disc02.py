def make_keeper(n):
    def helper(cond):
        for i in range(1,n+1):
            if(cond(i)): print(i)
    return helper
'''
def is_even(x):
    return x % 2 == 0
make_keeper(5)(is_even)
'''

def f3():
    return lambda x:x
#print(f3()(3))

def f4():
    return lambda : lambda x:lambda :x
print(f4()()(3)())