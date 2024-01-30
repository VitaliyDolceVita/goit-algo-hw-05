def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

    return fibonacci

# Приклад використання
fib = caching_fibonacci()
print(fib(5))  # Виведе 5 (0, 1, 1, 2, 3, 5)
print(fib(10))
print(fib(15))
print([fib(x) for x in range(16)])
