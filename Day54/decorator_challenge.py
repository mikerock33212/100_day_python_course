import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(function_to_be_decorate):
    def wrapper_func():
        start_time = time.time()
        function_to_be_decorate()
        end_time = time.time()
        print(f'Start time: {start_time}, End time: {end_time}')
        print(f'{function_to_be_decorate.__name__} ran speed: {end_time - start_time} s.')
    return wrapper_func


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()




