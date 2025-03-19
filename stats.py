def word_count(book_string):
    word_list = []
    word_list = book_string.split()
    return(len(word_list),word_list)

def char_count(word_list):
    string_dict = {}
    for word in word_list:
        word = word.lower()
        for letter in word:
            if letter in string_dict:
                string_dict.update({letter:string_dict[letter]+1})
            else:
                string_dict.update({letter:1})
    return string_dict



def sort_on(item):
    return item["occurance"]

def list_of_dict(string_dict):
    dictionaries_list = []
    for character in string_dict:
        dictionaries_list.append({"character":character,"occurance":string_dict[character]})
    
    dictionaries_list.sort(reverse=True,key=sort_on)
    return dictionaries_list
    # print(f"list of dict: {dictionaries_list}")


if __name__ == "__main__":
    # test_list = ["abcd","abcd","ABCD","#"]
    # print(char_count(test_list))



    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_list = []
    # print(file_contents)
    # word_list = file_contents.split(" ")
    # # This is a list
    # print(len(word_list))
    word_list = word_count(file_contents)
    list_of_dict(char_count(word_list))
    # print(f"{w_count} words found in the document")
    # print(char_count(word_list))
