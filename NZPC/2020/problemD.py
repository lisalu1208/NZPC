"""
problemD:

As the manufacturer of holders for door numbers, you have to know how wide to make
them based on the house number each of your customers supplies. Fortunately, all
house numbers in your area use exactly the same style of digit, so the calculation is
quite easy. Most digits are exactly 3 cm wide, but a 0 is 4 cm wide and a 1 is only 2
cm wide, so that adds a slight complication. Also, you have to remember to leave a 1
cm gap between digits, and a 1 cm border at the start and end of the number.
As you can see from the diagram, a customer who lives at number 120 will need a 13
cm wide holder – 4 cm for the border and gaps, 2 cm for the 1, 3 cm for the 2 and 4
cm for the 0. 4 + 2 + 3 + 4 = 13.

Input:

Input for this problem is a series of street numbers (integers between 1 and 9999
inclusive) each on a line of its own. The last number will be 0 which should not be
processed.

Output:

For each input line, output a single integer, the width in cm of the required holder for
that street number.
"""

number = input()
result = []
while number != "0":
    length = 0
    if 1 <= int(number) <= 9999:
        for n in number:
            if n == "1":
                length += 2
            elif n == "0":
                length += 4
            else:
                length += 3
    # Add the gap
    length += len(number) + 1
    result.append(length)
    number = input()

[print(r) for r in result]
