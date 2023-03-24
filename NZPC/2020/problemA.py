"""
problemA:

Jean and Joe are a rather untidy couple with a similar bogun taste in clothes. Their 2
children, Jane and James are also clothed in the style.
Jean’s mother came to stay and was horrified at the untidy state of the house. She
formed a pile of clothes for each of the 4 people in the house, but could only do so by
looking at the size of each item. Unfortunately sometimes the size had been cut off or
wasn’t readable, so these clothes she put in a separate pile.
If the size is ‘M’ or ‘L’, then it is Joe’s.
If the size is ‘S’ then it is James’.
If it is 12 or greater then it is Jean’s.
If it is smaller than 12 it is Jane’s.
Jean’s mother makes frequent visits and has to go through this process every visit.
Your task in this problem is to write a program that will assist her.

Input:

Input consists of data for a single visit by Jean's mother. The first line will consist of a
whole number, N (0 < N <= 50), which is the total number of clothes found strewn
round the house. Then follow N lines each representing the size of an item of clothing,
or an ‘X’ if the size label is missing or unreadable. The sizes will either be a 1 or 2-
digit number or a letter ‘S’, ‘M’ or ‘L’.

Output:

Output consists of one line which will contain five numbers, each separated by a space.
The numbers represent the number of clothes belonging to Joe, Jean, Jane and James
respectively in the current visit. The final number is the number of clothes unable to be
assigned to anyone. If there are no clothes in a pile, the number 0 must be shown.
"""

num_clothes = int(input())
result = 5 * [0]
if 0 < num_clothes <= 50:
    for i in range(num_clothes):
        size = input()
        if size.isupper() and (size == "M" or size == "L"):
            result[0] += 1
        elif size.isupper() and size == "S":
            result[3] += 1
        elif size.isnumeric() and int(size) >= 12:
            result[1] += 1
        elif size.isnumeric() and int(size) < 12:
            result[2] += 1
        elif size.isupper() and size == "X":
            result[4] += 1
print(*result, sep=" ")
