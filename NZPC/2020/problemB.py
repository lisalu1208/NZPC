"""
problemB:

Whenever somebody goes to an ATM to withdraw or deposit money, a calculation has
to be done to keep the person's bank balance correct. Your task in this problem is to
do such calculations. There is a bank rule that says that a customer may not have an
overdraft of more than $200, so any withdrawal that would take the balance below
-200 must be stopped. (A minus sign is used to indicate an overdraft, or negative
balance). There is no upper limit for an account balance.

Input:

Input consists of a number of lines, each representing a transaction. Each transaction
consists of an integer representing the starting balance (between -200 and +10,000),
the letter W or the letter D (Withdraw or Deposit), followed by a second integer
representing the amount to be withdrawn or deposited (between 5 and 400). Input will
be terminated by a line containing 0 W 0.

Output:

Output consists of one line for each line of input showing the new balance for each
transaction, except that if a withdrawal would take the balance below -200, the output
must be the words Not allowed
"""

line = input()
result = []
while line != "0 W 0":
    starting_balance = int(line.split(" ")[0])
    transaction = line.split(" ")[1]
    transaction_amount = int(line.split(" ")[2])
    if transaction == "D":
        result.append(starting_balance + transaction_amount)
    elif transaction == "W":
        if starting_balance - transaction_amount > -200:
            result.append(starting_balance - transaction_amount)
        else:
            result.append("Not allowed")
    line = input()

[print(i) for i in result]

