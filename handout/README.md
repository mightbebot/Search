# Project: Search

## Introduction

In this project we will explore the use of search strategies to solve a
single agent search problem with a single or multiple goals, and a two-player
game with complete information. In order to illustrate their execution, we have
wrapped everything up into a mash-up of Angry Birds. In every exercise, the
agent controlled is represented by a red dot (if you look really hard into it,
you'll eventually see the infamous face of Red, an Angry Bird character).

In the first part, we will have to implement uninformed and informed search
strategies for the graph-search algorithm. This
includes Breadth-First Search, Iterative Deepening Search, and A*. Then,
relying on our implementation of A*, we will do some work with heuristics.
The necessary data structures has been provided for

1. the state representation
2. the successor function
3. goal test
4. cost of actions

Then we will move onto _Heuristics_. Remember that a heuristic is a function
that, given a state _s_, estimates the remaining cost to reach a _goal_ state
from _s_. You will be required to produce an admissible heuristic estimate for
the multi-goals variant of the problem, where the agent has to plan its actions
to collect not one, but multiple yellow-birds.

In the second part, the task is a two-player game where our code will control
one of the players (the Red player). Task will ask you to implement some basic
adversarial search algorithms, namely, MiniMax. As the depth of the search tree
for this problem can be huge, it is difficult to reach the solution. For this
reason you will be asked to implement a depth-bounded version of the algorithm,
together with an _evaluation function_, which is meant to produce a numeric
estimate of the _utility_ of a given game state for a given player.

You can find a _description of the search problems_ on the section [Getting
Started](1_getting_started.md).

## Which files to touch

In each subsection, you will find the description of the files we will implement
the algorithm for corresponding task.

## Common Errors

Note for Windows users: Make sure that you install Python in a path that
doesn't contain any spaces (e.g. don't put it in `Program Files`). Otherwise
the program will fail.

We recommend using [Anaconda Python](https://www.anaconda.com/download/) to do the project if you are newb to python.


It's important that you use Python 3.6 or later. If you use an earlier Python
version, you might get `SyntaxError: invalid syntax` on the type annotations.

## Walkthrough

1. [Getting Started: The Search Problems](../README.md)
2. [Implementing Search Algorithms: The Fundamentals](2_implementation_notes.md)
3. [Question 1: Breadth-First Search (difficulty: **---)](3_breadth_first_search.md)
4. [Question 2: Iterative Deepening Search (difficulty: **---)](4_iterative_deepening_search.md)
5. [Question 3: A\* (difficulty: ***--)](5_a_star.md)
6. [Question 4: Heuristics for Single-Agent Search Problems (difficulty: **---)](6_heuristics.md)
7. [Question 5: Minimax (difficulty: **---)](7_minimax.md)
8. [Question 6: Evaluation Function (difficulty: **---)](8_evaluation_function.md)
