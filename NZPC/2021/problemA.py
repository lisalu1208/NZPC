"""
problem A:

Keepsafe is a tool used by KiwiBank to “provide an extra layer of security to
help protect customers while using Kiwibank Internet Banking.” Customers
have to set up a number of security questions and answers. After logging
in with a user name and password, a customer is presented with one of
their security questions and a space for the answer. Two letters in the
answer have to be entered as shown by white boxes.
For example:
If the pet's name was “Whisper”, the customer would press the P key then the R key. The
letters pressed must correspond, in order, to the two spaces in the outline answer to the
security question.
For this problem, you have to check customers' answers and verify that they are as expected

Input:

Input consists of a security question answer and a login attempt for one customer, each on a
separate line.
The first line contains the security question answer. It will consist of upper case letters and
single spaces only, starting and ending with a letter. There will be no more than 32 characters.
The next line shows the login attempt which consists of 2 positive integers followed by 2 upper
case letters, all separated by single spaces. The integers are the numbers of the characters
required to fill the two spaces in the outlined answer. They are presented in ascending order.
When numbering characters in the answer, the first character is 1, but only letters are assigned
numbers, spaces being ignored. The two letters are those entered by the customer into the two
spaces. They are expected to correspond to the letters in the appropriate places in the security
answer required.

Output:

Output consists of a single line containing one word. If the two letters entered match the letters
in the required places in the answer, in the order presented, then the output will be “correct”.
If one or both letters are not correct, the output is “error”.
"""

answer = input().replace(" ","")
if answer.isupper() and len(answer) <= 32:
    line = input()
    num_char1 = int(line.split(" ")[0])
    num_char2 = int(line.split(" ")[1])
    char1 = line.split(" ")[2]
    char2 = line.split(" ")[3]
    if char1 == answer[num_char1 - 1] and char2 == answer[num_char2 - 1]:
        print("correct")
    else:
        print("error")