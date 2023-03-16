"""
problemH:

League football (known in some circles as soccer) has been played in England since
1888 and is the most popular winter game through most of Europe, just as rugby is in
New Zealand. English newspapers and many Websites publish the latest results and
the current tables.

With English football, each team plays every other team both home and away, and at
the end of the season, the team with most points wins the title. Points are awarded
for winning (3 points) or drawing (1 point each). Teams level on points are separated
by the larger goal difference, that is goals for (ie scored) minus goals against (ie
conceded). If this is level, the team who has scored more goals is placed first.

In this problem you will be given a list of teams and their current record, followed by a
list of matches. You have to update the record of each team who has a result recorded
and output a correctly sorted league table.

Input:

The first line contains a single integer, T (8 <= T <= 30), which is the number of teams
in the league. The next 2 x T lines each contain the current record of one team as
follows:
<name>
<games played> <wins> <draws> <losses> <goals for> <goals against> <points>
The first line contains the team name which consists of one or more words, which may
contain numbers. No name will be longer than 30 characters.

All numbers on the second line are non-negative integers.
The next line contains a single integer, G (0 < G <= (T/2)), which is the number of
games recorded. There then follow 4 x G lines, each containing data on one game as
follows:
<home team name>
<home team score>
<away team name>
<away team score>
The two teams will both be from the preceding list of teams. The scores will each be
a non-negative integer less than 20.

Output:
T lines giving the updated record of each team from the input, name followed by data
all on 1 line. Teams are to be sorted by highest points, then highest goal difference,
then most goals scored, then alphabetical order (case insensitive, numbers before
letters).
"""

teamList = []
recordList = []
overallList = []

# Get the number of the teams from the input
numTeam = int(input())

# FOR each value in the range of 2 * numTeam
#    Index:       0          1       2       3          4             5           6
# TeamList: <games played> <wins> <draws> <losses> <goals for> <goals against> <points>
for i in range(numTeam):
    name = input()
    if len(name) <= 30:
        record = [int(r) for r in input().split(' ')]
        teamList.append(name)
        recordList.append(record)

# Get the number of games from the input
numGames = int(input())

# FOR each value in the range of 4 * numGames
for i in range(numGames):
    homeTeamName = input()
    homeTeamScore = int(input())
    awayTeamName = input()
    awayTeamScore = int(input())
    homeTeamIndex = teamList.index(homeTeamName)
    awayTeamIndex = teamList.index(awayTeamName)
    recordList[homeTeamIndex][0] += 1
    recordList[awayTeamIndex][0] += 1
    recordList[homeTeamIndex][4] += homeTeamScore
    recordList[homeTeamIndex][5] += awayTeamScore
    recordList[awayTeamIndex][4] += awayTeamScore
    recordList[awayTeamIndex][5] += homeTeamScore
    if homeTeamScore > awayTeamScore:
        recordList[homeTeamIndex][1] += 1
        recordList[homeTeamIndex][6] += 3
        recordList[awayTeamIndex][3] += 1
    elif homeTeamScore == awayTeamScore:
        recordList[homeTeamIndex][2] += 1
        recordList[awayTeamIndex][2] += 1
        recordList[homeTeamIndex][6] += 1
        recordList[awayTeamIndex][6] += 1
    else:
        recordList[homeTeamIndex][3] += 1
        recordList[awayTeamIndex][1] += 1
        recordList[awayTeamIndex][6] += 3
    overallList = list(zip(teamList, recordList))
    overallList.sort(key=lambda x: x[1][6], reverse=True)
    print(str(overallList))
    print(len(overallList))

#
#
for i in range(len(teamList)):
    print(teamList[i] + " " + ' ' .join(list(map(str, recordList[i]))))

