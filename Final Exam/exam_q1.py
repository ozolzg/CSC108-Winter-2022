"""
Q1: Short Answer
6 marks


A. 2 marks

You are working on a problem where the size of each test case is between 
1 and 100 integers and where the timeout is 4 seconds.
You have developed a cubic time algorithm for the problem that gives the correct answer
on all test cases.

If you submit that solution, will you pass all test cases in time?
Please answer YES or NO and then briefly explain your answer.

NO
Because integer 100 is the third power, we have a cubic time algorithm.
100 to the power of three doesn't happen in 4 seconds Not all test cases pass.



B. 2 marks

Your friend is working on a Python program and can't decide whether to use a
string, list, set, or dictionary. What general advice would you give them?
For each, tell them one reason that they might choose that type of data over the others.


String: you can concatenate strings or multiply strings by adding them.

List: By using a list, you can easily manage data through loops.

Set: there are various set operations such as union, intersection, difference, and complement that can be implemented
     very easily using set types.

Dictionary: Lists only use zero-based subscripts to access elements,
            whereas dictionaries can use any immutable data type, including strings and numbers.


C. 2 marks

In Assignment 3, you solved the Bard problem.

Next year, Dan is going to use a similar problem, but with a design change.
Every bard will now have a "teacher score" that represents how
skillfully they teach. As such, BARD_THRESHOLD is no longer enough to tell
whether a villager should become a bard at the end of a party. Instead, you should use
BARD_THRESHOLD minus the teacher score of the best teacher there. (As before,
no one can become a bard if there isn't already a bard at the party.)

What changes might Dan need to make to the program's .txt input file?

add new line for teacher score.


What changes might Dan need to make to the dictionary that stores villagers and/or
the set that stores bards?

just take BARD_THRESHOLD and minus teacher score.


"""
