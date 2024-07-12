#!/usr/local/bin/python3
# solve_birds.py : Bird puzzle solver
#
# Code by: Onkar Jadhav ojadhav, Sai Teja Burla saburla, Maitreya Kanitkar mkanitka
#
# Based on skeleton code by D. Crandall & B551 course staff, Fall 2022
#
# N birds stand in a row on a wire, each wearing a t-shirt with a number.
# In a single step, two adjacent birds can swap places. How can
# they rearrange themselves to be in order from 1 to N in the fewest
# possible steps?

# !/usr/bin/env python3
import sys
from queue import PriorityQueue

N = 5


#####
# THE ABSTRACTION:
#
# Initial state:

# Goal state:
# given a state, returns True or False to indicate if it is the goal state
def is_goal(state):
    return state == sorted(state)  # changed the problem specific goal state to a generalized goal state


# Successor function:
# given a state, return a list of successor states
def successors(state):
    return [state[0:n] + [state[n + 1], ] + [state[n], ] + state[n + 2:] for n in range(0, N - 1)]


def get_sorted_dict(state):
    s = sorted(state)
    d = {}

    for i in s:
        d[i] = s.index(i)

    return d


# Heuristic function:
# given a state, return an estimate of the number of steps to a goal from that state

# Here I have chosen the heuristic to be the number of misplaced tiles in a given state.
def h(state):
    c = 0
    d = get_sorted_dict(state)
    for i in state:
        if state.index(i) != d[i]:
            c += 1

    return c


#########
#
# THE ALGORITHM:
#
# This is a generic solver using BFS.
# Added a priority queue which dequeues the fringe using the value of the heuristic function and the cost.
#
def solve(initial_state_):
    cost = 0
    fringe = PriorityQueue()
    fringe.put((initial_state_, [], h(initial_state_) + cost), )

    while fringe.qsize() > 0:
        state, path, fn = fringe.get()

        if is_goal(state):
            return path + [state, ]

        for s in successors(state):
            fringe.put((s, path + [state, ], h(s) + cost + 1))

    return []


# Please don't modify anything below this line
#
if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise (Exception("Error: expected a test case filename"))

    test_cases = []
    with open(sys.argv[1], 'r') as file:
        for line in file:
            test_cases.append([int(i) for i in line.split()])
    for initial_state in test_cases:
        print('From state ' + str(initial_state) + " found goal state by taking path: " + str(solve(initial_state)))
