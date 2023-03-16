"""
problem D:

A palindrome is a word, phrase, number or other sequence of characters
which reads the same backwards or forwards. Given a string of lower case
letters, can you make it a palindrome by deleting exactly one character? Note
that the size of the string after deletion would be one less than it was before.

Input:

Up to 30 lines each containing from 3 to 30 lower case letters. The final line
will just contain # - do not process this line.

Output:

If it is possible to make a palindrome from the text by deleting one letter,
display the palindrome text. If it is not possible, display not possible.

It may be possible to make more than one palindrome by deleting a single
letter. For example, madmam will become mamam if the d is deleted, or madam if
the middle m is deleted. In such a case, display the palindrome formed by
deleting the earliest letter from the text.
"""

text = input()
answer = []
while text != "#":
    ans = ""
    # reverseIndex = 0
    # txt = text[::-1]
    length = len(text)
    front = 0
    back = len(text) - 1
    while length != 0:
        if text[front] == text[back]:
            ans += text[front]
            front += 1
            back -= 1
            length -= 2
            if front >= len(text) or back < 0:
                break
        else:
            front += 1
            length -= 1
    # for i in range(len(text)):
        # for j in range(reverseIndex, len(txt)):
        #     if text[i] == txt[reverseIndex]:
        #         ans += text[i]
        #         reverseIndex = j
        #         break
        #     else:
        #         reverseIndex += 1
    if len(ans) == len(text) - 1:
        answer.append(ans)
    else:
        answer.append("not possible")
    text = input()
print(*answer, sep="\n")
