def shift(lst, k, direction="left"):
    lst_copy = lst.copy()
    for ind in range(len(lst)):
        if direction == "left":
            if ind + k >= len(lst):
                lst[ind] = lst_copy[abs(len(lst) - (ind + k))]
            else:
                lst[ind] = lst_copy[ind + k]
        else:
            if ind - k < 0:
                lst[ind] = lst_copy[len(lst) - k + ind]
            else:
                lst[ind] = lst_copy[ind - k]
    return lst
