"""
problem H:

Tom and Jerry have come up with a simple way of encrypting their text messages to each
other. In this problem you will help them by translating encrypted messages into normal text.
Both boys' phones have letters on the keys 2 to 9 as is standard (see diagram). When Tom sends a message to
Jerry, he presses the required key one time too many, so gets the letter after the one he wants, unless the letter is
the last one on the key when he presses the key just once.
When Jerry sends a message to Tom, he presses the required key one time less than he normally would,
so gets the letter before the one he wants, unless the required letter is the first one on the key
when he selects the last letter. The boys do not encrypt digits, punctuation or spaces. All letters are lower case.

Input:

Each line in the input begins with a letter to show who sent the message that follows – this will
be an upper case J (for Jerry) or an upper case T (for Tom). This is not part of the message,
but is there so you know how to decrypt it. The last line starts with # - do not process this line.

Output:

For each line of input, output the normal text translation of the message (excluding the initial
letter). Each output should be on a line of its own.
"""