import functools
import datetime


def log(filename=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            try:
                # Выполняем основную функцию
                result = func(*args, **kwargs)
                end_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                log_message = f'{start_time}: {func.__name__}({args}, {kwargs}) executed successfully at {end_time}. Result: {result}'

                # Определяем, куда записать логи
                if filename is not None:
                    with open(filename, 'a') as file:
                        file.write(log_message + '\n')
                else:
                    print(log_message)
                return result
            except Exception as e:
                # Если возникла ошибка, фиксируем её
                end_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                log_message = f'{start_time}: Error in function {func.__name__}({args}, {kwargs}). Type of error: {type(e).__name__}. Message: {str(e)}'

                if filename is not None:
                    with open(filename, 'a') as file:
                        file.write(log_message + '\n')
                else:
                    print(log_message)
                raise

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)