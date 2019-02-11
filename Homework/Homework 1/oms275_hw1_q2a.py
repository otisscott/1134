def shift(lst, k):
    lst_copy = lst.copy()
    for ind in range(len(lst)):
        if ind + k >= len(lst):
            lst[ind] = lst_copy[abs(len(lst) - (ind + k))]
        else:
            lst[ind] = lst_copy[ind + k]
    return lst
