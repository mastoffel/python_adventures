# writing a decorator to cache the result of a pure function

import functools
import time

def memoize(fun):
    @functools.wraps(fun)
    fun._cache = {}
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key in fun._cache:
            return fun._cache[key]
        else:
            fun._cache[key] = fun(*args, **kwargs)
            return fun(*args, **kwargs)
    return wrapper


@memoize
def long_operation(x, y):
    time.sleep(2)
    return x + y

long_operation(2, 3)