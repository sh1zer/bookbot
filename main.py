def main():
    path_to_file = "books/frankenstein.txt"
    text_in_file = get_book_text(path_to_file)
    words_count_in_file = count_words(text_in_file)
    char_count_in_file = count_chars(text_in_file)
    sorted_char_counter = sort_dict(char_count_in_file)


    print(f" --- Begin report of {path_to_file} --- ")
    print(f"{words_count_in_file} words found in file")
    for ele in sorted_char_counter:
        if ele[0].isalpha():
            print(f"The \'{ele[0]}\' characted was found {ele[1]} times")
    print(" --- End of report ---")


def get_book_text(path_to_file):
     with open(path_to_file) as f:
        text_in_file = f.read()
        return text_in_file

def count_words(text):
    return len(text.split())

def count_chars(text):
    new_text = text.lower()
    counter = {}
    for c in new_text:
        counter[c] = counter.get(c, 0) + 1
    return counter    

def sort_dict(dic):
    new = [(key, dic[key]) for key in dic.keys()]
    new.sort(reverse=True, key=lambda x: x[1])
    return new

main()