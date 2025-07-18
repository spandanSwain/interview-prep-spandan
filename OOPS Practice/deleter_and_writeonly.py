# code to have a deleter property triggered when we do del obj.variable name
# code to have a write only variable

class User:
    def __init__(self, password):
        self._pass = password
    
    @property
    def password(self):
        raise ValueError("password is write-only")
    
    @password.setter
    def password(self, value):
        self._pass = value
        print("stored | updated")

    @password.deleter
    def password(self):
        self._pass = None
        print("removed")

u = User("123")
# print(u.password) # ValueError: password is write-only
u.password = "456" # no error meaning yeah we stored it
del u.password