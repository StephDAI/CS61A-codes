from math import sqrt
def print_if(s,f):
    for x in s:
        if f(x)== True: print(x)

# print_if([3, 4, 5, 6], lambda x: x > 4)
# result = print_if([3, 4, 5, 6], lambda x: x % 2 == 0)
# print(result)

def close(s,k):
    ans = []
    for i in range(len(s)):
        if abs(s[i]-i)<=k: ans.append(s[i])
    return ans

# t = [6, 2, 4, 3, 5]
# print(close(t, 0))  # Only 3 is equal to its index
# print(close(t, 1)) # 2, 3, and 5 are within 1 of their index
# print(close(t, 2))  # 2, 3, 4, and 5 are all within 2 of their index
# print(close(list(range(10)), 0))

def squares(s):
    return [int(sqrt(x)) for x in s if sqrt(x)*sqrt(x)==x]

# seq = [50,400]
# print(squares(seq))

def double_eights(n):
    if(n%10 == 8 and n//10%10 == 8): return True
    if(n<10): return False
    return double_eights(n//10)

def make_onion(f,g):
    def can_reach(x,y,lim):

        if lim < 0: return False
        elif x == y: return True
        else:
            return can_reach(f(x),y,lim-1) or can_reach(g(x),y,lim-1)
    return can_reach







