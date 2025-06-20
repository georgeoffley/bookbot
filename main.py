from stats import get_num_words
from stats import count_characters

def get_book_text(file_path) -> str:
    with open(file_path) as file:
        file_contents = file.read()

        return file_contents

def main():
    file_content_string = get_book_text('./books/frankenstein.txt')
    word_count = get_num_words(file_content_string)
    collection = count_characters(file_content_string)

    print(f'{word_count} words found in the document')
    print(collection)

main()