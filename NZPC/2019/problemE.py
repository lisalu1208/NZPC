"""
problem E:

Netball has had a high profile recently in New Zealand. The men’s team beat the women’s team
(the Silver Ferns) in a recent series. The Silver Ferns then went on to win the World
Championship. This has led to an upsurge in the number of people who want to take part in netball
coaching classes.
Alison Cooke runs a highly rated course at various centres across New Zealand. To pass the
course, a student must participate in 5 exercises for which they will be graded.
Performance in each exercise is given a pass/fail grade, and must be passed to score a mark
above 0. A mark of 10 is awarded if an exercise is passed first time, 7 if passed second time and
4 if passed after 3 or more attempts.
Exercises are weighted according to how difficult Ms Cooke judges them to be. This will vary
from course to course, but each exercise will be weighted between 1 and 3. The student’s mark
is multiplied by the weighting of the exercise to give their weighted mark for each exercise.
Exercise marks are added to give each student a total weighted mark for the assessment.
To pass a student’s total weighted mark must be at least 50% of the total weighted marks available
for the 5 netball exercises.

Input:

The first line of input will contain 5 numbers, separated by spaces, which are the weightings for
each of the 5 exercises. Each weighting will be an integer between 1 and 3 inclusive.
The next line will contain a single integer, S (0 < S <= 25), the number of students to assess.
There then follow S lines, each defining one student. A line will contain no more than 32
characters. The line contains a 4 digit ID, the student’s first name followed by the student’s last
name, all separated by spaces.
There then follows a series of lines representing the results for students in the exercises. Each
line has the following format:
<student id> <exercise> <result>
where <student id> is the 4 digit ID of the student whose result is shown,
<exercise> is one of the letters A to E to identify the exercise,
<result> is one of the letters P or F to indicate Pass of Fail
A student who fails an exercise may take it again until it is passed.
The final line will be
0 # #
This line marks the end of input and should not be processed.

Output:
Output consists of one line for each student from the input, in the same order as they were input.
Each line will contain the name of the student followed by a space, then the word Pass or the
word Fail.
"""

exercise = ['A', 'B', 'C', 'D', 'E']
exerciseWeights = list(zip(exercise, [int(weight) for weight in input().split(' ')]))

numStudents = int(input())
studentList = []

if 0 < numStudents <= 25:
    for i in range(numStudents):
        line = input()
        id = int(line.split(' ')[0])
        name = line.split(' ')[1] + " " + line.split(' ')[2]
        totalscore = 0
        time = [1] * 5
        studentList.append([id, name, totalscore, time])

    exerciseResult = input()
    while exerciseResult != "0 # #":
        stuID = int(exerciseResult.split(' ')[0])
        ex = exerciseResult.split(' ')[1]
        result = exerciseResult.split(' ')[2]
        stuIndex = [ind for ind in range(len(studentList)) if stuID in studentList[ind]][0]
        exIndex = [i for i in range(len(exerciseWeights)) if ex in exerciseWeights[i]][0]
        # print(str(exIndex))
        # print(str(studentList[index]))
        if result == "P":
            if studentList[stuIndex][3][exIndex] == 1:
                studentList[stuIndex][2] += exerciseWeights[exIndex][1] * 10
            elif studentList[stuIndex][3][exIndex] == 2:
                studentList[stuIndex][2] += exerciseWeights[exIndex][1] * 7
            else:
                studentList[stuIndex][2] += exerciseWeights[exIndex][1] * 4
        elif result == "F":
            studentList[stuIndex][3][exIndex] += 1
        exerciseResult = input()

    totalMark = 0
    for i in range(len(exerciseWeights)):
        totalMark += exerciseWeights[i][1] * 10

    for index in range(len(studentList)):
        if studentList[index][2] >= (totalMark * 0.5):
            print("{0} Pass".format(studentList[index][1]))
        else:
            print("{0} Fail".format(studentList[index][1]))



