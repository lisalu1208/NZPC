"""
Problem H:

A group of journalists decided it would be quite fun to rank the performance of
MPs in parliament each week, and have asked you to write a program to help
them.
The journalists were convinced that most MPs did not do very much at all, but
came up with a list of codes that would identify actions taken by MPs which
they considered noteworthy. They associated points with each action, some
positive and some negative. The current table of actions and points follows.
If your program is a success and the scheme catches on, more will be added
later.

Code               Action                                           Points
S    Made a speech lasting at least 5 minutes                       +10
Q    Asked a question during Question Time                          +5
A    Answered a question during Question Time                       +7
L    Spent less than an hour in the chamber                         -8
F    Made a funny remark that caused laughter in the chamber        +4
D    Made a derisory comment about another party                    -5
E    Was asked to leave the chamber                                 -10

Input:

Input will contain data for one week. It will start with a line containing a
positive integer N (0 < N <= 120), the number of MPs who attended the
debating chamber of parliament in the week in question. There then follow N
lines, each giving data on 1 MP. Data will be a unique identifying number, I (0
< I <= 120) followed by a space, followed by the name of the MP.

The list of MPs will be followed by a positive integer, A (0 < A <200), the
number of action entries that complete the data. Each of the A lines following
will contain data on 1 recorded action of an MP. It will consist of the MP’s
unique identifying number, followed by a space, followed by one of the letter
codes from the table above. The points for each MP have to be added to give
their points score for the week.

Output:

Output the points score and name of the best scoring MP, and the points
score and name of the worst scoring MP each on a separate line. In the case
of equal scores, list on the same line all MPs with those scores in order of
their unique identifying number, and separated by a space.
"""


def printanswer(indexList):
    answer = ""
    for i in range(len(indexList)):
        index = indexList[i][0]
        answer += " " + scoreList[index][1] + " " + scoreList[index][2]
    return answer


codelist = [('S', +10), ('Q', +5), ('A', +7), ('L', -8), ('F', +4), ('D', -5), ('E', -10)]
scoreList = []

numMPs = int(input())
score = 0
if 0 < numMPs <= 120:
    for i in range(numMPs):
        line = input()
        idNum = int(line.split(' ')[0])
        firstname = line.split(' ')[1]
        lastname = line.split(' ')[2]
        scoreList.append([idNum, firstname, lastname, score])

numAction = int(input())
if 0 < numAction < 200:
    for j in range(numAction):
        line = input()
        id = int(line.split(' ')[0])
        action = line.split(' ')[1]
        index = [y[0] for y in codelist].index(action)
        indexScoreList = [y[0] for y in scoreList].index(id)
        scoreList[indexScoreList][3] += codelist[index][1]

maxItem = max([sublist[-1] for sublist in scoreList])
maxIndex = [(ind, scoreList[ind].index(maxItem)) for ind in range(len(scoreList)) if maxItem in scoreList[ind]]

minItem = min([sublist[-1] for sublist in scoreList])
minIndex = [(ind, scoreList[ind].index(minItem)) for ind in range(len(scoreList)) if minItem in scoreList[ind]]

print(str(maxItem) + printanswer(maxIndex))
print(str(minItem) + printanswer(minIndex))
