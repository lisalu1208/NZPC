"""
problem G:

Mr Farkle was brought up on a farm and spent quite a bit of time in his youth
hunting rabbits! He now teaches maths and computing, and came up with a
hunting game to help his students learn about the binary search.

He put 50 envelopes at the front of the room, numbered sequentially from 1 to
50. Inside one he hid a rabbit – not a real one, of course, just a card with a
rabbit picture on it! He then put cards in all the other envelopes so that if an
envelope was chosen with a number lower than the one holding the rabbit, the
card would read “Try a higher number”, otherwise the card would read “Try a
lower number”.

Students have to find the rabbit using a binary search, and write down the
numbers of all the envelopes they open (in order) during their search.
Remember, in a binary search you have to pick the middle envelope in the
range you are searching. This is easy to find if there is an odd number of
envelopes, but with an even number, you have to choose the lower numbered
of the two middle envelopes. That means 25 will always be the first envelope
checked.

Input:

Each line of input will be a single number in the range 1 to 50 inclusive, it
being the number of the envelope in which Mr Farkle has hidden the rabbit.
The final input will be 0 which should not be processed.

Output:

For each line of input, output the numbers of all envelopes opened, in the
order they were opened, until the rabbit is found. Each number must be on
the same line separated by a space from the previous number.
"""


def half(lowerBound, upperBound):
    sum = upperBound + lowerBound
    if sum % 2 == 0:
        middle = int(sum / 2)
    else:
        middle = int(sum // 2)
    return middle


envHidden = int(input())
answerList = []

while envHidden != 0:
    answer = ""
    upperBound = 50
    lowerBound = 1
    num = 0
    if 1 <= envHidden <= 50:
        while num != envHidden:
            num = half(lowerBound, upperBound)
            if envHidden < num:
                upperBound = num
            else:
                lowerBound = num

            answer += str(num) + " "
    answerList.append(answer)
    envHidden = int(input())

print(*answerList, sep="\n")
