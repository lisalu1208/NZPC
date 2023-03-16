"""
problem A:

When I was at school, we were always very competitive; who can run fastest? Who gets best
marks in tests? This problem gets you to help with one such challenge – who is tallest?

Input:

Input consists of a number of groups of people. The first line for each group contains a single
integer, N, which is the number of people in the group. (0 < N <= 50). If N is 0, this marks the
end of input.

N lines then follow, each containing data on one person, a single name followed by a height in
metres which has 2 decimal places.

Output:

For each group of people, output a single line containing the name of the tallest person. Where
two or more people in a group have the same height, list each of them on the same line,
separated by spaces, in the order they appear in the input.
"""


numPeople = int(input())
answerList = []
while numPeople != 0:
    heightlist = []
    namelist = []
    if 0 < numPeople <= 50:
        for n in range(numPeople):
            line = input()
            name = line.split(' ')[0]
            height = float(line.split(' ')[1])
            namelist.append(name)
            heightlist.append(height)
        highestIndex = heightlist.index(max(heightlist))
        answerList.append(namelist[highestIndex])

    numPeople = int(input())

print(*answerList, sep="\n")
