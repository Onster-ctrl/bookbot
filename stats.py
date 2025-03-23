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


def chars_dict_to_sorted_list(char_dict):
    chars_list = []
    for char, count in char_dict.items():
        chars_list.append({"char": char, "count": count})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

def sort_on(dict):
    return dict["count"]
