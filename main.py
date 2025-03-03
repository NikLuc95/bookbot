#def get_book_text(path_to_file):
#
#    with open(path_to_file) as f:
#        file_contents = f.read()
#   return file_contents
#
#file_contents = get_book_text("/home/nik/workspace/github.com/NikLuc95/bookbot/books/frankenstein.txt")
#
#def main():
#
#    print(file_contents)

def count_book_text(path_to_file):

    with open(path_to_file) as f:
        file_contents = f.read()
        num_words = len(file_contents.split())

    return num_words

num_words = count_book_text("/home/nik/workspace/github.com/NikLuc95/bookbot/books/frankenstein.txt")

def main():

    print(f"{num_words} words found in the document")

main()