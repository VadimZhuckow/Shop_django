#
# def decorator(fn):
#     def wrapper(*args, **kwargs):
#
#         result = fn(*args, **kwargs)
#
#         return result
#
#     return wrapper
#
#
# def my_time(fn):
#     def wrapper(*args, **kwargs):
#         # Выполнить что-то до вызова исходной функции
#         t0 = time()
#
#         # Вызов исходной функции, которая сидит в аргументе fn
#         result = fn(*args, **kwargs)
#
#         # Выполнить что-то после вызова исходной функции
#         dt = time() - t0
#         print(f"Время выполнения {dt}")
#
#         return result
#
#     return wrapper


def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции: {func.name} с аргументами {args} и {kwargs}")
        result = func(*args, **kwargs)
        print(f"Функция {func.name} завершилась с результатом {result}")
        return result
    return wrapper

@log_decorator
def add(x, y):
    """Складывает два числа."""
    return x + y

# Вызов декорированной функции
add(5, 3)
