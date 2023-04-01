"""
problemE:

Becs and Cas are best friends. Cas left school when she was 16 as she has total
fashion shopping skills, and became a manager at Supre. So, she and Becs get their
clothes from Supre - and in fact they have always bought exactly what the other has
(they are that shallow), but they would simply die if they wore the same thing on the
same day.
The two friends are so into copying each other that they have exactly the same outfits
in their wardrobes hanging in exactly the same order. However, sometimes one of
them just hates an outfit, so throws it out. (For the sake of friendship she doesn't tell
the other and if she's ever asked about it by text she pretends it is at the cleaners).
One difference between the girls is that Becs numbers her outfits from left to right, so
outfit 1 is the left most outfit, whereas Cas numbers them from right to left, so 1 is the
right most outfit. Their wardrobes look the same, though, so, for example, the left most
outfit in each wardrobe is the same.
Your task in this problem is to write a program that would alert Becs and Cas in
advance if they choose the same outfit for a particular day.

Input:

Input starts with two integers, n and d. n (5 < n <= 50) represents the number of outfits
in each girl's wardrobe before any are thrown out. d represents the number of days
to be considered.
The next 2 lines show outfits that have been removed from the girl's wardrobes. Each
line will contain a single integer, r (0 <= r <= n). A value of 0 means no outfit has been
removed. Any other value means the girl has removed that numbered outfit (according
to her numbering system) from her wardrobe. The first line will refer to Becs' wardrobe,
the second to Cas'.
There then follow d lines, each representing the outfits chosen by each girl on a
particular day, separated by a space with Becs' choice first. For example:
3 12
means that Becs chose outfit 3 counting from the left of her wardrobe, Cas chose outfit
12 counting from the right of her wardrobe.


Output:

Output consists of one line for each day. Each day will have a day number followed
by OK if the girls have chosen different outfits, ALERT if they have chosen the same
one.
"""

numbers = input().split(" ")
num_outfits = int(numbers[0])
num_days = int(numbers[1])
outfits_list = [i+1 for i in range(num_outfits)]
becs = outfits_list
cas = outfits_list[::-1]
results = []

if 5 < num_outfits <= 50:
    becs_remove = int(input())
    cas_remove = int(input())
    if 0 <= becs_remove <= num_outfits and 0 <= cas_remove <= num_outfits:
        if becs_remove > 0:
            becs.remove(becs[becs_remove-1])
        if cas_remove > 0:
            cas.remove(cas[cas_remove-1])
        for day in range(num_days):
            items = input().split(" ")
            becs_outfit = int(items[0])
            cas_outfit = int(items[1])
            if becs[becs_outfit - 1] == cas[cas_outfit - 1]:
                results.append("Day {0} ALERT".format(day+1))
            else:
                results.append("Day {0} OK".format(day+1))

[print(i) for i in results]





