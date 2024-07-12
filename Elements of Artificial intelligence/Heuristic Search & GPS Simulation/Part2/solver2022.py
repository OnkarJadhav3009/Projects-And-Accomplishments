#!/usr/local/bin/python3
# solver2022.py : 2022 Sliding tile puzzle solver
#
# Code by: Onkar Jadhav ojadhav, Sai Teja Burla saburla, Maitreya Kanitkar mkanitka
#
# Based on skeleton code by D. Crandall & B551 Staff, Fall 2022
#

import sys
from queue import PriorityQueue

ROWS = 5
COLS = 5


def printable_board(board):
    return ['%3d ' * COLS % board[j:(j + COLS)] for j in range(0, ROWS * COLS, COLS)]


def left_movement(matrix, row):
    m = matrix
    m = m[:row] + [m[row][1:] + [m[row][0]]] + m[row + 1:]
    return m


def right_movement(matrix, row):
    m = matrix
    m = m[:row] + [[m[row][-1]] + m[row][0:-1]] + m[row + 1:]
    return m


def transpose_matrix(m):
    tm = []
    for i in range(len(m[0])):
        temp = []
        for j in m:
            temp.append(j[i])
        tm.append(temp)
    return tm


def up_movement(matrix, column):
    m = matrix
    tm = transpose_matrix(m)
    tm = left_movement(tm, column)
    m = transpose_matrix(tm)
    return m


def down_movement(matrix, column):
    m = matrix
    tm = transpose_matrix(m)
    tm = right_movement(tm, column)
    m = transpose_matrix(tm)
    return m


def clockwise(matrix):
    m = matrix
    m = right_movement(m, 0)
    m = up_movement(m, 0)
    m = left_movement(m, len(m) - 1)
    m = down_movement(m, len(m) - 1)

    m[0][-1], m[1][-1] = m[1][-1], m[0][-1]

    return m


def counter_clockwise(matrix):
    m = matrix
    m = left_movement(m, 0)
    m = up_movement(m, len(m) - 1)
    m = right_movement(m, len(m) - 1)
    m = down_movement(m, 0)

    m[0][0], m[1][0] = m[1][0], m[0][0]

    return m


def inner_rotate(matrix, type_):
    mm = matrix

    m = []
    for i in range(1, len(mm) - 1):  # Get the inner matrix
        m.append(mm[i][1:-1])

    if type_ == "c":
        m = clockwise(m)
    else:
        m = counter_clockwise(m)

    t = []
    for i in range(1, len(mm) - 1):
        t.append([mm[i][0]] + m[i - 1] + [mm[i][-1]])

    mm = mm[:1] + t + mm[-1:]

    return mm


# return a list of possible successor states
def successors(state):
    res = []

    for i in range(ROWS):
        res.append((left_movement(state, i), "L" + str(i + 1)))
        res.append((right_movement(state, i), "R" + str(i + 1)))

    for i in range(COLS):
        res.append((up_movement(state, i), "U" + str(i + 1)))
        res.append((down_movement(state, i), "D" + str(i + 1)))

    res.append((inner_rotate(state, "cc"), "Icc"))
    res.append((inner_rotate(state, "c"), "Ic"))
    res.append((counter_clockwise(state), "Occ"))
    res.append((clockwise(state), "Oc"))

    return res


# Heuristic function that returns the manhattan distance.
def h(state):
    d = {}
    e = 1
    # Create a dictionary for the goal state : element -> [row, column]
    for i in range(ROWS):
        for j in range(COLS):
            d[e] = (i, j)
            e += 1

    def manhattan(x1, y1, x2, y2):
        return abs(x2 - x1) + abs(y2 - y1)

    # Sum of Manhattan distances
    m_sum = 1
    for i in range(ROWS):
        for j in range(COLS):
            m_sum += manhattan(i, j, d[state[i][j]][0], d[state[i][j]][1])

    return m_sum


# check if we've reached the goal
def is_goal(state):
    return to_single_list(state) == sorted(to_single_list(state))


def to_matrix(state):
    start = 0
    end = ROWS
    res = []
    while end <= ROWS * COLS:
        res.append(list(state[start:end]))
        start = end
        end = end + COLS

    return res


def to_single_list(state):
    res = []
    for i in state:
        res.extend(i)

    return res


def solve(initial_board):
    """
    1. This function should return the solution as instructed in assignment, consisting of a list of moves like [
    "R2","D2","U1"]. 2. Do not add any extra parameters to solve() function, or it will break our grading and
    testing code. For testing, we will call this function with single argument(initial_board) and it should return the
    solution. 3. Please do not use any global variables, as it may cause the testing code to fail. 4. You can assume
    that all test cases will be solvable. 5. The current code just returns a dummy solution.
    """
    initial_board = to_matrix(initial_board)
    fringe = PriorityQueue()
    path = []
    cost = 0
    visited = set()
    fn = h(initial_board) + cost

    valid_moves = []
    for i in range(ROWS):
        valid_moves.append("L" + str(i + 1))
        valid_moves.append("R" + str(i + 1))
    for i in range(COLS):
        valid_moves.append("U" + str(i + 1))
        valid_moves.append("D" + str(i + 1))
    valid_moves += ["Occ", "Oc", "Icc", "Ic"]

    fringe.put((fn, initial_board, path, cost))

    while fringe.qsize() > 0:
        fn, state, path, cost = fringe.get()

        if is_goal(state):
            return path

        if tuple(to_single_list(state)) in visited:
            continue

        else:
            divisor = 0
            visited.add(tuple(to_single_list(state)))
            for (next_state, move) in successors(state):
                # !!! Trick to get the optimal number of moves
                # --if the move is L, R, U or D, then the obtained heuristic has to be divided by number of cols or rows
                # = 5 tiles as 5 tiles are moved in the operation.

                # --if the move is one of the outer rotations, the obtained heuristic has to be divided by number of
                # elements contributing in the operation = ((ROWS + COLS) * 2) - 4 = (5 + 5) x 2 - 4 = 16

                # --if the move is one of the inner rotations, the obtained heuristic has to be divided by number of
                # elements contributing in the operation = ((ROWS + COLS - 4) * 2) - 4 = (5 + 5 - 4) x 2 - 4 = 12 - 4
                # = 8
                if move in valid_moves[:ROWS * 2]:
                    divisor = ROWS
                if move in valid_moves[ROWS * 2:COLS * 4]:
                    divisor = COLS
                if move in valid_moves[COLS * 4:COLS * 4 + 2]:
                    divisor = ((ROWS + COLS) * 2) - 4
                if move in valid_moves[COLS * 4 + 2:]:
                    divisor = ((ROWS + COLS - 4) * 2) - 4

                if divisor == 0:
                    divisor = 1

                fn = h(next_state) / divisor + cost + 1
                fringe.put((fn, next_state, path + [move], cost + 1))

    return []


# Please don't modify anything below this line
#
if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise (Exception("Error: expected a board filename"))

    start_state = []
    with open(sys.argv[1], 'r') as file:
        for line in file:
            start_state += [int(i) for i in line.split()]

    if len(start_state) != ROWS * COLS:
        raise (Exception("Error: couldn't parse start state file"))

    print("Start state: \n" + "\n".join(printable_board(tuple(start_state))))

    print("Solving...")
    route = solve(tuple(start_state))

    print("Solution found in " + str(len(route)) + " moves:" + "\n" + " ".join(route))
