#!/usr/local/bin/python3
#
# route_pichu.py : a maze solver
#
# Submitted by : [ONKAR JADHAV, ojadhav]
#
# Based on skeleton code provided in CSCI B551, Fall 2022.

import sys


# Parse the map from a given filename
def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]


# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
    return 0 <= pos[0] < n and 0 <= pos[1] < m


# Find the possible moves from position (row, col)
def moves(map, row, col):
    moves = ((row + 1, col), (row - 1, col), (row, col - 1), (row, col + 1))

    # Return only moves that are within the house_map and legal (i.e. go through open space ".")
    return [move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@")]


# Perform search on the map
#
# This function MUST take a single parameter as input -- the house map --
# and return a tuple of the form (move_count, move_string), where:
# - move_count is the number of moves required to navigate from start to finish, or -1
#    if no such route exists
# - move_string is a string indicating the path, consisting of U, L, R, and D characters
#    (for up, left, right, and down)

def search(house_map):
    # Find pichu start position
    pichu_loc = [(row_i, col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if
                 house_map[row_i][col_i] == "p"][0]

    path = ""
    cost = 0
    
    # Created a map so that it is easy to get the respective direction letter.
    direction = {(-1, 0): "U",
                 (0, 1): "R",
                 (1, 0): "D",
                 (0, -1): "L"}

    # Declare a visited set which stores the 2D indices of where the pichu has visited.
    visited = set()
    # Fringe queue to store the pichu location, path and cost.
    fringe = [(pichu_loc, path, cost)]

    while fringe:
        # Get current pichu location, path, cost
        curr, path, cost = fringe.pop(0)
        r = curr[0]
        c = curr[1]

        if (r, c) in visited:
            continue
        if house_map[r][c] == "@":
            return cost, path
        else:
            visited.add((r, c))
            for move in moves(house_map, r, c):
                # When we get the difference of next move and the current move we get its direction index.
                # From that index I have retrived the letter
                d = (move[0] - r, move[1] - c)
                fringe.append((move, path + direction[d], cost + 1))

    return -1, ""


# Main Function
if __name__ == "__main__":
    house_map = parse_map(sys.argv[1])
    # print(house_map)
    print("Shhhh... quiet while I navigate!")
    solution = search(house_map)
    print("Here's the solution I found:")
    print(str(solution[0]) + " " + solution[1])
