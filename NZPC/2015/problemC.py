"""
problem C:

Julia and Jeremy are twins who like to set each other challenges. Both have been learning
about number systems, and are aware that we normally use decimal (base 10) numbers,
probably because of the number of fingers we have.
The twins decided it would be fun to convert our numbers to number systems that other
creatures may use, creatures who have a different number of digits or other appendages. See
if you can rise to their challenge!

Input:

Each challenge consists of 3 lines. The first line is a description of a creature (not necessarily
real life). This will be no more than 20 characters in length. The final challenge begins with # -
this challenge is not to be processed.
The second line of a challenge is the number of digits or appendages the twins assume the
creature would use as a basis for its numbering system. This will be a number between 2 and
20 inclusive.
The final line is a decimal number which is to be converted into the assumed numbering system
of the creature. This will be a positive integer no greater than 5,000.

Output:

Each challenge requires a single line of output. It consists of the name of the creature, followed
by a comma and a space, followed by the decimal number, followed by another comma and
space, followed by the converted number. As is usual, where a base larger than 10 is used,
upper case letters of the alphabet (A to J, in alphabetical order) are used as extra digits.
"""

DIGITS = '0123456789ABCDEFGHIJ'


def convert_to_base(decimal_number, base):
    remainder_stack = []

    while decimal_number > 0:
        remainder = decimal_number % base
        remainder_stack.append(remainder)
        decimal_number = decimal_number // base

    new_digits = []
    while remainder_stack:
        new_digits.append(DIGITS[remainder_stack.pop()])

    return ''.join(new_digits)


description = input()
answerlist = []
while description != "#":
    answer = ""
    b = int(input())
    number = int(input())
    if len(description) <= 20 and 2 <= b <= 20 and 0 < number <= 5000:
        newNumber = convert_to_base(number, b)
        answer += description + " " + str(number) + " " + str(newNumber)
        answerlist.append(answer)
    description = input()

print(*answerlist, sep="\n")
