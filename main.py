import string


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
    account_of_letters = None
    letters = string.ascii_lowercase[:]
    print(letters)


main()
