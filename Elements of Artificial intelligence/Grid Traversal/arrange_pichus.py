#!/usr/local/bin/python3
#
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#
# Submitted by : [ONKAR JADHAV, ojadhav]
#
# Based on skeleton code in CSCI B551, Fall 2022.

import sys


# Parse the map from a given filename
def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]


# Count total # of pichus on house_map
def count_pichus(house_map):
    return sum([row.count('p') for row in house_map])


# Return a string with the house_map rendered in a human-pichuly format
def printable_house_map(house_map):
    if house_map is None:
        return "False"
    else:
        return "\n".join(["".join(row) for row in house_map])


# Add a pichu to the house_map at the given position, and return a new house_map (doesn't change original)
def add_pichu(house_map, row, col):
    return house_map[0:row] + [house_map[row][0:col] + ['p', ] + house_map[row][col + 1:]] + house_map[row + 1:]


# All the 8 function below are used to return a list for its rows, columns and diagonals.
def up_rows(house_map, r, c):
    x = []
    while r >= 0 and house_map[r][c] not in 'X@':
        x.append((r, c))
        r -= 1
    return x


def down_rows(house_map, r, c):
    x = []
    while r < len(house_map) and house_map[r][c] not in 'X@':
        x.append((r, c))
        r += 1
    return x


def left_side(house_map, r, c):
    x = []
    while c >= 0 and house_map[r][c] not in 'X@':
        x.append((r, c))
        c -= 1
    return x


def right_side(house_map, r, c):
    x = []
    while c < len(house_map[0]) and house_map[r][c] not in 'X@':
        x.append((r, c))
        c += 1
    return x


def top_left(house_map, r, c):
    x = []
    while r >= 0 and c >= 0 and house_map[r][c] not in 'X@':
        x.append((r, c))
        r -= 1
        c -= 1
    return x


def top_right(house_map, r, c):
    x = []
    while r >= 0 and c < len(house_map[0]) and house_map[r][c] not in 'X@':
        x.append((r, c))
        r -= 1
        c += 1
    return x


def bottom_left(house_map, r, c):
    x = []
    while r < len(house_map) and c >= 0 and house_map[r][c] not in 'X@':
        x.append((r, c))
        r += 1
        c -= 1
    return x


def bottom_right(house_map, r, c):
    x = []
    while r < len(house_map) and c < len(house_map[0]) and house_map[r][c] not in 'X@':
        x.append((r, c))
        r += 1
        c += 1
    return x

# This function returns the total invalid indices.
def excluded(house_map):
    locs = get_p_locs(house_map)
    res = []
    for loc in locs:
        r = loc[0]
        c = loc[1]
        x = up_rows(house_map, r, c)
        x.extend(down_rows(house_map, r, c))
        x.extend(left_side(house_map, r, c))
        x.extend(right_side(house_map, r, c))
        x.extend(top_right(house_map, r, c))
        x.extend(bottom_right(house_map, r, c))
        x.extend(bottom_left(house_map, r, c))
        x.extend(top_left(house_map, r, c))
        x = list(set(x))
        x.pop(x.index((r, c)))
        res.extend(x)
    return list(set(res))

# Get the agent locations in the house_map
def get_p_locs(house_map):
    locs = []
    for i in range(len(house_map)):
        for j in range(len(house_map[i])):
            if house_map[i][j] == 'p':
                locs.append((i, j))
    return locs


# Get list of successors of given house_map state
def successors(house_map):
    x = excluded(house_map)
    return [add_pichu(house_map, r, c) for r in range(0, len(house_map)) for c in range(0, len(house_map[0])) if (r, c)
            not in x and house_map[r][c] == '.']


# check if house_map is a goal state
def is_goal(house_map, k):
    return count_pichus(house_map) == k


# Arrange agents on the map
#
# This function MUST take two parameters as input -- the house map and the value k --
# and return a tuple of the form (new_house_map, success), where:
# - new_house_map is a new version of the map with k agents,
# - success is True if a solution was found, and False otherwise.
#
def solve(initial_house_map, k):
    fringe = [initial_house_map]
    while len(fringe) > 0:
        for new_house_map in successors(fringe.pop()):
            if is_goal(new_house_map, k):
                return new_house_map, True
            fringe.append(new_house_map)
    return initial_house_map, k


# Main Function
if __name__ == "__main__":
    house_map = parse_map(sys.argv[1])
    # This is k, the number of agents
    k = int(sys.argv[2])
    print("Starting from initial house map:\n" + printable_house_map(house_map) + "\n\nLooking for solution...\n")
    solution = solve(house_map, k)
    print("Here's what we found:")
    if solution[0] == house_map:
        print("False")
    else:
        print(printable_house_map(solution[0]))
