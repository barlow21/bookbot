import sys
from stats import get_word_count, get_character_count, get_sorted_character_counts

def get_book_text(book_path):
    with open(book_path) as book:
        book_content = book.read()
        return book_content    

def main():
    print(sys.argv)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    bookcontent = get_book_text(book_path)
    word_count = get_word_count(bookcontent)
    character_count = get_character_count(bookcontent)
    sorted_character_count = get_sorted_character_counts(character_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for entry in sorted_character_count:
        print(f"{entry["char"]}: {entry["count"]}")
    
    print("============= END ===============")

main()