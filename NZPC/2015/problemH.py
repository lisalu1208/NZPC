"""
problem H:

PC^2 (pea sea squared) has been used to manage programming contests for many years. It
was written to manage the ACM contest where each problem solved scores 1 point, and time is
the tie breaker. To use it in the NZPC, or any other contest where questions have a variable
points weighting, a program needs to be written to read a PC^2 file and apply different rules.
That is what you have to do in this problem. You will be given a number of contests to manage.
For each you will be given the points each problem is worth, and a PC^2 entry for each team.
You have to rank the teams according to the rules of the contest in which they are competing.

Input:

Input consists of a number of contests. The first line for each contest contains a single integer,
P, which is the number of problems in the contest. (0 < P <= 20). Where P is 0, that marks the
end of input.
The second line consists of a series of positive integers, one per problem, separated by spaces.
This represents the number of points for each problem, the first number for the first problem and
so on.
The third line for each contest contains a single integer, T, which is the number of teams taking
part in the contest. (0 < T <= 50).
There then follow T lines, each line being data for one team. The data starts with the team
name. This may contain spaces, but is terminated by a comma (with no commas in the name).
There then follow one record for each problem, the records being separated by commas. The
records are in the same order as were the points values in line 2, problem 1 first and so on.
Each record has an integer, a slash character, /, and either another integer, or a – character.
The record should be interpreted as follows:
1. The first integer shows how many submissions the team made for the problem. It will be 0 or
more.
2. If the slash is followed by a -, it means that the team did not solve the problem, so score no
points for it.
3. If the slash is followed by a number, which will be zero or more, it means that the team did
solve the problem. The number shows how many minutes into the contest the successful
submission was made.

Output:

For each contest, output starts with a line containing the text Contest N, where N is the number
of the contest. The first contest in the input is 1, and contests are numbered in order.There then follows a line for
each team in the contest showing rank, team name and points
scored, separated by spaces. The teams must appear in ascending rank order (ie 1, 2, 3..).

In these contests teams are sorted by points scored, the higher the better. Teams with equal
points are considered equal and should be displayed in alphabetical order of name (not case
sensitive), but should have equal rank. Make sure any following team has its correct rank (for
example after joint first, the next team is rank 3).
"""

numProblems = int(input())
pointsList = [int(p) for p in input().split(' ')]
answerList = []
count = 0
while numProblems != 0:
    teamList = []
    numTeams = int(input())
    for team in range(numTeams):
        line = input()
        teamName = line.split(',')[0]
        score = 0
        for j in range(1, len(line.split(','))):
            numSubmission = int(line.split(',')[j].split('/')[0])
            if line.split(',')[j].split('/')[1].isnumeric():
                score += pointsList[j-1]
        teamList.append([teamName, score])
    numProblems = int(input())
    sortedList = sorted(teamList, key=lambda x: x[1], reverse=True)
    count += 1
    answerList.append([count, sortedList])

for i in range(len(answerList)):
    print("Constest {0}".format(answerList[i][0]))
    for j in range(len(answerList[i][1])):
        # print(str(answerList[i][1][j][0]))
        print("{0} {1} {2}".format(j+1, answerList[i][1][j][0], answerList[i][1][j][1]))



