"""
problem D:

Pictures can take up a lot of memory, so ways to encode images to save memory have been
invented. In this problem you have to take a fairly simple encoding and turn it into a picture.
The images here are all black and white and have been represented by X characters for black
and dot (.) characters for white. The encoding rule is simple. Starting from the left, the number
of consecutive white characters is recorded. This will be from 0 to 9 – if there are more than
nine, subsequent characters will be encoded separately, preceded by a _ character to show a
continuation. The number of consecutive black characters is then similarly recorded.
Your task is to expand the encoded data to produce the original picture.

Input:

The input will consist of a number of rectangular images, each represented by encoded data.
The first line will contain two integers C and L, separated by a space. C (0 < C < 100)
represents the number of characters to a line while L (0 < L < 50) represents the number of
lines in the image. The line 0 0 will mark the end of input and should not be processed.
L lines will follow each consisting of a set of single digits representing the characters in that line.
The _ character will be used where more than 9 consecutive characters of the same type occur
(see above). Adding the digits will give C.

Output:

For each image, output a line of the format Image n, where n is the image number. The images
are numbered consecutively in the order they appear in the input, starting with 1. The
characters on each line of the image must be output with X characters to represent black and
dot characters to represent white.
"""

