import sys
from stats import get_num_words, get_num_characters, get_sorted_character_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    book_word_count = get_num_words(book_text)
    unsorted_num_character = get_num_characters(book_text)
    sorted_num_characters = get_sorted_character_dict(unsorted_num_character)

    print("============ BOOKBOT ============")
    print("Analyzing book found at ", book_path, "...", sep="")
    print("----------- Word Count ----------")
    print("Found" ,book_word_count, "total words")
    print("--------- Character Count -------")
    for char in sorted_num_characters:
        if char['char'].isalpha():
            print(char['char'], ": ", char['num'], sep= "")
    print("============= END ===============")

main()
