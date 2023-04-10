def decor(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print('Func call')
        return res

    return wrapper


@decor
def sum_(a, b):
    return a + b

# Same

sum_ = decor(sum_)
