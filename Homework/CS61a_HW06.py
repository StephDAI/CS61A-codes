class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Nothing left to vend. Please restock.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'Please add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'Please add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    def __init__(self, product, price):
        """Set the product and its price, as well as other instance attributes."""
        "*** YOUR CODE HERE ***"
        self.product = product
        self.price = price
        self.stock = 0
        self.balance = 0

    def restock(self, n):
        """Add n to the stock and return a message about the updated stock level.

        E.g., Current candy stock: 3
        """
        "*** YOUR CODE HERE ***"
        self.stock += n
        return f"Current {self.product} stock: {self.stock}"

    def add_funds(self, n):
        """If the machine is out of stock, return a message informing the user to restock
        (and return their n dollars).

        E.g., Nothing left to vend. Please restock. Here is your $4.

        Otherwise, add n to the balance and return a message about the updated balance.

        E.g., Current balance: $4
        """
        "*** YOUR CODE HERE ***"
        if self.stock == 0:
            return f"Nothing left to vend. Please restock. Here is your ${n}."
        self.balance += n
        return f"Current balance: ${self.balance}"

    def vend(self):
        """Dispense the product if there is sufficient stock and funds and
        return a message. Update the stock and balance accordingly.

        E.g., Here is your candy and $2 change.

        If not, return a message suggesting how to correct the problem.

        E.g., Nothing left to vend. Please restock.
              Please add $3 more funds.
        """
        "*** YOUR CODE HERE ***"
        if self.stock == 0:
            return "Nothing left to vend. Please restock."
        if self.balance < self.price:
            return f"Please add ${self.price-self.balance} more funds."
        self.balance -= self.price
        self.stock -= 1
        if self.balance>0: 
            a = self.balance
            self.balance = 0
            return f"Here is your {self.product} and ${a} change"
        return f"Here is your {self.product}"
    
class Link:
    empty = ()
    def __init__(self, first, rest = empty):
        self.first = first
        self.rest = rest
    def __repr__(self):
        if self.rest == Link.empty: return f"Link({self.first})"
        return f"Link({self.first},{self.rest})"

def store_digits(n):
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    >>> store_digits(2450)
    Link(2, Link(4, Link(5, Link(0))))
    >>> store_digits(20105)
    Link(2, Link(0, Link(1, Link(0, Link(5)))))
    >>> # a check for restricted functions
    >>> import inspect, re
    >>> cleaned = re.sub(r"#.*\\n", '', re.sub(r'"{3}[\s\S]*?"{3}', '', inspect.getsource(store_digits)))
    >>> print("Do not use str or reversed!") if any([r in cleaned for r in ["str", "reversed"]]) else None
    """
    "*** YOUR CODE HERE ***"
    def store(arr):
        if len(arr) == 1:return Link(arr[0])
        return Link(arr[-1],store(arr[0:-1]))
    l = []
    while(n>9):
        l.append(n%10)
        n //= 10
    l.append(n)
    return store(l)
