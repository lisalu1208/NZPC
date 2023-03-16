"""
Problem E:

Shroeder and Patsy heard from a friend whose computer had been attacked
by a ransom virus. A nasty message appeared telling their friend that all his
files had been encrypted and that it would cost him to have them restored.

Being keen programmers, Shroeder and Patsy, just for fun you understand,
wondered how that worked. They tried a simple encryption which would
depend of a key which was a single number.

They thought they could use a sort of Caesar cipher (where letters are shifted
a number of places through the alphabet which is considered circular so A
follows Z). They would start with a shift somewhere between 1 and 25 (the
key), then increase it by one each letter. It would cycle round so after 25
would become 1 again.

To decipher, if you know the key it is quite easy, as long as you remember to
shift in the opposite direction!

Input:

Input consists of a single integer, K, the key, followed by a line of encrypted
text. The text will be no more than 250 characters long, and will consist of
lower case letters, spaces, digits and punctuation marks only. Only letters are
to by encrypted.

Output:

Output the line of text correctly decrypted.
"""

key = int(input())
text = input()
alphaList = [chr(i) for i in range(ord('a'), ord('z') + 1)]
answer = ""

for ch in text:
    if ch.isalpha():
        newIndex = alphaList.index(ch) - key
        if newIndex < 0:
            newIndex = len(alphaList) - (key - alphaList.index(ch))
        answer += alphaList[newIndex]
        key += 1
        if key > 25:
            key = 1
    else:
        answer += ch

print(answer)
