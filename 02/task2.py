import functools

def retry_deco(retries=3, exception_classes=None):
    if exception_classes is None:
        exception_classes = []

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 1
            while attempt <= retries:
                try:
                    print(f"run \"{func.__name__}\" with positional args = {args}, keyword kwargs = {kwargs}, attempt = {attempt}")
                    result = func(*args, **kwargs)
                    print(f"run \"{func.__name__}\" with positional args = {args}, keyword kwargs = {kwargs}, attempt = {attempt}, result = {result}")
                    return result
                except Exception as e:
                    if isinstance(e, tuple(exception_classes)):
                        print(f"run \"{func.__name__}\" with positional args = {args}, keyword kwargs = {kwargs}, attempt = {attempt}, exception = {e.__class__.__name__}")
                        return None
                    else:
                        print(f"run \"{func.__name__}\" with positional args = {args}, keyword kwargs = {kwargs}, attempt = {attempt}, exception = {e.__class__.__name__}")
                        attempt += 1
                        if attempt > retries:
                            return None
        return wrapper
    return decorator

