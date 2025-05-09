from time import time


def speed_check(function):
    def wrapper_function():
        start_time = time()
        function()
        end_time = time()
        print(f"{function.__name__} speed check : {end_time - start_time}s")
    return wrapper_function

@speed_check
def fast_function():
    for i in range(10000):
        i * i

@speed_check
def slow_function():
    for i in range(1000000):
        i * i


fast_function()
slow_function()