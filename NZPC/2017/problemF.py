"""
Musical chairs is a game frequently played at children s parties. Players are seated in
a circle facing outwards. When the music starts, the players have to stand up and
move clockwise round the chairs. One chair is removed, and when the music stops
the players all have to try to sit down on one of the chairs. The player who does not
manage to sit down is out, and the game continues until there is just one player left,
who is the winner.

Input:
The first line contains a single integer, N which is the number of players (1 < N <= 15).
The next N lines have the names of the players.

The next line contains R, an integer which tells how many rounds are to be processed
(0 < R < N). The next R lines each contain a pair of integers S and M, separated by a
space. S is the number of the seat to be removed. Seats are numbered from 1 to the
number of seats remaining in a clockwise direction.

M is the number of moves made before the music stops (0 < M <= 30). A move takes
a player from one seat to the next in a clockwise direction. A move from the highest
seat number takes a player to seat 1.

Output:
After each round has taken place, output a line
<name> has been eliminated.
where <name> is the name of the person who does not find a seat. This will be the
person who would have ended up at the seat which was removed.
At the end of the specified number of moves, output a line which either says
<name> has won.
where a single player remains, or
Players left are <name list>.
where the game is not yet finished.
<name list> contains the name of each player not yet eliminated in the same order
as in the input. The names are separated by spaces.
"""

numPlayers = int(input())
namesList = []
pairsList = []

if 1 < numPlayers <= 15:
    for i in range(numPlayers):
        name = input()
        namesList.append(name)

afterMove = namesList.copy()

numRounds = int(input())
if 0 < numRounds < numPlayers:
    for i in range(numRounds):
        pair = input()
        pairsList.append([int(num) for num in pair.split(' ')])

for r in range(numRounds):
    print(str(afterMove))
    for move in range(pairsList[r][1]):
        temp = afterMove[-1]
        for n in reversed(range(len(namesList) - 1)):
            afterMove[n + 1] = afterMove[n]
        afterMove[0] = temp
    print(afterMove[pairsList[r][0] - 1] + " has been eliminated.")
    namesList.remove(afterMove[pairsList[r][0] - 1])
    afterMove.remove(afterMove[pairsList[r][0] - 1])

if len(namesList) == 1:
    print(namesList[0] + " has won.")
else:
    print("Players left are " + ' '.join(namesList) + ".")
