import string
import time


def main():
    book_path = "books/Franskenstein.txt"
    contents = get_file_contents(book_path)
    single_words = split_words(contents)
    count_letters(contents)
    # print(contents)
    # print(single_words)


def get_file_contents(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents


def split_words(contents):
    words = contents.split()
    return words


def count_letters(contents):
    letter_frequency = {}

    # print(letters)

    # print(letter_frequency)
    start = time.time()
    letters = string.ascii_lowercase[:]
###################### Method1 : Define keys in dict first   time: 0.03897213935852051 ##############

    # for x in letters:
    #     letter_frequency[x] = 0
    # for i in contents.lower():
    #     if i in letter_frequency:
    #         letter_frequency[i] += 1
#####################Method 2: 1 loop    time: 0.03705883026123047#######################
    for i in contents.lower():
        if i in letter_frequency:
            letter_frequency[i] += 1
        elif i in letters:
            letter_frequency[i] = 1
        else:
            continue
    print(letter_frequency)
    end = time.time()
    print(end-start)


main()
