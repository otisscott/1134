def findChange(lst01):
    for num in range(len(lst01) - 1, 0, -1):
        print(lst01[num], num)
        if lst01[num - 1] == 0:
            return num
