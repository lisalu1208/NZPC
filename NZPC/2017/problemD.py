"""
problemD:
Recently discovered on a distant planet, a race of aliens has music a bit like ours (notes A, B, C, D, E, F and G) but
without any sharps or flats. Like our music, after G they start again at A.

To these aliens, beautiful music is any sequence of notes where the difference between 1 note and the next is 2, 4 or 6
notes above the previous note. Anything else is discordant and causes them discomfort.

Input:
Each line of input contains a set of N notes with no spaces between then (0 < N <= 21). Each note will be one of the
upper case letters between A and G inclusive. The final line of input will be a # symbol on its own. Do not process this
line.

You must assume that a note is the next note of that letter above the previous note.

Output:
For each line of input, if the notes follow the rule for being beautiful music, your output should be:
That music is beautiful.

Otherwise, the output should be: Ouch! The hurts my ears.
"""

notesList = ["A","B","C","D","E","F","G"]
notes = input()
answer = ""
outputList = []
while notes != "#":
    if len(notes) == 1:
        answer = "That music is beautiful."
    else:
        for i in range(len(notes)-1):
            difference = notesList.index(notes[i+1]) - notesList.index(notes[i])
            if difference < 0:
                difference = difference + len(notesList)
            if difference not in [2, 4, 6]:
                answer = "Ouch! That hurts my ears."
                break
            else:
                continue

    if answer == "":
        answer = "That music is beautiful."
    outputList.append(answer)
    notes = input()
    answer = ""

print(*outputList, sep="\n")
