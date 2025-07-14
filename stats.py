from operator import itemgetter

def num_words(book_text: str):
    return len(book_text.split())

def character_frequency(book_text: str):
    book_text_lower = book_text.lower()
    character_frequency = {}
    for character in book_text_lower:
        if character in character_frequency:
            character_frequency[character] += 1
        else:
            character_frequency[character] = 1
    return character_frequency

def sort_on(items):
    return(items['num'])

def generate_sorted_dicts(char_freq: dict):
    dicts_list = []
    for key, value in char_freq.items():
        char_dict = {}
        char_dict["char"] = key
        char_dict["num"] = value
        dicts_list.append(char_dict)
    return sorted(dicts_list, key=itemgetter('num'), reverse = True)
