"""
Q2: Multiple Choice
10 marks


For each of the following multiple choice questions, clearly indicate your answer
by placing a * to the left of the answer that you choose.

E.g,. On this question I wish to mark answer 'b' as the correct answer.

What is the right answer?
a) no no no
* b) something true
c) not this answer
d) also not this answer


TODO answer all subquestions


Q2.1
Consider this Python function.

def f(number):
    if number > 10:
        if number < 20:
            return True
        else:
            return False
    else:
        return False

Which of the following does exactly the same thing as that function above?

a)
def f(number):
    return number > 10 or number < 20

b)
def f(number):
    return number > 10 and number > 20

c)
def f(number):
    return number < 10 or number < 20

d)
def f(number):
    return number > 10 and (not number < 20)

* e) None of the above


--------------------

Q2.2
Consider this Python function.

def first_longer(tweet1: str, tweet2: str) -> bool:
    '''
    Return tweet1 or tweet2, whichever is longer.

    >>> first_longer('abc', 'd')
    True
    '''
    return len(tweet1) > len(tweet2)

One of the components of this function is inconsistent with the rest. Which is it?

a) Example
b) Type contract
* c) Description
d) Body (code)


--------------------

Q2.3
Which of the following is true of short-circuiting?

a) It can be used for 'or', but not 'and'.
* b) It can be used for both 'and' and 'or'; its use depends on particular values.
c) It is used on any Boolean expression; it doesn't matter what the values are.
d) 'x or y' is always the same as 'y or x' because of short-circuiting.


--------------------

Q2.4
Here is a Python function.

def do_something(lst1, lst2):
    for element1 in lst1:
        for element2 in lst2:
            if element1 >= element2:
                return False
    return True

What is the overall purpose of this function?

a) Return True iff the length of lst2 is less than the length of lst1.
b) Return True iff each element in lst1 is less than the element at the same index in lst2.
* c) Return True iff every element in lst1 is less than every element in lst2.
d) Return True iff every element in lst1 is less than the first element in lst2.
e) Return True iff every element in lst2 is less than the first element in lst1.


--------------------

Q2.5
Think back to our code that inverts a dictionary. What would happen if our
original dictionary had lists as values, and we tried to invert it?

a) It would work. The inversion code handles this.
* b) It would not work. It would try to create a dictionary
   that had lists as keys, and that isn't allowed.
c) It would work, unless there were collisions.
d) The question makes no sense: there can't be a dictionary that has lists as values.


--------------------

Q2.6
I am designing a Refrigerator class.
What should I use to add current_temperature to the class?

* a) An attribute
b) A method
c) Inheritance
d) A complete new class


--------------------

Q2.7
Here is the design recipe for a Python function.

def common(s1: str, s2: str) -> tuple[int, int]:
    '''
    Given two strings of equal length s1 and s2, return a tuple where
    the first element is the number of positions where s1
    and s2 have the same character, and the second element is the
    number of positions where s1 and s2 have the same character ignoring case.
    '''

Here are some possible test cases for this function. Assume that we are
going to include them all in our test suite, except one.
Choose the letter for the test that should be removed.

a) common('', '')
b) common('a', 'a')
c) common('aBC', 'abC')
* d) common('abc', '')
e) common('abc', 'def')


--------------------

Q2.8
What is the time complexity of the following function?

def mystery(lst):
    index = 0
    while index < 1000:
        index2 = 0
        while index2 < index ** 2:
            index2 = index2 + 1
        index = index + 1

* a) Linear
b) Quadratic
c) Slower than quadratic
d) Faster than linear


--------------------

Q2.9
What is the time complexity of the following function?

def mystery(lst):
    index = 0
    while index < len(lst):
        index2 = 0
        while index2 < index:
            index2 = index2 + 1
        index = index + 1

a) Linear
* b) Quadratic
c) Slower than quadratic
d) Faster than linear


--------------------

Q2.10
You are trying to decide whether to use a while loop, a for loop, or a for-range loop.
Which of the following is good advice?

a) Always use a for loop; the for loop is most powerful.
b) Always use a while loop, except when user input is involved.
* c) Use a while loop when the number of iterations is not known.
d) Use a for-range loop as a more flexible loop than a while loop.

"""
