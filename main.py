def get_book_text(path):
    with open(path) as f:
        return f.read()

from stats import count_words, character_counts, chars_dict_to_sorted_list

def main():
    path = "books/frankenstein.txt"
    book_text = get_book_text(path)
    num_words = count_words(book_text)
    
    char_counts = character_counts(book_text)
    sorted_chars = chars_dict_to_sorted_list(char_counts)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        # Only print alphabetic characters
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")


main()

