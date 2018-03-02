import re

file = open('search_files/dictionary.txt')

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)


dictionary_list = []

for line in file:
    words = split_line(line)
    for word in words:
        dictionary_list.append(word)
print(dictionary_list)
file.close()

print("--- Linear Search ---")
