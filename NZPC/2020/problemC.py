"""
problemC:

A nasty virus has infected my computer. Its effect has been to attack all my text files
and reverse every word in them. Your job in this problem is to write the code to restore
my text files to their original condition.
As far as the virus was concerned, a word was any sequence of characters that ended
with a space or an end of line character. You will see what I mean when I tell you that
the first line in one of my files was:
Get ready for the New Zealand Programming Contest on 26th September.
The virus turned this into:
teG ydaer rof eht weN dnalaeZ gnimmaroorP tsetnoC no ht62 .remetpeS
See how it included the full stop with September and put it before the letters?

Input:

Input will consist of a single line containing from 1 to 250 characters, which will start
and end with a non-white space character. There will not be any tab characters. There
will be only 1 space between words or between a sentence terminator (. ? or !) and the
next sentence.

Output:

Output will consist of one line where each word (as defined in paragraph 2 above) in
the input line has been reversed.
"""

line = input()
line_rev = []
if 1 <= len(line) <= 250:
    words = line.split(" ")
    for w in words:
        w_rev = w[::-1]
        line_rev.append(w_rev)

print(*line_rev, sep=" ")
