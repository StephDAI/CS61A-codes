def num_eights(n):
    if(n<10 and n==8): return 1
    elif(n<10 and n!=8): return 0
    elif(n%10==8): return 1+num_eights(n//10)
    elif(n%10!=8): return num_eights(n//10)

#print(num_eights(18848))

def digit_distance(n):
    if n<10: return 0
    else:
        a = n%10
        b = n//10%10
        return abs(a-b)+digit_distance(n//10)
    
#print(digit_distance(3464660003))

def interleaved_sum(n,odd_f,even_f):
    def helper(k):
        if(n == k): return odd_f(k)
        elif(n-k==1): return even_f(n) + odd_f(k)
        else:
            return even_f(k+1) + odd_f(k) + helper(k+2)
    return helper(1)

identity = lambda x: x
square = lambda x: x * x
triple = lambda x: x * 3
#print(interleaved_sum(5, identity, square)) # 1   + 2*2 + 3   + 4*4 + 5
    #29
#print(interleaved_sum(5, square, identity)) # 1*1 + 2   + 3*3 + 4   + 5*5
    # 41
#print(interleaved_sum(4, triple, square) )  # 1*3 + 2*2 + 3*3 + 4*4
    # 32
#print(interleaved_sum(4, square, triple)  ) # 1*1 + 2*3 + 3*3 + 4*3
    # 28

def next_smaller_dollar(bill):
    """Returns the next smaller bill in order."""
    if bill == 100:
        return 50
    if bill == 50:
        return 20
    if bill == 20:
        return 10
    elif bill == 10:
        return 5
    elif bill == 5:
        return 1
    
def get_max_dollar(n):
    if n >= 100 : return 100
    elif n >= 50 : return 50
    elif n >= 20: return 20
    elif n >= 10: return 10
    elif n >= 5: return 5
    elif n >= 1: return 1
    else: return 0 




def next_larger_dollar(bill):
    """Returns the next larger bill in order."""
    if bill == 1:
        return 5
    elif bill == 5:
        return 10
    elif bill == 10:
        return 20
    elif bill == 20:
        return 50
    elif bill == 50:
        return 100

def count_dollars(n1):
    def helper(n,x):
        if n==0: return 1
        #elif x == 1: return 1
        elif x > n: return 0
        elif x==100: return helper(n-x,x)
        else: return helper(n,next_larger_dollar(x)) + helper((n - x),(x))
    #max = get_max_dollar(n1)
    return helper(n1,1)
print(count_dollars(15))
print(count_dollars(10))
print(count_dollars(20))
print(count_dollars(45))
print(count_dollars(100))
print(count_dollars(200))