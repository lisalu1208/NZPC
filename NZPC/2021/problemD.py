"""
problemD:

Our local car park needs your help. They have a fixed number of spaces
for parking and want to be able to tell drivers who are approaching the
park just how many spaces are available to use. They also need to stop
the entry barrier from opening if the park is full. If your system works, they
will sell it to other car park owners.

Input:

Input consits of a single scenario representing a single car park. The first line consists of two
integers, S and C (10 <= S <= 500, 0 <= C <= S). S is the number of spaces in the car park
overall, and C is the number of cars currently parked there. 

The second line consists of a string of from 0 to 255 characters, each character being one of
the upper case letters ‘I’ or ‘O’. This string represents a stream of data from the entry and exit
barriers. I means that a car has attempted to come in to the car park, O that a car has driven
out. If the car park is not full, a car attempting to enter will be allowed in and counted. If all the
spaces in the car park are filled with cars, a car attempting to enter will be refused entry and not
counted. (Such a car may try again later).

If there are no cars in the car park, an ‘O’ in the data stream at that point represents an error,
and processing of that scenario should stop.

Output:

Output consists of a single line. If there has been an error in the data stream, it will contain just
the word “Error.”. Otherwise, it will show the number of cars in the car park at the end of the
scenario in the format “X cars.” The line ends with a full stop.
"""

line1 = input()
S = int(line1.split(" ")[0])
C = int(line1.split(" ")[1])

if 10 <= S <= 500 and 0 <= C <= S:
    line2 = input()
    if 0 <= len(line2) <= 255:
        for i in line2:
            if i == "I" and C != S:
                C += 1
            elif i == "O" and C > 0:
                C -= 1
            else:
                print("Error.")
                quit()

print("{0} cars".format(C))

