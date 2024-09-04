def read_file_contents(filepath):
    with open(filepath) as f:
        return f.read()

def word_counter(book):
    count = len(book.split())

    return count

def character_counter(book):
    character_count = {}
    book_lowered = book.lower()
    for char in book_lowered:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    return character_count

def convert_character_dict_to_list_of_dict(dict):
    lst = []
    for key in dict:
        lst.append({"char": key, "num": dict[key]})
    return lst

def sort_on(dict):
    return dict["num"]

def print_report(path, word_count, character_list):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print()
    for char in character_list:
        if char["char"].isalpha():
            print(f"The '{char['char']}' character was found {char['num']} times")
    print("--- End report ---")


def main():
    frankenstein_book_path = "books/frankenstein.txt"
    frankenstein_book = read_file_contents(frankenstein_book_path)
    word_count = word_counter(frankenstein_book)
    character_dict = character_counter(frankenstein_book)
    character_list = convert_character_dict_to_list_of_dict(character_dict)
    character_list.sort(reverse=True, key=sort_on)
    print_report(frankenstein_book_path, word_count, character_list)

main()