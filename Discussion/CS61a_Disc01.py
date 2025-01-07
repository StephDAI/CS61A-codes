def ordered_digits(x):
    last = x % 10
    x = x // 10
    while x > 0 and last >= x % 10:
        last = x % 10
        x //= 10
    if x == 0: return True
    else: return False

n = int(input("input a number:"))
print(ordered_digits(n))