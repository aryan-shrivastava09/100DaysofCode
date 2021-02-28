def add(*args):
    print(args)
    print(type(args))
    sum = 0
    for n in args:
        sum += n
    return sum


add1_10 = add(1,2,3,4,5,6,7,8,9, 10)
print(add1_10)

def calculate(n, **kwargs):
    # print(kwargs)
    # print(type(kwargs))
    # for (key,value) in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
calculate(5, add = 3, multiply = 5)

class car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        print(self.make)
        print(self.model)

# c = car(make = "Ford", model = "Mustang")
c = car(make = "Ford")
