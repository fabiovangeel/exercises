def last_digit(x):
    return x % 10


def remove_last_digit(x):
    return x // 10


def digit_sum(x):
    sum = 0
    while x > 0:
        sum += last_digit(x)
        x = remove_last_digit(x)
    return sum
