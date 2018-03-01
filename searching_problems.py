'''
Complete the following 3 searching problems using techniques
from class and from Ch15 of the textbook website
'''
import re

# This function takes in a line of text and returns a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

#1.  (7pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.  (read the file line by line to accomplish this task)
file = open('search_files/dictionary.txt', 'r')
all_words = []

for line in file:
    words = split_line(line)
    for word in words:
        all_words.append(word)

lengths = [len(x) for x in all_words]
print(all_words[lengths.index(max(lengths))])

file.close()

#2.  (7pts)  Write code which finds
#  The total word count AND average word length of "AliceInWonderLand.txt"

file = open('search_files/AliceInWonderland.txt')

word_count = 0
word_len = []
average = 0

for line in file:
    words = split_line(line)
    for word in words:
        word_count += 1
        word_len.append(len(word))

print(word_count)

print(sum(word_len) / len(word_len))


# CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS

#3 (13pts)  How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?

cheshire_num = 0
Cheshire = False
file = open('search_files/AliceInWonderland.txt', 'r')
all_words = []

for line in file:
    words = split_line(line)
    for word in words:
        all_words.append(word)

for word in all_words:
    if word == "Cheshire":
        Cheshire = True


for i in range(len(all_words)):
    if all_words[i] == "Cheshire":
        if all_words[i + 1].upper() == "CAT":
            cheshire_num += 1
print(cheshire_num)


#### OR #####

#3  (13pts)Find the most frequently occurring 
#  seven letter word in "AliceInWonderLand.txt"




# CHALLNENGE PROBLEM  (for fun, not for credit).  
#  What words appear in the text of "Alice in Wonderland" that DO NOT occur in "Alice Through the Looking Glass".  Make a list.  You can substitute this for any of the above problems.




