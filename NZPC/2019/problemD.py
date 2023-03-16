"""
problem D:

Association Croquet is a game played between 2 teams either as singles or doubles.
Each team has 2 balls which they hit with their mallets. During a turn, the same ball
must be hit each time.

The aim is to score points by manoeuvring both balls on your
side through 6 hoops, once in each direction, then hitting the
centre peg. A point is scored each time a ball is hit through the
next hoop, and when the ball hits the centre peg. 26 points
wins the game.

A number of strokes are possible; they are represented by the following codes.
M Miss – a ball does not hit another ball, does not hit the centre peg, nor does it run
a hoop. This ends the player’s turn. Play continues with a player from the
opposing team.
R A roquet. A ball hits another ball; this gives the player another hit which must be
a croquet shot.
C A croquet shot. The player’s ball is placed in contact with the ball it roqueted and
played so that both balls move. The player then has a free hit.
H A hoop shot. The ball is hit through the next hoop in the correct direction. The
player scores a point and then has a free hit.
P A ball is pegged out by hitting it against the centre peg. This scores a point and
ends the player’s turn. The pegged out ball is removed from the game, and play
continues with a player from the opposing team.
This problem requires you to follow a series of strokes in a game and track the score.

Input:

The first 2 lines contain the names of the two teams who are playing the game
recorded, one per line. Names may contain spaces or punctuation but will not be
longer than 20 characters.
The next line contains the score at the start of the series of recorded strokes. It will
consist of 2 integers, both in the range 0 to 25 inclusive, separated by a space. The
first score will be for the first named team.
The fourth line will be a positive integer, N, being the number of characters in the final
line (0 < N <= 255).
The final line will consist of a series of N characters, each being one of the letters M,
R, C, H and P. These are codes for strokes as defined above. The first stroke is played
by the first named team. The sequence of strokes will not necessarily complete a
game, but will not take a team’s score beyond 26 points.

Output:

The score at the end of the sequence of strokes recorded in the format
team_1 x team_2 y
team_1 and team_2 are the names of the 2 teams in the order they were input.
x is the score of team_1 and y is the score of t team_2

"""