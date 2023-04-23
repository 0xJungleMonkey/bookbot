This project is made from 0xJungleMonkey when she is crazy.
```python

def main():
    book_path = "books/Franskenstein.txt"
    contents = get_file_contents(book_path)
    single_words = split_words(contents)
    letter_dict = count_letters(contents)
    sorted_dict = sort_dict(letter_dict)
    generate_report(sorted_dict)
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
#####################  Method 2: 1 loop    time: 0.03705883026123047#######################
    for i in contents.lower():
        if i in letter_frequency:
            letter_frequency[i] += 1
        elif i in letters:
            letter_frequency[i] = 1
        else:
            continue
    end = time.time()
    print(end-start)
    return letter_frequency


def sort_dict(letter_frequency):
    sorted_dict = sorted(letter_frequency.items(),
                         key=lambda x: x[1], reverse=True)
    converted_dict = dict(sorted_dict)
    return converted_dict


def generate_report(sorted_dict):
    f = open("bookbotreport.txt", "w")
    f.write("Bookbot basic report:\n")
    for i in sorted_dict:
        f.write("The letter \"" + i + "\" is used " + str(sorted_dict[i])
                + " times.\n")


main()
```

    0.05390787124633789



```python
import time 
```


```python
import string
```


```python
def main():
    book_path = "books/Franskenstein.txt"
    contents = get_file_contents(book_path)
    single_words = split_words(contents)
    letter_dict = count_letters(contents)
    sorted_dict = sort_dict(letter_dict)
    generate_report(sorted_dict)
    print(sorted_dict)
    # print(single_words)
main()
```

    0.05623602867126465
    {'e': 46043, 't': 30365, 'a': 26743, 'o': 25225, 'i': 24613, 'n': 24367, 's': 21155, 'r': 20818, 'h': 19725, 'd': 16863, 'l': 12739, 'm': 10604, 'u': 10407, 'c': 9243, 'f': 8731, 'y': 7914, 'w': 7638, 'p': 6121, 'g': 5974, 'b': 5026, 'v': 3833, 'k': 1755, 'x': 677, 'j': 504, 'q': 324, 'z': 243}



```python
def generate_report(sorted_dict):
    f = open("bookbotreport.txt", "w")
    f.write("Bookbot basic report:\n")
    for i in sorted_dict:
        print("The letter \"" + i + "\" is used " + str(sorted_dict[i])
                + " times.\n")


main()
```

    0.0645449161529541
    The letter "e" is used 46043 times.
    
    The letter "t" is used 30365 times.
    
    The letter "a" is used 26743 times.
    
    The letter "o" is used 25225 times.
    
    The letter "i" is used 24613 times.
    
    The letter "n" is used 24367 times.
    
    The letter "s" is used 21155 times.
    
    The letter "r" is used 20818 times.
    
    The letter "h" is used 19725 times.
    
    The letter "d" is used 16863 times.
    
    The letter "l" is used 12739 times.
    
    The letter "m" is used 10604 times.
    
    The letter "u" is used 10407 times.
    
    The letter "c" is used 9243 times.
    
    The letter "f" is used 8731 times.
    
    The letter "y" is used 7914 times.
    
    The letter "w" is used 7638 times.
    
    The letter "p" is used 6121 times.
    
    The letter "g" is used 5974 times.
    
    The letter "b" is used 5026 times.
    
    The letter "v" is used 3833 times.
    
    The letter "k" is used 1755 times.
    
    The letter "x" is used 677 times.
    
    The letter "j" is used 504 times.
    
    The letter "q" is used 324 times.
    
    The letter "z" is used 243 times.
    
    {'e': 46043, 't': 30365, 'a': 26743, 'o': 25225, 'i': 24613, 'n': 24367, 's': 21155, 'r': 20818, 'h': 19725, 'd': 16863, 'l': 12739, 'm': 10604, 'u': 10407, 'c': 9243, 'f': 8731, 'y': 7914, 'w': 7638, 'p': 6121, 'g': 5974, 'b': 5026, 'v': 3833, 'k': 1755, 'x': 677, 'j': 504, 'q': 324, 'z': 243}



```python

```


```python

```


```python

```
