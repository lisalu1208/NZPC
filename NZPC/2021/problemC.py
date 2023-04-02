"""
problemC:

An arithmetic sequence is one in which there is some first number, 
and then a series of numbers which are all a fixed number different.
For example 3, 5, 7, 9 is an arithmetic sequence that has
a first number 3. Then each term after that in the
sequence is formed by adding 2 to the previous term.
(The terms are different by 2). The 3 is also called the first
term (term 1) and 9 is the 4th term.
Given a starting number, a difference and a value, your program is to work out if the number
could be part of the sequence. If so, output which term that number would be, and if not, output
that it is not in the sequence.

Input:

Input will consist of a number of lines, where each line has 3 numbers separated by spaces.
The first number is an integer that is the first term in the sequence. The second is the
difference - this will be a non-zero integer. The third is the value that you will need to test to
determine whether it can be part of the sequence or not. It will not be the same as the first
term.
Input is terminated by a zero value for each of the 3 numbers.

Output:
Output will consist of one line for each input line. It will consist of either “Term X“ where X is an
integer indicating which term it is, or “Not in sequence” if the number isn’t part of the
sequence
"""

results = []

line = input()

while line != "0 0 0":
    start = int(line.split(" ")[0])
    difference = int(line.split(" ")[1])
    test = int(line.split(" ")[2])
    if (test - start) % difference == 0:
        results.append("Term {0}".format(int((test-start) / difference + 1)))
    else:
        results.append("Not in sequence")
    line = input()
[print(i) for i in results]