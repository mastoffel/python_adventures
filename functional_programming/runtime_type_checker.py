# A decorator factory to type check function arguments and results

import functools
import inspect


def bind_args(function, *args, **kwargs):
    return inspect.signature(function).bind(*args, **kwargs).arguments

def check_types(severity=1):
    
    # no checking if severity 0
    if severity == 0:
        return lambda function: function
    
    def message(msg):
        if severity==1:
            print(msg)
        else:
            raise TypeError(msg)

    def checker(function):
        # check if there are annotations
        if not function.__annotations__:
            return function
        # check that each annotation is a class
        if not all([inspect.isclass(x) for x in list(function.__annotations__.values())]):
            raise ValueError("Annotations have to be types")
        
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            bound_args = bind_args(function, *args, **kwargs)
            annots = function.__annotations__
            for arg in bound_args.keys():
                if type(bound_args[arg]) != annots[arg]:
                    message(f"Incorrect argument type. Received {arg}={bound_args[arg]} but expected type {annots[arg]}")
            res = function(*args, **kwargs)
            if type(res) != annots['return']:
                message(f"Incorrect result type. Received {res} but expected type {annots['return']}")
            return function(*args, **kwargs)
        return wrapper
    return checker

@check_types(severity=2)
def foo(a: int, b: str) -> bool:
    return b[a] == "X"

# correct types 
foo(a=2, b='puffer fish')

# incorrect types
foo(a='fish', b='puffer fish')
