"""
Problem A:

Part of an exercise at the Whangerei School for Young Ladies involves girls standing in a line. Their position in a
line is given by a number; 1 means the first girl, 3 the third girl etc. The exercise involves girls swapping places
and the participants having to remember the new order. You are to write a program which accepts as input pairs of
numbers which mean you should swap the positions of the girls at those two positions. The program will then report
the new line positions which the participants are trying to remember.

Input:

Input will consist of the first names of the girls in the line from first to last at the start of
the exercise. Names will be unique, and will be as defined in the preamble. The names
will be entered on one line, each name separated by a space. There will be at least 2
names and a maximum of 26 names.
The number of pairs (swaps) will be n (a non-negative integer no greater than 1000)
on the second line. There will follow n lines of pairs of numbers which will be separated
by a single space. The two numbers in a pair will always be different to each other
and will both represent the position of a girl in the line. These are the girls who must
swap places.

Output:

Output should be of the names of the girls in their new order in the line

"""


# Read in the name list
nameList = input().split(' ')
numberOfSwap = int(input())
i = 0
if 0 < numberOfSwap <= 1000:
    for i in range(numberOfSwap):
        readIn = input()
        firstNumber = int(readIn.split(' ')[0]) - 1
        secondNumber = int(readIn.split(' ')[1]) - 1
        name = nameList[firstNumber]
        nameList[firstNumber] = nameList[secondNumber]
        nameList[secondNumber] = name
print(*nameList, sep=' ')
