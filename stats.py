def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def character_counts(text):
    char_dict = {}
    text = text.lower()
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict