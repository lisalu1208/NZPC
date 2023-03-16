"""
problem A:

The Western Suburbs Croquet Club has 2 categories of membership, Senior and Open. They
would like your help with an application form that will tell prospective members into which
category they will be placed.
To be a senior, a member must be at least 55 years old, and must have a handicap no lower
than 8. In this croquet club, handicaps range from -2 up to +26; the better the player, the lower
the handicap. In a match, the difference in handicaps is used to determine how many bisques
(free shots) the weaker player will receive. A player with no existing handicap will be given a
handicap of 26.

Input:

Input begins with a line containing a single integer, N (0< N <= 50), which is the number of
potential new members for you to classify. This is followed by N lines, each line being data for
one member. The data will consist of two integers, A and H, separated by a space. A, the
person’s age, will be a positive integer, H a valid handicap.

Output:

For each line of input, produce one line of output. The output should be the category in which
the prospective member would be placed, Senior or Open.
"""

numMembers = int(input())
answerList = []
if 0 < numMembers <= 50:
    for i in range(numMembers):
        line = input()
        age = int(line.split(' ')[0])
        handicap = int(line.split(' ')[1])
        if age >= 50 and handicap >= 8:
            answerList.append("Senior")
        else:
            answerList.append("Open")

print(*answerList, sep="\n")
