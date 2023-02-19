"""
Q3: Pytest
3 marks


On Assignment 4, Question 1, you were asked to solve the Assignment Difficulty problem.
Now you're working on a function that you could use as part of your solution,
and have come up with the following code.
"""


def smallest_score(lst: list[int]) -> int:
    '''
    Valid sublists have at least 2 elements.
    Return the smallest score of any valid sublist of lst.
    lst is guaranteed to have at least 2 elements.
    '''
    in_order = lst[:]
    in_order.sort()
    res = in_order[1] - in_order[0]
    for i in range(len(in_order) - 1):
        res = min(res, in_order[i+1] - in_order[i])
    return res

"""
Unfortunately, your code is not correct.
Below, write a Pytest test case that fails,
but that should pass if your smallest_score function were correct.

Write ONLY the Pytest test case; don't try to fix the busted smallest_score code.
"""

def test_case1() -> None:
    nums = [5, 4, 3, 2, 1]
    assert smallest_score(nums) == 1

def test_case2() -> None:
    nums = [100, 57, 33, 24, 0]
    assert smallest_score(nums) == 9

def test_case3() -> None:
    nums = [44, 55, 10, 20, 30]
    assert smallest_score(nums) == 10

if __name__ == "__main__":
    pytest.main(["exam_q3.py"])
