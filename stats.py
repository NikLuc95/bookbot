def count_book_text(path_to_file):

    with open(path_to_file) as f:
        file_contents = f.read()
        num_words = len(file_contents.split())

    return num_words

def count_book_characters(path_to_file):

    count = {}

    with open(path_to_file) as f:
        file_contents = f.read()
        list_characters = list(file_contents.lower())
        
        import string

        characters = list(string.printable)

    for character in characters:
        
        count[character] = list_characters.count(character)

    return count