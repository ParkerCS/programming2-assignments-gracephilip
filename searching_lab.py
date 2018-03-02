import re

file = open('search_files/dictionary.txt')

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)


def linear_search(word, dictionary_list, line_num):
    key = word
    for words in dictionary_list:
        if words == key.upper():
            break
    else:
        print("Line", line_num, "possible misspelled word:", word)



dictionary_list = []

for line in file:
    words = split_line(line)
    for word in words:
        dictionary_list.append(word)
print(dictionary_list)
file.close()

print("--- Linear Search ---")

file = open('search_files/AliceInWonderland200.txt')

line_num = 0
for line in file:
    words = split_line(line)
    line_num += 1
    for word in words:
        linear_search(word, dictionary_list, line_num)

file.close()

print("--- Binary Search ---")

file = open('search_files/AliceInWonderland.txt')




