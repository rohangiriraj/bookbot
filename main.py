from stats import num_words, character_frequency, generate_sorted_dicts
import sys

def get_book_text(file_path: str):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {file_path}...')
    book_str = get_book_text(file_path)
    print('----------- Word Count ----------')
    print(f"Found {num_words(book_str)} total words")
    print('--------- Character Count -------')
    char_freq_dict = character_frequency(book_str)
    sorted_freq_dict = generate_sorted_dicts(char_freq_dict)
    for i in sorted_freq_dict:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")
    print('============= END ===============')
main()
