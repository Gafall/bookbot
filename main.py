def word_counter(book):
    count = len(book.split())
    return count

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(word_counter(file_contents))

main()