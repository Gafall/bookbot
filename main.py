def read_file_contents(filepath):
    with open(filepath) as f:
        return f.read()

def word_counter(book):
    count = len(book.split())
    return count

def main():
    frankenstein_book_path = "books/frankenstein.txt"
    frankenstein_book = read_file_contents(frankenstein_book_path)
    word_count = word_counter(frankenstein_book)
    print(f"Frankenstein has {word_count} words")

main()