"""
Q4: Writing a Program
4 marks


Write a program (not a function!) that asks the user for nonnegative integers,
one integer per line.
When the user is finished entering their integers, they enter a negative integer
to tell the program to stop asking them for more integers.
Once the input is complete, the program prints "No integers to average"
if the user provided no nonnegative integers,
and the average of the nonnegative integers otherwise.

You must NOT use lists, tuples, or dictionaries in your code.

Here is a sample program run where the user enters 4 and then 8 and then -1.
The program outputs Average: 6.0

4
8
-1
Average: 6.0

Here is another run where the user types -3 to the first prompt.
The program outputs No integers to average

-3
No integers to average


"""

average = 0
number = 0

while True:
    integer = int(input())
    if integer <= 0:
        print()
        break
    average += integer
    number += 1
if number == 0:
    print("No integers to average")
else:
    result = average / number
    print(result)
