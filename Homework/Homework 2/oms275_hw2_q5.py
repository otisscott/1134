def split_parity(lst):
    for num in lst:
        if num % 2 == 0:
            lst.append(lst.pop(lst.index(num)))
    return lst
