"""
problemF:

You probably know about HTML, the mark up language used to create Web pages.
HTML code contains a number of tags which are expected to follow certain rules.
In this problem we will be concerned with two of these rules:
1 Every opening tag has to have a corresponding closing tag
2 All tags must be properly nested.
Tags are marked by angled brackets which contain a keyword, such as <body> or
<strong>. These are opening tags, the corresponding closing tags having / before
the keyword, ie </body> and </strong>. It is possible for a tag to be both opening
and closing, such as <br />, which complies with rule 1.
A keyword is a single lower case word with no spaces.
To be properly nested, if a tag is opened inside another tag, it must be closed before
the other tag closes. For example
<body> <strong> </strong> </body> is properly nested
<body> <strong> </body> </strong> is not, and breaks rule 2.

Notes

If there are no tags present, the text complies with both rules.
Attributes may be present within an opening tag, such as
<a href="http://www.nzprogcontest.org.nz">This is a link</a>
The closing tag has only to match the keyword, not the attributes.

Input

Input will consist of a number of lines of HTML code, each line containing from 0 to
255 characters. The last line will contain a single # character – do not process this
line. Within the text of each line will be zero or more tags. No angle bracket will be
present unless it is part of a properly formed tag.
Determine whether or not the HTML meets the rules specified above.

Output

Output will consist of a single line for each line of input. The line will contain either the
word legal, or the word illegal. 
"""

results = []

line = input()
while line != "#":
    
    line = input()
[print(i) for i in results]