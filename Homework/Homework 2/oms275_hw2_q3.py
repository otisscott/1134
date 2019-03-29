def factors(num):
    for number in range(1, num + 1):
        if num % number == 0:
            yield number


print(factors(15))
