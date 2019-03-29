def remove_all(lst, value):
    for num in range(len(lst)):
        try:
            if lst[num] == value:
                del lst[num]
        except IndexError:
            pass
    if value in lst:
        remove_all(lst, value)
