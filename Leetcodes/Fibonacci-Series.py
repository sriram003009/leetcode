def fibonacci_series(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_series(n - 1) + fibonacci_series(n - 2)


n = 15
numbers = [fibonacci_series(i) for i in range(n + 1)]
print("Fibonacci numbers F(0) through F(%d):" % n)
print(numbers)