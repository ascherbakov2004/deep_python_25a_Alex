import time

def retry_deco(retries=3, exceptions=None):
    if exceptions is None:
        exceptions = []

    def decorator(func):
        def wrapper(*args, **kwargs):
            attempt = 1
            while attempt <= retries:
                try:
                    print(f"run \"{func.__name__}\" with positional args = {args}, "
                          f"keyword kwargs = {kwargs}, attempt = {attempt}")
                    
                    result = func(*args, **kwargs)

                    print(f"run \"{func.__name__}\" with positional args = {args}, "
                          f"keyword kwargs = {kwargs}, attempt = {attempt}, result = {result}")
                    return result

                except Exception as e:
                    print(f"run \"{func.__name__}\" with positional args = {args}, "
                          f"keyword kwargs = {kwargs}, attempt = {attempt}, exception = {str(e)}")

                    if type(e) in exceptions:
                        return None

                    attempt += 1

            print(f"run \"{func.__name__}\" with positional args = {args}, "
                  f"keyword kwargs = {kwargs}, attempt = {retries}, exception = {str(e)}")
            return None

        return wrapper

    return decorator


def mean(n):
    if n <= 0:
        raise RuntimeError("n должно быть больше 0")

    def inner_mean(func):
        time_n_iter = [0] * n
        iteration_num = 0
        sum_times = 0

        def inner(*args, **kwargs):
            start_ts = time.time()
            result = func(*args, **kwargs)
            end_ts = time.time()

            nonlocal sum_times
            nonlocal iteration_num

            iteration_num += 1
            sum_times -= time_n_iter[iteration_num % n]
            time_n_iter[iteration_num % n] = end_ts - start_ts
            sum_times += time_n_iter[iteration_num % n]

            if iteration_num >= n:
                print(
                    f"Время выполнения последних {n} "
                    f"итераций функции {func.__name__} : {sum_times/n:.3f}"
                )

            return result

        return inner

    return inner_mean


