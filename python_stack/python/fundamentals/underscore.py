class Underscore:
    def map(self, iterable, callback):
        # your code here
        for i in range(len(iterable)):
            iterable[i] = callback(iterable[i])
        return iterable    
    def find(self, iterable, callback):
        # your code here
        for i in range(len(iterable)):
            if callback(iterable[i]):
                return iterable[i]

    def filter(self, iterable, callback):
        # your code
        retArr = []
        for i in range(len(iterable)):
            if callback(iterable[i]):
                retArr.append(iterable[i])
        return retArr        
    def reject(self, iterable, callback):
        # your code
        retArr = []
        for i in range(len(iterable)):
            if not callback(iterable[i]):
                retArr.append(iterable[i])
        return retArr        
# you just created a library with 4 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
squares = _.map([1,2,3], lambda x: x**2)
print(squares)

firstEven = _.find([1,2,5,4], lambda x: x %2==0)
print(firstEven)

evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print("evens", evens)

odds = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print("odds",odds)

