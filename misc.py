import random
# printing profile with variadic arguments

def create_profile(name, *surnames, **details):
    print(name, *surnames)
    for x, y in details.items():
        print(x, ": ", y)
   
    
create_profile('Martin', 'Adam', 'Stoffel', studies='Btown',
               hobbies='football')

def echo(args):
    """hidden string
    :param args: let it print"""
    return args

hex(id(echo))
foo = echo
id(foo)

x = 10
y = x
id(x)
id(y)

isinstance(foo, object)
isinstance(x, object)

echo.__doc__ = "new hidden string"

# lambda functions
(lambda x, y: x + y)(2, 5)

list(map(lambda x: x+x, range(11)))

# map
tuple(map(len, ["apple", "orange", "pear"]))


a = tuple(map(len, ["apple", "orange", "pear"]))
b = tuple(map(lambda x: x.upper(), ["apple", "orange", "pear"]))
c = tuple(map(lambda x: x[::-1], ["apple", "orange", "pear"]))
d = tuple(map(lambda x: x[:2], ["apple", "orange", "pear"]))

a = tuple(filter(lambda x: x%3 == 0, range(100)))
b = tuple(filter(lambda x: x%5 == 0, range(100))
c = tuple(filter(lambda x: x%15 == 0, range(100))
d = tuple(filter(lambda x: (x%3 != 0) & (x$5 != 0), range(100))
        
it = iter(range(100))
66 in it
next(it)  # => 67

def generate_tribonacci_numbers():
    a, b, c = 0, 0, 1
    while True:
        # Yield an infinite stream of Tribonacci numbers! The next value of the sequence will be c + b + a.
        yield a
        a, b, c = b, c, c + b + a
        

g = generate_tribonacci_numbers()
next(g)

def is_tribonacci(num):
    for trib in generate_tribonacci_numbers():
        if trib == num:
            return True
        if trib > num:
            return False

# infinite stream of random lists
def random_list(size, start=0, stop=10):
    return list(random.randrange(start, stop) for _ in range(size))
    
random_list(0)

import itertools

def generate_cases_another_alternative():
    return map(random_list, itertools.count())
    
generate_cases_another_alternative()

# write a decorator
def div_test(n):
    def divisible_by(m):
        return m%n == 0
    return divisible_by

div_3 = div_test(3)
div_3(4)
    
def foo(a: int, b: str) -> bool:
    return b[a] == 'X'
    
type(foo.__annotations__['a'])

