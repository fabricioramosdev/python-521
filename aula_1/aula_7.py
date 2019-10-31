def cache(fn):
        fn._cache = {}
        def wrapper(*args,**kwargs):
            if not args in fn._cache:
                fn._cache[args] =  fn(*args,  **kwargs)
            return fn._cache[args]
    return wrapper

def fib(n):
    