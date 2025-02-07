def input_strings():
    string1 = input('Введите строку №1: ')
    string2 = input('Введите строку №2: ')
    string3 = input('Введите строку №3: ')
    return string1, string2, string3


def process_strings(string1, string2, string3):
    words_set = set(string1.split() + string2.split() + string3.split())
    words_list = list(words_set)
    return words_list


def find_longest_word(words):
    words.sort(key=lambda x: (-len(x), x))
    return words[0] if words else ""


def main():
    string1, string2, string3 = input_strings()

    unique_words = process_strings(string1, string2, string3)

    longest_word = find_longest_word(unique_words)

    print('+'.join(unique_words))
    print(longest_word)


main()