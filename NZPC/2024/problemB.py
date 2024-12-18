"""
problem B:

According to Wikipedia, “Monopoly is a multi-player economicsthemed board game”. It goes on to say: “In the game, players
roll two dice to move around the game board, buying and trading
properties and developing them with houses and hotels. Players
collect rent from their opponents, aiming to drive them into
bankruptcy.”
There is a jail on the board where players may find themselves sent for a number of
reasons, most obviously for landing on the “Go to Jail” square. There are also 2 packs
of cards which players have to obey when they land on appropriate squares. Both
packs contain a “Go to Jail” card, but also a “Get out of jail free” card. A player may
keep a “Get out of jail free” card until it is needed.
This problem assumes a player is in jail, and has to get out. There are 3 ways:
1. Throw doubles, that is where both dice show the same number.
2. After 3 turns use a “Get out of jail free” card.
3. After 3 turns, pay a $50 fine.
This problem assumes that the player will wait until they have played 3 turns before
using their card or paying the fine.
Once out, the player moves forward the number of squares indicated by adding the
dice from the last turn.

Input:

The first line of input will be the dice scores for the first throw, on a single line and
separated by a space.
If doubles are not thrown, a second similar line will appear, and similarly a third line if
doubles are still not thrown.
If all 3 lines do not show doubles, a fourth line of input will show if the player has a
“Get out of jail free” card (lower case y or n).

Output:

Output will consist of a single line with the following format:
<Reason>. Move forwards n squares.
<Reason> is one of
Doubles Use card $50 fine
n is the sum of the last 2 dice thrown.

"""

firstNumber = 0
secondNumber = 0
i = 0
for i in range(3):
    line = input()
    firstNumber = int(line.split(' ')[0])
    secondNumber = int(line.split(' ')[1])
    if firstNumber == secondNumber:
        print("Doubles. Move forwards {0} squares".format(firstNumber+secondNumber))
        exit()
line = input()
if line == "y":
    print("Use card. Move forwards {0} squares".format(firstNumber+secondNumber))
elif line == "n":
    print("$50 fine. Move forwards {0} squares".format(firstNumber+secondNumber))

