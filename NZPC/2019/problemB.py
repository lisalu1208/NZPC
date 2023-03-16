"""
problem B:

How is your arithmetic? In this problem, you will be presented with 2 numbers and
have to calculate and display their sum, difference, product, quotient and remainder.

Input:

Input will consist of 2 numbers, N1 and N2, each on a line of its own. Both numbers
will be integers between -100 and 100 inclusive. N2 will not be 0.

Output:

Output 4 lines showing the required values. The required output format is:
N1 + N2 = <sum>
N1 - N2 = <difference>
N1 x N2 = <product>
N1 divided by N2 is <quotient> remainder <remainder>
where <sum> is N1 + N2, <difference> is N1 – N2, <product> is N1 x N2,
<quotient> is N1 divided by N2 (integer part only) and <remainder> is the remainder
when N1 is divided by N2.
"""

num1 = int(input())
num2 = int(input())

if -100 <= num1 <= 100 and -100 <= num2 <= 100 and num2 != 0:
    print("{0} + {1} = {2}".format(num1, num2, num1 + num2))
    print("{0} - {1} = {2}".format(num1, num2, num1 - num2))
    print("{0} x {1} = {2}".format(num1, num2, num1 * num2))
    print("{0} divided by {1} is {2} remainder {3}".format(num1, num2, int(num1 / num2), num1 - num2 * int(num1/num2)))
