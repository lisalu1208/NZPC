"""
problemB:

Today it is 11th September. If you were born before 11th
September (in whatever year you were born) then you have
already had your 2021 birthday. If you were born after 11th
September, you have not yet had your 2021 birthday. If you
were born on 11th September – happy birthday! If you were
born on 29th February – unlucky, you do not have a birthday
this year, as 2021 is not a leap year!

Input:
Input will consist of a number of lines containing dates. All dates will be valid and no
date will be repeated, so there will be no more than 366 lines. The format for a line
will be one or two digits, a space, and the full name of a month. The name will begin
with an upper case letter, and the other letters will be lower case. Input will be
terminated by a line containing just 0 #. This line should not be processed.

Output:

Output will consist of a single line of text for each line of input:
"You have had your birthday." if a person born on that date would have already
had their birthday in 2021,
"Your birthday is still to come." if they would not,
"Happy birthday!" if the date is 11
th September and
"Sorry, leapling, no birthday this year." if the date is 29th February. 
"""

results = []
line = input()

while line != "0 #":
    day = int(line.split(" ")[0])
    month = line.split(" ")[1]
    if month == "October" or month == "November" or month == "December" or (month == "September" and day > 11):
        results.append("Your birthday is still to come.")
    elif month == "September" and day == 11:
        results.append("Happy birthday!")
    elif month == "February" and day == 29:
        results.append("Sorry, leapling, no birthday this year.")
    else:
        results.append("You have had your birthday.")
    line = input()

[print(i) for i in results]
