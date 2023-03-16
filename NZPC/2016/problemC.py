"""
problem C:

The Olympic Games in Rio cannot have escaped your attention! 2016 is a
summer Olympics year.

The modern summer Olympic Games were first held in 1896, and have been
held at 4 yearly intervals since then, except during the two world wars (1914
to 1918 and 1939 to 1945). The next games are scheduled to be held in
Tokyo in 4 years time.

Input:

Input will consist of a list of years, one per line, in the range 1860 to 2030
inclusive. The final year will be 0 – do not process that year.

Output:

Output is one line per year. The year is given followed by:
Summer Olympics if the summer Olympic Games were held, or are scheduled to be held in that year.
Games cancelled if the summer games should have been held but there was a war.
No city yet chosen if it is a future summer Olympic year but no city has yet been awarded the games
No summer games otherwise.
"""

answerList = []
year = int(input())
while year != 0:
    if 1816 <= year <= 2030:
        if year % 4 == 0:
            if 1914 <= year <= 1918 or 1939 <= year <= 1945:
                answerList.append(str(year) + " Games cancelled")
            elif year <= 2020:
                answerList.append(str(year) + " Summer Olympics")
            elif year > 2020:
                answerList.append(str(year) + " No city yet chosen")
        else:
            answerList.append(str(year) + " No summer games")
    year = int(input())

print(*answerList, sep="\n")
