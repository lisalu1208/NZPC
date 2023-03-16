"""
Shona is a linguistics student who has an assignment to analyse letter distribution in
sentences taken from various sources. Your task is to write a program to help her.

The problem is to plot a graph showing how many of each letter appear in the sentence
supplied. Upper and lower case letters are considered the same letter. Characters that are
not letters of the English alphabet are ignored.

input:

The input consists of a single line of text of no more than 250 characters. At least one
character will be a letter.

output:
Output consists of a graph with 26 horizontal bars. The letters of the alphabet (upper case)
form the y axis, in alphabetical order from top to bottom. Each is followed by a space, a vertical
bar, another space then a star for every time that letter appears in the supplied text. There
are no spaces between the stars.
"""

# Get input string and convert it to all uppercases
sentence = input().upper()

# Create a dictionary with all the alphabets as keys and 0 as values
alphabetDict = {chr(ord('A') + i): 0 for i in range(26)}

if len(sentence) <= 250:
    for ch in sentence:
        if ch.isalpha():
            alphabetDict[ch] += 1

for alph, value in alphabetDict.items():
    output = alph + " | "
    for i in range(value):
        output += "*"
    print(output)

