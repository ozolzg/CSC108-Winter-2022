"""
Q1: Short Answer
4 marks


For Parts A and B, you are being marked not only on correctness but also on simplicity.
The allowed operators are those that we have used in the course.

A. 1 mark
Suppose that x and y are variable names that already refer to Boolean values.
Write an expression (not a statement!) that evaluates to True iff x or y,
but not both, are True.

# (x or y) or not(x and y)


B. 1 mark
Suppose that x, y, and z are variable names that already refer to Boolean values.
Write an expression (not a statement!) that evaluates to True iff
at least one of the three variables (x, y, z) is False.

# not(x and y and z)


C. 2 marks
Consider the following code:
"""


def sort_and_pop(x: list, i: int) -> list:
    x.sort()
    return x.pop(i)


# Dan's code
lst = [23, 17, 3, 13, 11, 5, 7, 2, 19, 1]
lst = sort_and_pop(lst, 5)
lst = sort_and_pop(lst, 2)

"""
If you run this code, you'll find that it produces an error.
Surprise! According to the type contract, Dan's Code should work. But it doesn't, because
the function type contract has faulty type annotations.

Correct the function type contract so that it's clear from the type contract
that Dan's code will not work.
(Dan's Code will and should remain an incorrect use of the function!)
"""

# def sort_and_pop(x: list, i: int) -> int:
#     x.sort()
#     return x.pop(i)
