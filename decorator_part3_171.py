# this line use for the decorator function showing doc msg
from functools import wraps

def decorator_function(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):
        """this is wrapper function """
        print('this is owesome function')
        return any_function(*args,**kwargs)
    return wrapper_function


@decorator_function
def add(a,b):
    '''this add function '''
    return a+b

print(add.__doc__)
print(add.__name__)


# print(add(5,7))