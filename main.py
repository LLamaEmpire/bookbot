from stats import *
import sys

if len(sys.argv) != 2:
    
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else: 
    path_to_file = sys.argv[1]

# path_to_file = "books/frankenstein.txt"

with open(path_to_file) as f:
    file_contents = f.read()
# word_list = []
# print(file_contents)
# word_list = file_contents.split(" ")
# # This is a list
# print(len(word_list))
# w_count, word_list = word_count(file_contents)

# print(f"{w_count} words found in the document")
# print(char_count(word_list))


# word_count gets my string...
# word_count_value = word_count(file_contents)
# dict_list = list_of_dict(word_count_value)

w_count, word_list = word_count(file_contents)
dict_list = list_of_dict(char_count(word_list))


def print_report(dict_list,w_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------)")
    print(f"Found {w_count} total words")
    print("--------- Character Count -------")
    for char_pair in dict_list:
        if not char_pair["character"].isalpha():
            continue
        else:
            print(f"{char_pair['character']}: {char_pair['occurance']}")
    print("============= END ===============")

print_report(dict_list,w_count)