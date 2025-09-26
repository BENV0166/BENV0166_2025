import time

def square(x):
    return x**2

def slow_square(x):
    # Slow the performance down by doing some needless calculations
    A = 1
    for i in range(200):
        A += 1

    return x**2