def decorator_function(func):
    def wrapper(*args):
        print('Функция-обёртка!')
        print('Оборачиваемая функция: {}'.format(func))
        print('Выполняем обёрнутую функцию...')
        print('Сумма первых', *args, 'чисел Фибоначчи: ', sum(func(*args)))
        print('Первые', *args, 'чисел Фибоначчи: ', list(func(*args)))
        print('Выходим из обёртки')
        return func

    return wrapper


@decorator_function
def generator_of_fibonacci_numbers(n):
    fib1 = 0
    fib2 = 1
    for i in range(n):
        tmp = fib1 + fib2
        fib1 = fib2
        fib2 = tmp

        # fib1, fib2 = fib2, fib1 + fib2
        yield fib1


generator_of_fibonacci_numbers(20)
