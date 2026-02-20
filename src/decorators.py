import time
from email.generator import Generator
from functools import wraps
from typing import Any


def log(filename: Any = None) -> Generator:
    def decorator(func: Any) -> Generator:
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.strftime("%Y-%m-%d %H:%M:%S")
            try:
                result = func(*args, **kwargs)
                end_time = time.strftime("%Y-%m-%d %H:%M:%S")
                log_message = f"{start_time}: {func.__name__} {args}, {kwargs} ok at {end_time}. Result: {result}"
                if filename is not None:
                    with open(filename, "a") as file:
                        file.write(log_message + "\n")
                else:
                    print(log_message)
                return result
            except Exception as e:
                end_time = time.strftime("%Y-%m-%d %H:%M:%S")
                log_message = (
                    f"{start_time}: "
                    f"{func.__name__} error: {type(e).__name__} at {end_time}. "
                    f"Inputs: {args}, {kwargs}"
                )
                if filename is not None:
                    with open(filename, "a") as file:
                        file.write(log_message + "\n")
                else:
                    print(log_message)
                raise

        return wrapper

    return decorator
