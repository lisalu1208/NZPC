"""
problem B:

Mike wrote some text on a piece of paper and now he wants to know how many
holes are in the text.

What is a hole in this context?

If you think of the paper as the plane and a letter as a curve on the plane, then each
letter divides the plane into regions. For example letters "A" and "O" divide the plane
into two regions so we say these letters each have one hole. Similarly, letter "B" has
two holes and letters such as "C", "E", "F" and "K" have no holes. Spaces, of course,
have no holes.

We say that the number of holes in the text is equal to the total number of holes in
the letters of the text. Help Mike to determine how many holes are in the text.

Input:

Input starts with an integer, N, on a line of its own (0 < N <= 30). It tells you how
many lines of text follow. There then follow N lines of text. Each line contains a
string of text composed only of upper case letters and spaces; it will contain at least 1
letter. The length of the text is no more than 250 characters.

Output:

For each line of input, output a single line containing the number of holes in the
corresponding text.

26 LETTERS:
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

ONE HOLE: A D O P Q R

TWO HOLES: B
"""

OneHoleList = ['A', 'D', 'O', 'P', 'Q', 'R']
# Get number of lines
numLines = int(input())
countList = []

for i in range(numLines):
    line = input().upper()
    count = 0
    for ch in line:
        if ch.isalpha():
            if ch in OneHoleList:
                count += 1
            elif ch == 'B':
                count += 2
    countList.append(count)

print(*countList, sep="\n")
