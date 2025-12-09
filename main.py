from stats import words_in_string, character_count, char_to_dict
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
        

    book = get_book_text(book_path)
    num_words = words_in_string(book)
    each_char_count = character_count(book)
    dict_of_chars = char_to_dict(each_char_count)

    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in dict_of_chars:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")
    
    

main()