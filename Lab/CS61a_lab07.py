class Account:
    """An account has a balance and a holder.

    >>> a = Account('John')
    >>> a.deposit(10)
    10
    >>> a.balance
    10
    >>> a.interest
    0.02
    >>> a.time_to_retire(10.25)  # 10 -> 10.2 -> 10.404
    2
    >>> a.balance                # Calling time_to_retire method should not change the balance
    10
    >>> a.time_to_retire(11)     # 10 -> 10.2 -> ... -> 11.040808032
    5
    >>> a.time_to_retire(100)
    117
    """
    max_withdrawal = 10
    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        if amount > self.max_withdrawal:
            return "Can't withdraw that amount"
        self.balance = self.balance - amount
        return self.balance
    
    def time_to_retire(self, amount):
        """Return the number of years until balance would grow to amount."""
        assert self.balance > 0 and amount > 0 and self.interest > 0
        "*** YOUR CODE HERE ***"
        cnt_yrs = 0
        money = self.balance
        while money < amount:
            money *= (1+Account.interest)
            cnt_yrs += 1
        return cnt_yrs
# a = Account('John')
# print(a.deposit(10))
# print(a.balance)
# print(a.interest)
# print(a.time_to_retire(10.25))  # 10 -> 10.2 -> 10.404
# print(a.balance)                # Calling time_to_retire method should not change the balance
# print(a.time_to_retire(11))     # 10 -> 10.2 -> ... -> 11.040808032
# print(a.time_to_retire(100))

class FreeChecking(Account):
    """A bank account that charges for withdrawals, but the first two are free!

    >>> ch = FreeChecking('Jack')
    >>> ch.balance = 20
    >>> ch.withdraw(100)  # First one's free. Still counts as a free withdrawal even though it was unsuccessful
    'Insufficient funds'
    >>> ch.withdraw(3)    # Second withdrawal is also free
    17
    >>> ch.balance
    17
    >>> ch.withdraw(3)    # Now there is a fee because free_withdrawals is only 2
    13
    >>> ch.withdraw(3)
    9
    >>> ch2 = FreeChecking('John')
    >>> ch2.balance = 10
    >>> ch2.withdraw(3) # No fee
    7
    >>> ch.withdraw(3)  # ch still charges a fee
    5
    >>> ch.withdraw(5)  # Not enough to cover fee + withdraw
    'Insufficient funds'
    """
    withdraw_fee = 1
    free_withdrawals = 2

    "*** YOUR CODE HERE ***"
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.free_withdrawals = FreeChecking.free_withdrawals
    def withdraw(self, amount):
        if self.free_withdrawals > 0:
            self.free_withdrawals -= 1
        else:
            amount += FreeChecking.withdraw_fee
        if self.balance < amount: return "Insufficient funds"
        else: 
            self.balance -= amount
            return self.balance
# ch = FreeChecking('Jack')
# ch.balance = 20
# print(ch.withdraw(100))  # First one's free. Still counts as a free withdrawal even though it was unsuccessful
# print(ch.withdraw(3))    # Second withdrawal is also free
# print(ch.balance)
# print(ch.withdraw(3))    # Now there is a fee because free_withdrawals is only 2
# print(ch.withdraw(3))
# ch2 = FreeChecking('John')
# ch2.balance = 10
# print(ch2.withdraw(3)) # No fee
# print(ch.withdraw(3))  # ch still charges a fee
# print(ch.withdraw(5))
class Link:
    empty = ()
    def __init__(self, first, rest = empty):
        self.first = first
        self.rest = rest
    def __repr__(self):
        if self.rest is Link.empty: return f"Link({repr(self.first)})"
        return f"Link({repr(self.first)},{repr(self.rest)})"
    def __str__(self):
        string = "<"
        while self.rest is not Link.empty:
            string = string + str(self.first) + " "
            self = self.rest
        return string + str(self.first) + ">"

def without(s, i):
    """Return a new linked list like s but without the element at index i.

    >>> s = Link(3, Link(5, Link(7, Link(9))))
    >>> without(s, 0)
    Link(5, Link(7, Link(9)))
    >>> without(s, 2)
    Link(3, Link(5, Link(9)))
    >>> without(s, 4)           # There is no index 4, so all of s is retained.
    Link(3, Link(5, Link(7, Link(9))))
    >>> without(s, 4) is not s  # Make sure a copy is created
    True
    """
    "*** YOUR CODE HERE ***"
    def remove(linked_list,index):
        if linked_list is Link.empty: return linked_list
        if i == index: return linked_list.rest
        return Link(linked_list.first,remove(linked_list.rest,index+1))
    return remove(s,0)
# s = Link(3, Link(5, Link(7, Link(9))))
# print(without(s, 0))
# print(without(s, 2))
# print(without(s, 4))           # There is no index 4, so all of s is retained.
# print(without(s, 4) is not s)
def duplicate_link(s, val):
    """Mutates s so that each element equal to val is followed by another val.

    >>> x = Link(5, Link(4, Link(5)))
    >>> duplicate_link(x, 5)
    >>> x
    Link(5, Link(5, Link(4, Link(5, Link(5)))))
    >>> y = Link(2, Link(4, Link(6, Link(8))))
    >>> duplicate_link(y, 10)
    >>> y
    Link(2, Link(4, Link(6, Link(8))))
    >>> z = Link(1, Link(2, (Link(2, Link(3)))))
    >>> duplicate_link(z, 2) # ensures that back to back links with val are both duplicated
    >>> z
    Link(1, Link(2, Link(2, Link(2, Link(2, Link(3))))))
    """
    "*** YOUR CODE HERE ***"
    def modify(s,val):
        if s is Link.empty: return s
        if s.first == val:
            s.rest = Link(val,s.rest)
            s.rest.rest = modify(s.rest.rest,val)
        else:
            s.rest = modify(s.rest,val)
        return s
    s = modify(s,val)
x = Link(5, Link(4, Link(5)))
duplicate_link(x, 5)
print(x)
y = Link(2, Link(4, Link(6, Link(8))))
duplicate_link(y, 10)
print(y)
z = Link(1, Link(2, (Link(2, Link(3)))))
duplicate_link(z, 2) # ensures that back to back links with val are both duplicated
print(z)