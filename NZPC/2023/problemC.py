"""
problem C:

In a small town in New Zealand, a lot of strange graffiti has been appearing. The local
authorities have employed a graffiti expert who has determined that the graffiti follows
3 rules:
1. There are 3 distinct images which we will represent
with the characters #, & and %.
2. A first image is selected and it is drawn once or twice.
3. One or more times, an image is chosen which is
different from the last one used and, one or more
times, drawn once to the left and once to the right of the previous image(s).
Lately, several copycat graffiti artists have been at work, but they are not following the
established rules.
Your job is to analyse graffiti examples from around the town and tell the local authority
if they are genuine or copycat.

Input:

Input consists of a number of lines of graffiti. The first line is a positive integer, N (0<
N<=15) which tells how many lines of graffiti follow.
The next N lines each contain at least 1 but no more than 20 characters (each being
#, & or %), each line representing one piece of graffiti.

Output:

For each line of input, output a one word verdict. If the graffiti example follows the
rules, the output should be the word genuine. Otherwise the output should be the
word copycat.
"""

result = []
num_lines = int(input())
if 0 < num_lines <= 15:
    for i in range(num_lines):
        break
        