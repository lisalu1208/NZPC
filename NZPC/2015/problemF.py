"""
problem F:

James Pond is a business man who often dreams he is a secret agent! He enjoys encrypting
messages to his colleagues, who then have the task of decrypting them in order to read them.
Your task is to write the decryption program for his staff to use.
Mr Pond uses the date as a key. He adds the day, month and year together, does a modulo 25
(remainder operator) on the answer and adds one to give him a value from 1 to 25 inclusive.
This value, S, becomes the shift in his Caeser cypher.
In a Caesar cypher, each letter of a message is shifted S places forward through the alphabet,
with z shifting to a where appropriate. For example, with a shift of 5, a becomes f, h becomes
m and x becomes c. White space, punctuation and digits are not changed.

Input:

Each message starts with the date as 3 integers on a single line, separated by spaces. A date
of 0 0 0 marks the end of input.
The date is followed by a single line of at least 1 and no more than 250 characters; the line will
not be just white space. Only lower case letters, spaces, punctuation marks and digits are
used.
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
a b c d e f g h i j k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z

Output:

For each message in the input, output a single line showing the decrypted message.
"""


alphaList = [chr(i) for i in range(ord('a'), ord('z') + 1)]
date = input()
answerList = []
while date != "0 0 0":
    answer = ""
    key = 0
    numbers = [int(x) for x in date.split(' ')]
    key += sum(numbers)
    cipher = key % 25 + 1
    line = input()
    for ch in range(len(line)):
        if line[ch].isalpha():
            newindex = alphaList.index(line[ch]) - cipher
            if newindex >= 0:
                answer += alphaList[newindex]
            else:
                answer += alphaList[newindex + 26]
        else:
            answer += line[ch]
    answerList.append(answer)
    date = input()

print(*answerList, sep="\n")
