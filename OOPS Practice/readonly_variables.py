class Balance:
    def __init__(self, salary, tax):
        if tax > salary:
            raise ValueError("Tax is always smaller than salary(except u know where)")
        self._salary = salary
        self._tax = tax

    @property
    def salary(self):
        return self._salary - self._tax

if __name__ == "__main__":
    b = Balance(300, 20)
    print(b.salary)
    # b.salary = 2 will throw this error
    # AttributeError: property 'salary' of 'Balance' object has no setter: thus we have readonly values