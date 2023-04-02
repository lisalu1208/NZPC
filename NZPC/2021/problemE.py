"""
problemE:

I am trying to create a dictionary of all the words in common use by my students. To
do this, I am planning to feed text from their work, discussion forum entries and emails
through a program that extracts the words.
To make it easy to check if a word has been seen before, I am
formatting the text carefully. Firstly, I put everything in lower
case, then I strip out all punctuation leaving the words separated
by single spaces. If the punctuation comes within a word, it is
removed and not replaced with a space. If a "word" consists only
of digits, it is ignored. Finally, I sort the words into alphabetical
order, removing duplicates.
Punctuation is considered to be anything that is not a letter, a number or white space

Input:

Input will consist of a piece of text to be analysed. It will be a single line which will
contain no more than 250 characters, and will contain at least one word which can be
extracted. 

Output:

Output will be the qualifying words extracted from the text, one per line, in alphabetical
order. 
"""

line = input().lower()

