"""
problem G:

Miss Fotheringale is teaching her maths class about plotting graphs. As a first exercise,
she wants them to plot a linear graph y = ax + b for values of x from 0 to 10 inclusive.
She wants you to help by writing a program that outputs the correct answers to make it
easier for her to mark her pupils' work.

Input:

The first line of input is a single number N, 0 < N < 30, a positive integer that tells the
number of graphs to be plotted.
N lines then follow, each representing one graph to be plotted. Each line contains 2
positive integers, A and B, 0 <= A, B <10, being the values of a and b for the graph.

Output:

For each graph, firstly output the equation being plotted on a line by itself. Under this must
be the graph. All points on the axes, plus points on the graph must be represented by the
* character. The x axis must contain the points 0 to 10 from left to right, the y axis the
points 0 to the maximum value from bottom to top.
"""

numGraph = int(input())
for i in range(numGraph):
    xlist = [(int(i) + 1) for i in range(10)]
    ylist = []
    line = input()
    A = int(line.split(' ')[0])
    B = int(line.split(' ')[1])
    if 0 <= A < 10 and 0 <= B < 10:
        for x in range(10):
            y = A * x + B
            ylist.append(y)
    
    # print("y = {0}x + {1}".format(A, B))
