import functools


def log(filename=None):
    """декоратор логирования вызовов функций"""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok\n"
            except Exception as e:
                message = f"{func.__name__} error: {e.__class__.__name__}, {args}, {kwargs}\n"
                result = None

            if filename:
                with open(filename, "w", encoding="utf-8") as f:  # Изменено на "w"
                    f.write(message)
            else:
                print(message)

            return result

        return wrapper

    return decorator


"""декоратор логирования вызовов функций"""


@log("mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)


"""функция складывания"""


@log()
def error_function(x):
    return 1 / x


error_function(0)


"""функция деления на ноль"""
