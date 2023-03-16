"""
problem A:

The manager of a car park has asked for your help with an occupancy survey. He
wants to know how many spaces in the car park are occupied on consecutive days.

Input:

The first line in the input will be a single positive integer, N (0<N<=250), which is the
number of parking spaces available.
The second line contains data for the first day. It consists of N characters, O for an
occupied space, with - for an empty space.
The third line contains similar data for the second day.

Output:
Output consists of a single integer, the number of parking spaces that were occupied
on both days.
"""

numParking = int(input())
count = 0
if 0 < numParking <= 250:
    first = input()
    second = input()
    for i in range(numParking):
        if first[i] == "O" and second[i] == "O":
            count += 1

print(count)
