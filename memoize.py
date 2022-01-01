# writing a decorator to cache the result of a pure function

import functools
import time

def memoize(function):
    function._cache = {}
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key not in function._cache:
            function._cache[key] = function(*args, **kwargs)
        return function._cache[key]
    return wrapper


@memoize
def long_operation(x, y):
    time.sleep(2)
    return x + y

long_operation(3, 3) # takes 2 second
long_operation(3, 3) # near instant

