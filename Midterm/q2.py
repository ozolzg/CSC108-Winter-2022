"""
Q2: Debugging
3 marks

Consider the following function and attempted body.
"""


from typing import TextIO

def clean(in_file: TextIO, out_file: TextIO) -> None:
    '''
    in_file is a file open for reading; out_file is a file open for writing.
    Each line in in_file ends with a newline character.
    Copy each line from in_file to out_file.
    For any line that includes a *, do not include the first *
    or any following characters on that line.
    '''

    in_file = open(in_file)  # Line 1
    out_file = open(out_file, 'w')  # Line 2
    line = in_file.readline()  # Line 3
    while line.strip():  # Line 4
        line = in_file.readline()  # Line 5
        if '*' in line:  # Line 6
            line = line[:line.find('*')+1] + '\n'  # Line 7
        out_file.write(f'{line}\n')  # Line 8
        line = in_file.readline()  # Line 9


"""
There may be some bugs or errors in this code that prevent it from working properly.

For each line, indicate:
*OK* if the line is correct
*REMOVE* if the line has to be removed.
*CHANGE* if the line has to be changed
 (here, please also indicate what the line has to be changed to).


# TODO: tell us what to do with each line

Line 1 *OK*

Line 2 *OK*

Line 3 *OK*

Line 4 *OK*

Line 5 *REMOVE*

Line 6 *OK*

Line 7 *CHANGE* - in line[:line.find('*')+1] + '\n', +1 must be removed, so that the string after including * is not include.

Line 8 *CHANGE* - \n must be removed. in_line already contains '\n'

Line 9 *OK*


"""
