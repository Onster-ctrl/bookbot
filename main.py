def get_book_text(path):
    with open(path) as f:
        return f.read()

from stats import count_words
from stats import character_counts

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document")
    
    char = character_counts(book_text)
    for char, count in char.items():
        print(f"'{char}': {count}")


main()

