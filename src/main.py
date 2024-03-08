import traceback


def count_words(text: str) -> tuple[dict, int]:
    word_dictionary = {}
    for word in text.split():
        lowered = word.lower()
        count = word_dictionary.get(lowered) or 0
        word_dictionary[lowered] = count + 1
    return word_dictionary, len(text)


def count_characters(text: str) -> tuple[dict, int]:
    char_dictionary = dict()
    for char in text:
        lowered = char.lower()
        count = char_dictionary.get(lowered) or 0
        char_dictionary[lowered] = count + 1
    return char_dictionary, len(text)


def sort_on(view):
    return view[1]


def print_report(file_path, view, word_count):
    print(f'--- Begin report of {file_path} ---')
    print(f'{word_count} words found in the document')
    for char, count in view:
        if not char.isalpha():
            continue
        print(f'The {char} character was found {count} times')
    print('--- End of report ---')


def main():
    file_path = './books/frankenstein.txt'
    try:
        with open(file_path) as file:
            file_contents = file.read()
            char_dictionary, char_count = count_characters(file_contents)
            word_dictionary, word_count = count_words(file_contents)
            view = sorted(char_dictionary.items(), key=sort_on, reverse=True)
            print_report(file_path, view, word_count)
    except Exception:
        traceback.print_exc()


if __name__ == '__main__':
    main()
