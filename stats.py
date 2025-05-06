def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    char_counter = {}
    for char in text.lower():
        if char not in char_counter:
            char_counter[char] = 0
        char_counter[char] += 1
    return char_counter

def sort_on(dict):
    return dict["count"]

def get_sorted_character_counts(char_count):
    list = []
    for char, count in char_count.items():
        if char.isalpha():
            list.append({"char": char, "count": count})
    list.sort(reverse=True, key=sort_on)
    return list
    