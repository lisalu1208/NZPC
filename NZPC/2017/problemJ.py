"""
Modern art is something that everyone has an opinion about – you love it or you hate it. Rarely
discussed however is what aficionados consider to be the pinnacle of human (and computer) artistic
achievement – ASCII art. In this problem you are (or rather your computer is) asked to rise to the
lofty aesthetic levels of this amazing art form and draw a binary tree.

Consider the tree shown below on the left. It has six nodes, each labelled with an upper case letter
of the alphabet. Node A is the root of the tree. It has two sub-trees, the first shown above to the
right of A and the second below to the right. The tree is binary in the sense that each node may
have at most two sub-trees, however it is not balanced – E has no first sub-tree, only a second.

The same tree is shown on the right in ASCII art. Nodes are shown using their letters. Single
forward and backward slash characters are used for edges. Where a subtree doesn’t fit into the
space above or below its parent node the connecting line is extended with vertical bar characters
directly above or below the node character, as required. See sample output for examples.

Input:
Input will consist of a series of trees. The first line of the input holds a single integer T, being the
number of trees (1 <= T <= 100). Then for each tree, there is a line of input describing the tree in
prefix format – for a node the letter of the node is output first, followed by the coded first subtree,
and then the coded second subtree. Each node is output with two subtrees. If a subtree is empty it
is output as a ‘@’ character. The input for the tree drawn above is ABC@@D@@E@F@@
Each input tree description will be no longer than 100 characters. Note that node letters may be
repeated and may not be in alphabetic order.

Output:
For each tree your program should output one line with the text “Graph” and the number of the tree
(counting from 1). This should be followed by the ASCII tree drawn as described. Lines should not
have trailing blank characters. Output one blank line between trees. Note that the sample output is
presented twice on the next page – on the left as it should appear, and on the right with space
characters replaced by periods. This is provided to help clarify the format.
"""