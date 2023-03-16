"""
problem M:

A string hashing function is an algorithm that turns arbitrary strings into numbers. If S is a string of length N,
one simple hashing function is
      S[0] * 31^(N‐1) + S[1] * 31^(N‐2) + ... + S[N‐1]
where S[i] is the ASCII code of the i'th character and ^ indicates exponentiation. The computation is done
using big integer arithmetic (it never overflows).
Note: In most programming languages ^ does NOT perform exponentiation.
Here are some example strings and the corresponding values computed by this hashing function:
1. "ab" (N = 2, ASCII codes of characters: 97 98)
hash = 97 * 31 + 98 = 3105
2. "Hi!" (N = 3, ASCII codes of characters: 72 105 33)
hash = 72 * 31^2 + 105 * 31 + 33 = 72480
3. "IJ!" (N = 3, ASCII codes of characters: 73 74 33).
hash = 73 * 31^2 + 74 * 31 + 33 = 72480
Sometimes different strings have the same hash (like the second and third strings above).
A string is considered valid if all its characters have ASCII codes in the range 32 to 126 inclusive.
Your task is to count the number of valid strings that have the same hash as a given input string.

Input:

Input consists of several lines. Each line describes a string using a sequence of space‐separated integers in
the format
      N S[0] S[1] ... S[N‐1]
N is the length of the string (1 <= N <= 1000) and S[i] is the ASCII code of the i'th character (32 <= S[i] <= 126).
A value of N = 0 indicates the end of the input and should not be processed.

Output:

For each test case, print a single integer: the number of valid strings that have the same hash as the input
string (including the input string itself), modulo 1,000,000,007 (10^9 + 7).
"""

