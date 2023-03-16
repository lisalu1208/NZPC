"""
problem D:

In an attempt to get herself fit, a friend of mine has bought herself a pedometer. She
wears it when walking and it tells her how far she has walked.
The pedometer is sensitive to movement and is able to count steps reasonably accurately.
Before using it, users have to measure the length of a pace and enter it into the
pedometer, which can then use it to show how far has been walked. In this problem, you
have to do this calculation.

Input:

You will be given data for several pedometer users and asked to calculate how far each
has walked. The first line of input for a person is a single integer L (10 < L < 100) which
gives the stride length, in centimetres, of the person using the pedometer. This will be 0
for the last person whose data is not to be processed.
The next line for each user is a single integer N (1 <= N <=100) which is the number of
entries for this person. N lines then follow, each containing a single positive integer no
greater than 20,000. This is the number of steps the user has taken for the time period in
question.

Output:

For each user shown in the input, begin output with a single line of the format
User U
where U is the user number. Users are numbered from 1 in the order they appear in the
input. This is followed by N lines, one for each entry showing the number of steps, which
shows the appropriate distance walked in kilometers. This will be in the format
d.ddddd
ie at least one number before the decimal point and exactly 5 after it.
"""

stridelength = int(input())
userCount = 0
answerlist = []

while stridelength != 0:
    numEntries = int(input())
    userCount += 1
    answerlist.append(["User {0}".format(userCount)])
    if 10 < stridelength < 100 and 1 <= numEntries <= 100:
        for i in range(numEntries):
            steps = int(input())
            if 0 < steps <= 2e4:
                answerlist[userCount-1].append(format(stridelength / 1e5 * steps, '.5f'))
    stridelength = int(input())

for i in range(len(answerlist)):
    print(*answerlist[i], sep="\n")
