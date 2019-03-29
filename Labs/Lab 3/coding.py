#1.)


def reverse_list(lst):
    """
    : lst type: list[]
    : return type: None
    """
    lst[::-1]


#2.)


def is_palindrome(s):
    """
    : s type: str
    : return type: bool
    """
    if s[:len(s)//2] == s[:len(s)//2:-1]:
        return True
    else:
        return False


#3.)


def move_zeroes(nums):
    """
    : nums type: list[int]
    : return type: None
    """
    for num in range(len(nums)):
        if nums[num] == 0:
            nums.append(nums.pop(num))


#4.) b.)


def find_missing(lst):
    """
    : nums type: list[int] (sorted)
    : return type: int
    """
    for num in range(len(lst)):
        if lst[num] != num:
            return num


def find_missing_unsorted(lst):
    """
    : nums type: list[int] (unsorted)
    : return type: int
    """
    full_range = list(range(len(lst) + 1))
    li_dif = [i for i in lst + full_range if i not in lst]
    return li_dif[0]


def main():
    my_list = [1, "dicks", ["hi"]]
    reverse_list(my_list)
    print(my_list)

    print(is_palindrome("racecar"))
    print(is_palindrome("this is not a palindrome"))

    my_nums = [0, 1, 0, 3, 13, 0]
    move_zeroes(my_nums)
    print(my_nums)

    unsorted = [8, 6, 0, 4, 3, 5, 1, 2]
    lst = unsorted.copy()
    lst.sort()
    print(find_missing(lst))

    print(find_missing_unsorted(unsorted))


main()
