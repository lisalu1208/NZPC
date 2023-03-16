"""
problem C:

How many 1s are there in the numbers between 10 and 15 inclusive?
10 11 12 13 14 15
You will see that there are 7. In this problem you will be asked to perform similar counts.

Input:

Input begins with a line containing a single integer, N (0< N <= 100), which is the number of
counts you have to make. Each count is represented by a separate line containing 3 integers, S
F C, separated by single spaces. S (-1000 <= S < 1000) is the start number, F is the finish
number (S < F <= 1000) while C is the digit to count (a single digit).

Output:

For each count line in the input, produce one line of output. The output should be the number of
times the required digit occurs in the specified number range (inclusive).
"""

numCounts = int(input())
answerlist = []
if 0 < numCounts <= 100:
    for i in range(numCounts):
        count = 0
        line = input()
        startNum = line.split(' ')[0]
        finishNum = line.split(' ')[1]
        digit = line.split(' ')[2]
        if -1000 <= int(startNum) < 1000 and int(startNum) < int(finishNum) <= 1000 and digit.isdigit():
            for j in range(int(startNum), int(finishNum) + 1):
                for d in range(len(str(j))):
                    if str(j)[d] == digit:
                        count += 1
        answerlist.append(count)

print(*answerlist, sep="\n")