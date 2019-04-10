class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result = num
        for arg in nums:
            self.result += arg
        return self

    def subtract(self, num, *nums):
        self.result = num
        for arg in nums:
            self.result -= arg
        return self

md = MathDojo()

x = md.add(2).result.add(2,5,1).subtract(3,2).result
y= md.add(2,5,1).result
z = md.subtract(3,2).result
print(x)
print(y)
print(z)