from stats import count_book_text, count_book_characters, char_list

path = "/home/nik/workspace/github.com/NikLuc95/bookbot/books/frankenstein.txt"

count = count_book_characters(path)

num_words = count_book_text(path)

dicts = char_list(count)

def main():

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
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
