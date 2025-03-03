from stats import count_book_text, count_book_characters

count = count_book_characters("/home/nik/workspace/github.com/NikLuc95/bookbot/books/frankenstein.txt")

num_words = count_book_text("/home/nik/workspace/github.com/NikLuc95/bookbot/books/frankenstein.txt")

def main():

    print(f"{num_words} words found in the document")
    print(count)

main()