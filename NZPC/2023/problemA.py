number_Jellybeans = int(input())
number_people = int(input())
winner_guess = number_Jellybeans
if 50 <= number_Jellybeans <= 1000 and 1 <= number_people <= 250:
    for i in range(number_people):
        name = input()
        guess = int(input())
        gap = abs(guess - number_Jellybeans)
        if gap < winner_guess:
            winner = name
            winner_guess = gap
print(winner)

