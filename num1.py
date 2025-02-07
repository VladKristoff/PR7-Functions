def get_input():
    input_string = input("Введите строку фраз: ")
    sample_string = input("Введите строку-образец: ")
    return input_string, sample_string

def split_phrases(input_string):
    return input_string.split('; ')

def get_unique_chars(string):
    return set(string.lower())

def filter_phrases(phrases, sample_set):
    filtered_phrases = []
    for phrase in phrases:
        phrase_set = get_unique_chars(phrase)
        common_chars = len(sample_set.intersection(phrase_set))
        if common_chars <= 3:
            filtered_phrases.append(phrase)
    return filtered_phrases

def main():
    input_string, sample_string = get_input()
    phrases = split_phrases(input_string)
    sample_set = get_unique_chars(sample_string)
    filtered_phrases = filter_phrases(phrases, sample_set)
    result = ' # '.join(filtered_phrases)
    print(f"Результат: {result}")


main()