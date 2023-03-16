"""
problem B:

Wikipedia tells us that “In mathematics, a geometric progression, also known as a geometric
sequence, is a sequence of numbers where each term after the first is found by multiplying the
previous one by a fixed, non-zero number called the common ratio.” So
1 6 36 216
is a geometric progression with a common ratio of 6. As you can see
1 x 6 = 6
6 x 6 = 36
36 x 6 = 216
In this problem you will be given sets of numbers and, if the numbers in a set form a geometric
progression, you are to give the common ratio.

Input:

Input begins with a line containing a single integer, N (0< N <= 100), which is the number of sets
of numbers for you to evaluate. This is followed by N lines, each line being a set of numbers.
There will be at least 3 but no more than 20 numbers on a line. If there is a common ratio, its
value will be between +1 and +20 or between -1 and -20, both inclusive.

Output:

For each line of input, produce one line of output. If the input line is a geometric progression,
the output line should be the word “yes” followed by a space, followed by the common ratio. If
the input line is not a geometric progression, the output line should be the word “no”.
"""


numSets = int(input())
answerlist = []
if 0 < numSets <= 100:
    for i in range(numSets):
        isRatio = True
        line = input()
        if 3 <= len(line.split(' ')) <= 20:
            numlist = [int(x) for x in line.split(' ')]
            ratio = int(numlist[1] / numlist[0])
            for j in range(len(numlist) - 1, 2, -1):
                if numlist[j] / numlist[j - 1] != ratio:
                    isRatio = False
                    break
            if isRatio:
                answerlist.append("yes {0}".format(ratio))
            else:
                answerlist.append("no")

print(*answerlist, sep="\n")
