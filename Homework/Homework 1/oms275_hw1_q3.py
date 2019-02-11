def sum_squares(n):
    total = 0
    for num in range(n):
        total += num**2
    return total


def sum_squared_lst_comp(n):
    return sum([x**2 for x in range(n)])


def sum_odd_squares(n):
    total = 0
    for num in range(1, n, 2):
        total += num**2
    return total


def sum_odd_squares_lst_comp(n):
    return sum([x**2 for x in range(1, n, 2)])
