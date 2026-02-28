import time
import tracemalloc

def measure_execution_time(func):
    def timed_execution(*args, **kwargs):
        start_timestamp = time.time()
        result = func(*args, **kwargs)
        end_timestamp = time.time()
        execution_duration = end_timestamp - start_timestamp
        print(f"Function {func.__name__} took {execution_duration:.2f} seconds to execute")
        return result
    return timed_execution

def measure_memory_usage(target_function):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        # Call the original function
        result = target_function(*args, **kwargs)

        snapshot = tracemalloc.take_snapshot()
        top_stats = snapshot.statistics("lineno")
        
        # Print the top memory–consuming lines
        print(f"Memory usage of {target_function.__name__}:")
        for stat in top_stats[:5]:
            print(stat)
    # Return the result
        return result
    return wrapper

#2
# @measure_memory_usage
# @measure_execution_time
# def calculate_fibonacci_recursion(number):
#     def calculate(n):
#         if n > 1:
#             value = calculate(n - 2) + calculate(n - 1)
#         elif n == 1:
#             value = 1
#         else:
#             value = 0
#         return value
#     return calculate(number)

# # Call the decorated function
# result = calculate_fibonacci_recursion(int(input("Введите число")))
# print(f"Result: {result}")

#3
# @measure_memory_usage
# @measure_execution_time
# def calculate_fibonacci_recursion(number):
#     if number > 1:
#         value, b = 0, 1
#         for n in range(number):
#             value, b = b, value + b
#     elif number == 1:
#         value = 1
#     else:
#         value = 0

#     return value

# # Call the decorated function
# result = calculate_fibonacci_recursion(int(input("Введите число")))
# print(f"Result: {result}")

#4
@measure_execution_time
def get_max_consecutive_elements(result_string):
    counter = 1
    count_max = 1
    for s in range(1, len(result_string)):
        if result_string[s] == result_string[s-1]:
            counter += 1
        else:
            if counter > count_max:
                count_max = counter
            counter = 1
    return max(count_max, counter)

# Call the decorated function
result = get_max_consecutive_elements(str(input("Введите строку:")))
print(f"Result: {result}")
