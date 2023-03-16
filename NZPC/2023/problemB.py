"""
problem B:

Bridge is a popular card game played all round the world. A game uses a standard
pack of 52 playing cards. Two pairs of players compete to score the most points.
North (N) and South (S) play East (E) and West (W). One player
deals the cards one at a time so that each player holds 13 cards.
The first card is dealt to the player to the left of the dealer, the last
to the dealer. During play there are 13 rounds (or tricks) – the best
card in each trick winning the trick.
Before playing the cards, players have to bid how many tricks they will win. There are
many bidding systems that may be used; several of these evaluate a hand by
assigning points to the best cards. In the system we are going to use in this problem,
each ace (A) scores 4 points, each king (K) scores 3 points, each queen (Q) scores 2
points and each jack (J) scores 1 point. Your job is to assign the correct cards to each
player in a deal, and evaluate their hands using the specified points system

Input:

Input consists of two lines.
On line 1 is a single letter (N, S, E or W) showing which player is dealing.
On line 2 are 52 characters showing the order of the cards in the pack. Apart from A,
K, Q and J, t represents a 10, and numbers 2 to 9 represent cards with those numbers.
There are 4 of each valued card in the pack. Suits are ignored

Output:

Output consists of a single line showing the points value of the cards held by the 4
players, separated by spaces. The dealer will be first with their points, the other
players following in clockwise order. As a check, note that the total points must be 40
"""


def nextPlayer(player_index):
    index = player_index + 1
    if index >= 4:
        index = 0
    return index

def printResult(players, points, dealer_index):
    index = dealer_index
    for i in players:
        print(players[index] + " " + str(points[index]))
        index = nextPlayer(index)


player_deal = input()
card_order = input()

players = ["N", "E", "S", "W"]

dealer = players.index(player_deal)
index_player = nextPlayer(dealer)
points_list = 4*[0]
for card in card_order:
    if card == "A":
        points_list[index_player] += 4
    elif card == "K":
        points_list[index_player] += 3
    elif card == "Q":
        points_list[index_player] += 2
    elif card == "J":
        points_list[index_player] += 1
    index_player = nextPlayer(index_player)

printResult(players, points_list, dealer)
