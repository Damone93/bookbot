import sys
sys.argv == ["main.py", "books/frankenstein.txt"]
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]
with open(book_path) as get_book_text:
    word_dict = {}
    main = get_book_text.read()
    words = main.lower()
    num_words = words.split()
    num_of_words = len(num_words)
    #To count characters and add them to dictionary
    for character in words:
        if character in word_dict:
            word_dict[character] += 1
        else:
            word_dict[character] = 1

from stats import sort_dict
sortword = sort_dict(word_dict)
print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print("Found", num_of_words, "total words")
print("--------- Character Count -------")
for values in sortword:
    char = values["char"]
    num = values["num"]
    if char.isalpha():
        print(f"{char}: {num}")
print("============= END ===============")