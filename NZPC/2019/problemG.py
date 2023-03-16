"""
problem G:

To correctly evaluate an expression like 3 + 4 * 2, you need to know the rules of
arithmetic. You do the multiplication first, giving 8, then add the 3 to get 11. If you
add first to get 7 then multiply that by 2 you get 14, an incorrect answer.
An alternative way to write this expression is 3 4 2 * +. Here the operators come after
the operands (the numbers), hence postfix. To evaluate this, when you encounter the
*, multiply together the previous two operands (so 2 * 4) and store the answer. You
next encounter the + so add the stored answer, 8, to the 3. This is the same as the
answer in the first paragraph.
In this problem you will be required to evaluate expressions which use postfix notation.

Input:

The first line of input will be a single integer, N (0 < N <= 20), the number of
expressions to follow. The remaining N lines will each contain a valid expression for
you to evaluate.
Each expression will contain a list of non-negative integers less than 100 and
arithmetic operators (+ - * /) with no more than 30 characters. Every operator will have
two available operands. / is integer divide (returns only the integer part of the quotient).
Division by zero will not occur.

Output:

For each expression in the input, output the evaluation of the expression, a single
integer.
"""


def operate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return int(num1 / num2)


numExpressions = int(input())
if 0 < numExpressions <= 20:
    expression = input().split(' ')
    for i in range(len(expression)):
        answer = 0
        if expression[i] == "*" or "-" or "/" or "+" and i >= 2:
            num1 = int(expression[i - 2])
            num2 = int(expression[i - 1])
            operator = expression[i]


