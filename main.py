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


def main():
    frankenstein_book_path = "books/frankenstein.txt"
    frankenstein_book = read_file_contents(frankenstein_book_path)
    word_count = word_counter(frankenstein_book)
    print(f"Frankenstein has {word_count} words")
    print(character_counter(frankenstein_book))
main()