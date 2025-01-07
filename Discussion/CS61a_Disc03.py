import math

def multiply(m,n): 
    if n == 1: return m
    else:
        return m + multiply(m,n-1)
    
#print(multiply(5,8)) 40

def is_prime(n):
    def helper(x):
        if(x > math.sqrt(n)): return True
        elif (n % x == 0): return False
        else : return helper(x + 1)
    return helper(2)

#print(is_prime(16)) False
#print(is_prime(23)) True 

def hailstone(n):
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0 :
        return hailstone(n//2) + 1
    elif n % 2 == 1:
        return hailstone(3*n+1) + 1
    
#a = hailstone(114720)
#print(a) 

def merge(n1,n2):
    if n1 == 0 :
        return n2
    elif n2 == 0:
        return n1
    elif(n1 % 10 >= n2 % 10):
        return n2%10 + merge(n1,n2//10) * 10
    elif(n1 % 10 < n2 % 10):
        return n1%10 + merge(n1//10,n2) * 10
    
print(merge(31,21))