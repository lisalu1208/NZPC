"""
problem G:

Fizz, Buzz is a game for 2 or more players, often children who are learning maths. Each player
in turn has to take a number, starting at 1 and going up in 1s. If the number is a multiple of 3,
instead of the number they must say “Fizz”. If the number is a multiple of 5, instead of the
number they must say “Buzz”. If the number is a multiple of 3 and of 5, instead of the number
they must say “Fizz Buzz”. For all other cases, the person says the number. There will be an
agreed stopping point. A typical round would start like this:
1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz.
This problem is a variation of that game. You will be given a number of games each with a start
number and an end number, and two numbers whose multiples you are to replace by Fizz and
Buzz, like 3 and 5 in the above example. You are to display the correct output for each game.

Input:

The first line of input will contain a single integer, N (0 < N <= 20), which is the number of
games to play out. N lines then follow, each representing one game.
A game will be defined by 4 positive integers on a single line, F, L, N1 and N2. F is the first
number to be called in the game, L is the last number. 1 <= F <= L < 100. N1 and N2 are the
numbers whose multiples must be replaced. 1 < N1, N2 < 20.

Output:

For each game, the first line must be of the format Game n, where n is the game number. The
first game in the input list will be Game 1 with games numbered consecutively in the order they
are listed.
For each game, all numbers between F and L are to be displayed, each on a separate line. If a
number is a multiple of N1, it must be replaced by the word “Fizz”. If a number is a multiple of
N2, it must be replaced by the word “Buzz”. If a number is a multiple of N1 and N2, it must be
replaced by the words “Fizz Buzz”.
"""

numGame = int(input())
answerlist = []
count = 0
if 0 < numGame <= 20:
    for i in range(numGame):
        count += 1
        answerlist.append([count, []])
        line = input()
        first = int(line.split(' ')[0])
        last = int(line.split(' ')[1])
        num1 = int(line.split(' ')[2])
        num2 = int(line.split(' ')[3])
        if 1 <= first <= last <= 100 and 1 < num1 < 20 and 1 < num2 < 20:
            for num in range(first, last + 1):
                if num % num1 == 0 and num % num2 == 0:
                    answerlist[i][1].append("Fizz Buzz")
                elif num % num1 == 0:
                    answerlist[i][1].append("Fizz")
                elif num % num2 == 0:
                    answerlist[i][1].append("Buzz")
                else:
                    answerlist[i][1].append(str(num))

for g in range(len(answerlist)):
    print("Game {0}".format(answerlist[g][0]))
    for i in range(len(answerlist[g][1])):
        print(answerlist[g][1][i])
