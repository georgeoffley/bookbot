from stats import get_num_words
from stats import count_characters
from stats import pretty_list
import sys

def get_book_text(file_path) -> str:
    with open(file_path) as file:
        file_contents = file.read()

        return file_contents

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    file_path = sys.argv[1]
    # file_path = './books/frankenstein.txt'
    file_content_string = get_book_text(file_path)
    word_count = get_num_words(file_content_string)
    collection = count_characters(file_content_string)
    report = pretty_list(collection)


    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {file_path}')
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print ('--------- Character Count -------')
    for entries in report:
        print(f'{entries['char']}: {entries['num']}')
    print('============= END ===============')

main()