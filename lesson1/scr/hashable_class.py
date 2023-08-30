class HashTestClass():
    def __init__(self, val: int) -> None:
        self.value = val


c1 = HashTestClass(1)
c2 = HashTestClass(2)
c3 = HashTestClass(3)

print(c1.__hash__())
c1.value = 2
print(c1.__hash__())
print(c2.__hash__())
print(c3.__hash__())