def find_duplicates(lst):
    dupes = []
    for num in range(len(lst)):
        if lst[abs(lst[num])] >= 0:
            lst[abs(lst[num])] = -lst[abs(lst[num])]
        else:
            dupes.append(abs(lst[num]))
    return dupes
