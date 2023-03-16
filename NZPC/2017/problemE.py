"""
Problem E:
Parity is an important concept in data transmission. Because the process is not error
proof, parity is used to provide a check on whether or not data has been corrupted in
transmission.

If even parity is being used, each byte will have an even number of 1 characters. If
odd parity is being used, each byte will have an odd number of 1 characters.
In this problem, we are looking for a single bit that has been corrupted. To help you
find it, the last byte is not part of the data being transmitted, but is a parity byte. Each
bit of the parity byte will be used to make the corresponding bits in the data bytes odd
or even depending on the parity being used.

Input:
The first line of input is a single integer, N (3 <= N <= 10), the number of bytes of data
to follow. The next N lines each contain a single byte of data consisting of 8 characters
separated by spaces. Each character will be either 1 or 0.

There will be one further line of 8 characters (again 1 or 0) which will be the parity
byte. In the parity byte, each bit is a parity bit for the corresponding bits in the
preceding N lines, using the same parity as is used by the data bytes. The parity byte
itself may not show the same parity as the data bytes

Output:
Output 3 lines of information about the data in the input.
Line 1: Either the word Even or the word Odd to describe the parity being used by
the bytes which are not broken.
Line 2: Byte <number> is broken
Line 3: Bit <number> is broken
<number> is the number of the appropriate byte or bit, where the first of each is
number 1.
"""


def CheckByte(bList, totalcountOne):
    lineByte = 0
    for currentByte in bList:
        numOne = 0
        for b in currentByte:
            if b == "1":
                numOne += 1
        if numOne % 2 != totalcountOne % 2:
            lineByte = bList.index(currentByte) + 1
            break
    return lineByte


def CheckBit(bList, totalcountOne):
    lineBit = 0
    for i in range(len(bList[0])):
        countBit = 0
        for byte in bList:
            if byte[i] == "1":
                countBit += 1
        if countBit % 2 != totalcountOne % 2:
            lineBit = i + 1
    return lineBit


numByte = int(input())
bytesList = []
count = 0
if 3 <= numByte <= 10:
    for i in range(numByte + 1):
        byte = input()
        bytesList.append(byte.split(' '))

    for bit in bytesList[-1]:
        if bit == "1":
            count += 1

    if count % 2 == 0:
        print("Even")
        isEven = True
    else:
        print("Odd")
        isEven = False

    numLineByte = CheckByte(bytesList, count)
    print("Byte " + str(numLineByte) + " is broken")

    numLineBit = CheckBit(bytesList, count)
    print("Bit " + str(numLineBit) + " is broken")





