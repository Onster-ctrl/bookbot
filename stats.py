def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def character_counts(text):
    counts = {}
    text = text.lower()
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts