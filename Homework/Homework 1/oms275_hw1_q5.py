def fibs(n):
    second, last = 1, 1
    for num in range(n):
        yield second  #Not sure if I'm allowed to use this, but it makes the solution so much more simple
        second, last = last, second + last
