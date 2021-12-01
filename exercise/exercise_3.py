# 1 262p
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val


class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val


cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)


# 2
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            mv = self.value - 100
            self.value -= mv


Mcal = MaxLimitCalculator()
Mcal.add(50)
Mcal.add(60)

print(Mcal.value)
