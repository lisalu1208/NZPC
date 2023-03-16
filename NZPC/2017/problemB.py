"""
Problem B:
In golf croquet doubles, two teams of 2 play each other. Each player has their own ball which they hit when it is their
turn. A turn comprises one hit of the ball.

There are 6 hoops which are each played twice, once in each direction, in a prescribed order. A point is scored by the
first team to make the current hoop. To make a hoop, one of the team's balls must be knocked through the current hoop
in the right direction. The first team to score 7 points wins. If the game reaches 6-6, a final deciding hoop is played.
Note that a team cannot score more than 7 points, the game ends as soon as the 7th hoop is won.

The balls are played in a fixed order: blue, red, black (blue's partner) then yellow (red's partner). We can record the
progress of a match by recording the outcome of each shot. The code we are using is:

S: a standard shot that does not make a hoop
H: a shot that makes a hoop for the team who played the shot
D: a shot that makes 2 hoops for the team who played the shot -- an extremely unlikely scenario but it can happen!
A team on 6 points will only score the first of the two hoops, of course.
O: a shot that makes a hoop for an opponent's ball!

The last one is almost certainly an accident, but it happens far more times than players like!

Input:
The input represents part or all of a single game of golf croquet. The first two lines each contain the name of a team,
each consisting of one or more words. The name will be no more than 30 characters long. The first named team play blue
and black. The third line is a single integer, S, which tells how many strokes are recorded, for a game that has started
but which may not yet be completed. (0 < S <= 255)

The fourth line contains S upper case letter characters, each being one of the 4 characters defined above (S, H, D OR O).
Blue always plays the first shot followed in turn by red, black, and yellow.

Output:
Output a single line of text with the current score in the form
team1name x team2name y
Follow this by a space then one of:
teamname has won.
teamname is winning.
All square.
"""

# Get the names of two teams
team1name = input()
team2name = input()

# Get the number of strokes
numStrokes = int(input())

strokes = input()

team1score = 0
team2score = 0

answer = ""

for i in range(numStrokes):
    if strokes[i] == 'S':
        continue
    elif strokes[i] == 'H':
        if i % 4 == 0 or i % 4 == 2:
            team1score += 1
        else:
            team2score += 1
    elif strokes[i] == 'D':
        if i % 4 == 0 or i % 4 == 2:
            team1score += 2
        else:
            team2score += 2
    elif strokes[i] == 'O':
        if i % 4 == 0 or i % 4 == 2:
            team2score += 1
        else:
            team1score += 1

answer += team1name + " " + str(team1score) + " " + team2name + " " + str(team2score) + ". "

if team1score < 7 and team2score < 7:
    if team1score < team2score:
        answer += team2name + " is winning."
    elif team1score > team2score:
        answer += team1name + " is winning."
    else:
        answer += ". All square."

elif team1score >= 7:
    answer += team1name + " has won."

elif team2score >= 7:
    answer += team2name + " has won."

print(answer)



