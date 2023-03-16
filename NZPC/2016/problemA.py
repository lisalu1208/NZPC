"""
Problem A:

The Bloggs family keep getting invited to birthday parties, and they feel they
must buy the person who invites them a present. The trouble is they do not
have much money!
The family has come up with a strategy. Whenever they go to a shop to buy a
present, they will not buy the cheapest present (that would seem mean!), so
they buy the second cheapest gift they can find. Your task here is to help
them quickly find the second least expensive gift in the shop.

Input:

Input will consist of a single scenario which contains a list of prices from a
shop, each on a separate line. The first line will contain N, the number of
prices (2 <= N <= 100). No price will be duplicated. The next N lines will
each contain a single price in the form of a decimal number with 2 places of
decimals (ie dollars and cents).

Output:

Output the second lowest price on a line by itself. It must be in the same
format as with the input.
"""

pricelist = []
# Get the number of prices from the input
numPrices = int(input())
if 2 <= numPrices <= 100:
    for i in range(numPrices):
        price = float(input())
        pricelist.append(price)

# Sort the list from lowest to highest
pricelist.sort()
# print out the second item which is the second smallest value
print("{:.2f}".format(pricelist[1]))
