from abc import ABC, abstractmethod

class IPayment(ABC):
    @abstractmethod
    def auth_users(self, *args):
        pass
    @abstractmethod
    def process_payment(self, *args):
        pass

class BalanceMixin:
    def __init__(self, balance):
        self._balance = balance
    
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, value):
        if value<0:
            self._balance = 0
        else:
            self._balance = value

class CreditCard(IPayment, BalanceMixin):
    def __init__(self, balance):
        super().__init__(balance)

    def auth_users(self, cred):
        if cred == "ID123":
            print("Authenticated")
        else:
            print("Access Denied")
    
    def process_payment(self, amt:float):
        self.balance+=amt
        print(f"Added {amt}, Current balance: {self.balance}")


class UPI(IPayment, BalanceMixin):
    def __init__(self, balance):
        super().__init__(balance)

    def auth_users(self, cred):
        if cred == "ID123":
            print("Authenticated")
        else:
            print("Access Denied")
    
    def process_payment(self, amt:float):
        self.balance+=amt
        print(f"Added {amt}, Current balance: {self.balance}")
    

class Wallet(IPayment, BalanceMixin):
    def __init__(self, balance):
        super().__init__(balance)

    def auth_users(self, cred):
        if cred == "ID123":
            print("Authenticated")
        else:
            print("Access Denied")
    
    def process_payment(self, amt:float):
        self.balance+=amt
        print(f"Printing internal _balance = {self._balance} inside Wallet class")
        print(f"Added {amt}, Current balance: {self.balance}")

if __name__ == "__main__":
    payment = [CreditCard(100), UPI(500), Wallet(1000)]
    for p in payment:
        p.auth_users("ID123")
        p.process_payment(100)
        print("---")


"""
In this example,
    the getter (@property) returns the value of _balance
    the setter (@variable.setter) writes the value of balance
these are triggered when the functions like "auth_users()" and "process_payment()" use balance (not _balance)

so, what is difference between "balance" and "_balance":
    1. _balance is a protected (__variable is private): which is used for internal use, i.e. look at BalanceMixin class, the constructor uses this to store the value being passed in the object, and the getter is returning that value. Also, see that the setter is initialising that _balance variable

    2. balance is used by the functions "auth_users()" and "process_payment()"
       How can we use balance in those functions? the balance is using the @property decorator and it's constructor is using _balance to store the initial values (talking inside BalanceMixin class), so always imagine that when we @property and .setter over any function it becomes a variable (no longer a function).

    3. Also, these getter and setter are triggered when we self.balance+=amt in "process_payment", as we are trying to set a new value to balance. Only triggered when we try to print or set balance (not _balance), when we access _balance we are just accessing _balance: the protected internal variable
"""

"""
OUTPUT:
Authenticated
Added 100, Current balance: 200
---
Authenticated
Added 100, Current balance: 600
---
Authenticated
Printing internal _balance = 1100 inside Wallet class
Added 100, Current balance: 1100
---
"""
