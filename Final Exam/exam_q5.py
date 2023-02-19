"""
Q5: Dictionaries and Files
6 marks


To get a passing grade in this question, you must make good use of a Python dictionary.

Each line of a hockey file contains a four-digit year, a team name, 
and a two-digit number of wins.

Here is one such file, hockey.txt:

2003maple leafs45
2020maple leafs35
1995senators18
1996maple leafs30
2000senators48
2012canadiens48

The first line of the file, for example, says that in 2003 (year), 
the maple leafs (team name) had 45 wins.

Write a function that takes an open hockey file and returns a list of tuples,
where each tuple refers to a team name and that team's maximum number of wins in any year.

Here is a sample call of the function on hockey.txt:

>>> teams_and_most_wins(open('hockey.txt'))
[('maple leafs', 45), ('senators', 48), ('canadiens', 48)]

"""

from typing import TextIO

def teams_and_most_wins(f: TextIO) -> list[tuple[str, int]]:
    '''
    f is an open hockey file.
    Each year has 4 digits and each number of wins has 2 digits.

    Return a list of tuples where each tuple stores
    a team name and that team's maximum number of wins in any year.

    Every team should appear in exactly one of the tuples.
    '''



# return [(x, dic[x]) for x in dict]
#
# dic = {}
# for row in f:
#     team = row[4:-2]
#     if team in dic:
#         prev_wins = dic[team]
#         curr_wins = row[-2:]
#         dic[team] = max(prev_wins, curr_wins)
#     else:
#         dic[team] = row[-2:]
#
# return [(team, dic[team]) for team in dic]


