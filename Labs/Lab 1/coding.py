import random


# 1.)
def binary_converter(bin_str):
    final = 0
    for num in range(len(bin_str)):
        final += int(bin_str[num]) * (2**num)
    return final


def string_converter(bin_num):
    return string_converter(bin_num >> 1) + [bin_num & 1] if bin_num > 1 else [1]


def add_binary(bin_num1, bin_num2):
    """
    bin_num1 - type: str
    bin_num2 - type: str
    return value - type: str
    """
    num1, num2 = binary_converter(bin_num1), binary_converter(bin_num2)
    total = num1 + num2
    final = ""
    for each in string_converter(total):
        final += str(each)
    return final


print(add_binary("11", "1"))


# 2.)
def can_construct(word, letters):
    """
    word - type: str
    letters - type:str
    return value - type:bool
    """
    word_list = list(word)
    for let1 in range(len(letters)):
        if letters[let1] in word_list:
            word_list.remove(letters[let1])
    if len(word_list) > 0:
        return False
    return True


print(can_construct("apples", "aples"))
print(can_construct("apples", "aplespl"))


# 3.)
def rand_num(lst, n):
    rand = random.randint(0, n - 1)
    if rand in lst:
        rand_num(lst, n)
    else:
        lst.append(rand)
        return lst


def create_permutation(n):
    """
    n - type: int
    return value - type: list
    """
    final = []
    for num in range(n):
        rand_num(final, n)
    return final


def scramble_word(word):
    """
    word - type: String
    return value - type: String
    """
    scrambled = create_permutation(len(word))
    final_str = ""
    for num in scrambled:
        final_str += word[num]
    return final_str


def guessing_game(word):
    scrambled_word = scramble_word(word)
    scrambled_word = " ".join(scrambled_word)
    print("Unscrambled the word: ", scrambled_word)
    for i in range(3):
        inp = input("Try #" + str(i+1) + ": ")
        if inp == word:
            print("Yay, you got it!")
            break
        elif i == 2:
            print("Sorry, you failed :(")
        else:
            print("Wrong!")


print(scramble_word("pokemon"))
print(create_permutation(6))
guessing_game("pokemon")
