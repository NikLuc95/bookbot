import sys 

from stats import count_book_text, count_book_characters, char_list

count = count_book_characters(sys.argv[1])

num_words = count_book_text(sys.argv[1])

dicts = char_list(count)

def main():

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for item in dicts:
        char = item["character"]
        count = item["count"]
        if char.isalpha() and char.islower():
            print(f"{char}: {count}")

    print("============= END ===============")

main()
