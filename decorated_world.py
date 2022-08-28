from typing import Callable
import functools


def decorator_with_args_for_any_decorator(decorator_to_enhance: Callable) -> Callable:
    """ Decorator. Allows another decorator to accept arbitrary arguments """

    def decorator_maker(*args, **kwargs) -> Callable:
        def decorator_wrapper(func: Callable) -> Callable:
            return decorator_to_enhance(func, *args, **kwargs)

        return decorator_wrapper

    return decorator_maker


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *dec_args, **dec_kwargs) -> Callable:
    """ Decorator pattern """

    @functools.wraps(func)
    def wrapper(*func_args, **func_kwargs) -> Callable:
        print('Passed args and quargs to the decorator:', dec_args, dec_kwargs)
        return func(*func_args, **func_kwargs)

    return wrapper


@decorated_decorator(100, 'rubles', 200, 'friends')
def decorated_function(text: str, num: int) -> None:
    print("Hi!", text, num)


decorated_function("User", 101)
