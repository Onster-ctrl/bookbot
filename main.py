def get_book_text(path):
    with open(path) as f:
        return f.read()

from stats import count_words

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document")

main()

