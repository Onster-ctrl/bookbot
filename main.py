import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)  
book_path = sys.argv[1]
print(f"Book path provided: {book_path}")

def get_book_text(path):
    with open(path) as f:
        return f.read()

from stats import count_words, character_counts, chars_dict_to_sorted_list

def main():
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    
    char_counts = character_counts(book_text)
    sorted_chars = chars_dict_to_sorted_list(char_counts)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")


main()

