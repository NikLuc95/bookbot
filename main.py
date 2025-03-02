def get_book_text(path_to_file):

    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

file_contents = get_book_text("/home/nik/workspace/github.com/NikLuc95/bookbot/books/frankenstein.txt")

def main():

    print(file_contents)
    
main()