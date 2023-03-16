"""
problem F:

An alpha puzzle is a type of crossword puzzle where each letter square (ie one that is not black)
contains a number to represent a letter. Throughout the puzzle, a particular letter is always
represented by the same number. All letters of the alphabet are used, so numbers range from 1
to 26.
In this problem you will be given a prepared alpha puzzle and must check it to see that all 26
letters have been used at least once each, making it a valid puzzle. Valid puzzles go to the next
stage of preparation, invalid ones go back to the designer.

Input:

You will be presented with a number of puzzles to validate. Each puzzle starts with a single
integer, S, on a line by itself (10 <= S <=20). S is the size of the puzzle – the number of rows
and columns of squares that it contains. If S is 0 it marks the end of input – do not process that
puzzle.
There then follow S lines each containing S integers separated by spaces. Integers will be in
the range 0 to 26, with 0 representing black squares (ie squares which do not contain letters),
while the other integers each represent a letter of the alphabet.

Output:

Output one line for each puzzle presented. If the puzzle contains all 26 letters at least once, the
output should be “Ready to go”. Otherwise, the output should be “Back to the designer"
"""


numPuzzles = int(input())
answerlist = []
while numPuzzles != 0:
    alphalist = [i for i in range(1, 27)]
    if 10 <= numPuzzles <= 20:
        for n in range(numPuzzles):
            puzzleList = [int(i) for i in input().split(' ')]
            for l in range(len(puzzleList)):
                if puzzleList[l] != 0 and alphalist.count(puzzleList[l]) != 0:
                    alphalist.remove(puzzleList[l])

    if len(alphalist) != 0:
        answerlist.append("Back to the designer")
    else:
        answerlist.append("Ready to go")
    numPuzzles = int(input())

print(*answerlist, sep="\n")



