#
# raichu.py : Play the game of Raichu
#
# PLEASE PUT YOUR NAMES AND USER IDS HERE!
# Chinmay Pathak(crpathak), Onkar Jadhav(ojadhav), Saurabh Dete(sdete)
# Based on skeleton code by D. Crandall, Oct 2021
#
import copy
import sys
import random
from pprint import pprint


def board_to_string(board, N):
    return "\n".join(board[i:i + N] for i in range(0, len(board), N))


def white_pichu_moves(r, c, board):
    moves = []
    boards = []

    board[r][c] = '.'

    if r + 1 < len(board) and c + 1 < len(board[0]):
        if board[r + 1][c + 1] == '.':
            moves.append((r + 1, c + 1, 1))
        if board[r + 1][c + 1] == 'b':
            if r + 2 < len(board) and c + 2 < len(board[0]):
                if board[r + 2][c + 2] == '.':
                    moves.append((r + 2, c + 2, 2))

    if r + 1 < len(board) and c - 1 >= 0:
        if board[r + 1][c - 1] == '.':
            moves.append((r + 1, c - 1, 1))
        if board[r + 1][c - 1] == 'b':
            if r + 2 < len(board) and c - 2 >= 0:
                if board[r + 2][c - 2] == '.':
                    moves.append((r + 2, c - 2, 3))

    for i in list(set(moves)):
        successors_board = copy.deepcopy(board)
        if i[2] == 2:
            successors_board[i[0] - 1][i[1] - 1] = '.'
        if i[2] == 3:
            successors_board[i[0] - 1][i[1] + 1] = '.'

        if i[0] == len(board) - 1:
            successors_board[i[0]][i[1]] = '@'
        else:
            successors_board[i[0]][i[1]] = 'w'

        boards.append(successors_board)

    return boards


def black_pichu_moves(r, c, board):
    moves = []
    boards = []

    board[r][c] = '.'

    if r - 1 >= 0 and c + 1 < len(board[0]):
        if board[r - 1][c + 1] == '.':
            moves.append((r - 1, c + 1, 1))
        if board[r - 1][c + 1] == 'w':
            if r - 2 >= 0 and c + 2 < len(board[0]):
                if board[r - 2][c + 2] == '.':
                    moves.append((r - 2, c + 2, 2))

    if r - 1 >= 0 and c - 1 >= 0:
        if board[r - 1][c - 1] == '.':
            moves.append((r - 1, c - 1, 1))
        if board[r - 1][c - 1] == 'w':
            if r - 2 >= 0 and c - 2 >= 0:
                if board[r - 2][c - 2] == '.':
                    moves.append((r - 2, c - 2, 3))

    for i in list(set(moves)):

        successors_board = copy.deepcopy(board)
        if i[2] == 2:
            successors_board[i[0] + 1][i[1] - 1] = '.'
        if i[2] == 3:
            successors_board[i[0] + 1][i[1] + 1] = '.'

        if i[0] == 0:
            successors_board[i[0]][i[1]] = '$'
        else:
            successors_board[i[0]][i[1]] = 'b'

        boards.append(successors_board)

    return boards


def white_pikachu_moves(r, c, board):
    moves = []
    boards = []

    board[r][c] = '.'

    # 1 below or 2 below jump
    if r + 1 < len(board):
        if board[r + 1][c] == '.':
            moves.append((r + 1, c, 1))
        if board[r + 1][c] in 'bB':
            if r + 2 < len(board):
                if board[r + 2][c] == '.':
                    moves.append((r + 2, c, 2))
        else:
            # 2 below or 3 below jump
            if r + 1 < len(board):
                if board[r + 1][c] == '.':
                    if r + 2 < len(board):
                        if board[r + 2][c] == '.':
                            moves.append((r + 2, c, 1))
                        elif board[r + 2][c] in 'bB':
                            if r + 3 < len(board):
                                if board[r + 3][c] == '.':
                                    moves.append((r + 3, c, 2))

    # 1 left or 2 left jump
    if c - 1 >= 0:
        if board[r][c - 1] == '.':
            moves.append((r, c - 1, 1))
        if board[r][c - 1] in 'bB':
            if c - 2 >= 0:
                if board[r][c - 2] == '.':
                    moves.append((r, c - 2, 3))
        else:
            # 2 left or 3 left jump
            if c - 1 >= 0:
                if board[r][c - 1] == '.':
                    if c - 2 >= 0:
                        if board[r][c - 2] == '.':
                            moves.append((r, c - 2, 1))
                        elif board[r][c - 2] in 'bB':
                            if c - 3 >= 0:
                                if board[r][c - 3] == '.':
                                    moves.append((r, c - 3, 3))

    # 1 right or 2 right jump
    if c + 1 < len(board[0]):
        if board[r][c + 1] == '.':
            moves.append((r, c + 1, 1))
        if board[r][c + 1] in 'bB':
            if c + 2 < len(board[0]):
                if board[r][c + 2] == '.':
                    moves.append((r, c + 2, 4))
        else:
            # 2 right or 3 right jump
            if c + 1 < len(board[0]):
                if board[r][c + 1] == '.':
                    if c + 2 < len(board[0]):
                        if board[r][c + 2] == '.':
                            moves.append((r, c + 2, 1))
                        elif board[r][c + 2] in 'bB':
                            if c + 3 < len(board[0]):
                                if board[r][c + 3] == '.':
                                    moves.append((r, c + 3, 4))

    # --------------------------------------------------

    for i in list(set(moves)):
        successors_board = copy.deepcopy(board)
        if i[2] == 2:
            successors_board[i[0] - 1][i[1]] = '.'
        if i[2] == 3:
            successors_board[i[0]][i[1] + 1] = '.'
        if i[2] == 4:
            successors_board[i[0]][i[1] - 1] = '.'

        if i[0] == len(board) - 1:
            successors_board[i[0]][i[1]] = '@'
        else:
            successors_board[i[0]][i[1]] = 'W'

        boards.append(successors_board)

    return boards


def black_pikachu_moves(r, c, board):
    moves = []
    boards = []

    board[r][c] = '.'

    # 1 below or 2 below jump
    if r - 1 >= 0:
        if board[r - 1][c] == '.':
            moves.append((r - 1, c, 1))
        if board[r - 1][c] in 'wW':
            if r - 2 >= 0:
                if board[r - 2][c] == '.':
                    moves.append((r - 2, c, 2))
        else:
            # 2 below or 3 below jump
            if r - 1 >= 0:
                if board[r - 1][c] == '.':
                    if r - 2 >= 0:
                        if board[r - 2][c] == '.':
                            moves.append((r - 2, c, 1))
                        elif board[r - 2][c] in 'wW':
                            if r - 3 < len(board):
                                if board[r - 3][c] == '.':
                                    moves.append((r - 3, c, 2))

    # 1 left or 2 left jump
    if c - 1 >= 0:
        if board[r][c - 1] == '.':
            moves.append((r, c - 1, 1))
        if board[r][c - 1] in 'wW':
            if c - 2 >= 0:
                if board[r][c - 2] == '.':
                    moves.append((r, c - 2, 3))
        else:
            # 2 left or 3 left jump
            if c - 1 >= 0:
                if board[r][c - 1] == '.':
                    if c - 2 >= 0:
                        if board[r][c - 2] == '.':
                            moves.append((r, c - 2, 1))
                        elif board[r][c - 2] in 'wW':
                            if c - 3 >= 0:
                                if board[r][c - 3] == '.':
                                    moves.append((r, c - 3, 3))

    # 1 right or 2 right jump
    if c + 1 < len(board[0]):
        if board[r][c + 1] == '.':
            moves.append((r, c + 1, 1))
        if board[r][c + 1] in 'wW':
            if c + 2 < len(board[0]):
                if board[r][c + 2] == '.':
                    moves.append((r, c + 2, 4))
        else:
            # 2 right or 3 right jump
            if c + 1 < len(board[0]):
                if board[r][c + 1] == '.':
                    if c + 2 < len(board[0]):
                        if board[r][c + 2] == '.':
                            moves.append((r, c + 2, 1))
                        elif board[r][c + 2] in 'wW':
                            if c + 3 < len(board[0]):
                                if board[r][c + 3] == '.':
                                    moves.append((r, c + 3, 4))

    # --------------------------------------------------

    for i in list(set(moves)):
        successors_board = copy.deepcopy(board)
        if i[2] == 2:
            successors_board[i[0] - 1][i[1]] = '.'
        if i[2] == 3:
            successors_board[i[0]][i[1] + 1] = '.'
        if i[2] == 4:
            successors_board[i[0]][i[1] - 1] = '.'
        if i[0] == 0:
            successors_board[i[0]][i[1]] = '$'
        else:
            successors_board[i[0]][i[1]] = 'B'

        boards.append(successors_board)

    return boards


def white_raichu_moves(r, c, board):
    boards = []
    possible_moves = []
    exec_map = {}
    board[r][c] = '.'

    # move up till . jump if opponent
    r_ = r
    total_jumps = 0
    coeff = 1
    ex_r = ex_c = 0
    while r_ >= 0:
        if board[r_][c] in "wW@":
            break
        if board[r_][c] in "bB$":
            total_jumps += 1
            if total_jumps == 2:
                break
            ex_r = r_
            ex_c = c
            coeff = 2
        else:
            if r_ != r:
                if coeff == 2:
                    exec_map[(r_, c)] = (ex_r, ex_c)
                possible_moves.append((r_, c, coeff))
        r_ -= 1

    # move down till . jump if opponent
    r_ = r
    total_jumps = 0
    coeff = 1
    ex_r = ex_c = 0
    while r_ < len(board):
        if board[r_][c] in "wW@":
            break
        if board[r_][c] in "bB$":
            total_jumps += 1
            if total_jumps == 2:
                break
            ex_r = r_
            ex_c = c
            coeff = 2
        else:
            if r_ != r:
                if coeff == 2:
                    exec_map[(r_, c)] = (ex_r, ex_c)
                possible_moves.append((r_, c, coeff))
        r_ += 1

    # move left till . jump if opponent
    c_ = c
    ex_r = ex_c = 0
    coeff = 1
    total_jumps = 0
    while c_ >= 0:
        if board[r][c_] in "wW@":
            break
        if board[r][c_] in "bB$":
            total_jumps += 1
            if total_jumps == 2:
                break
            ex_r = r
            ex_c = c_
            coeff = 2
        else:
            if c_ != c:
                if coeff == 2:
                    exec_map[(r, c_)] = (ex_r, ex_c)
                possible_moves.append((r, c_, coeff))
        c_ -= 1

    # move right till . jump if opponent
    c_ = c
    ex_r = ex_c = 0
    coeff = 1
    total_jumps = 0
    while c_ < len(board[0]):
        if board[r][c_] in "wW@":
            break
        if board[r][c_] in "bB$":
            total_jumps += 1
            if total_jumps == 2:
                break
            ex_r = r
            ex_c = c_
            coeff = 2
        else:
            if c_ != c:
                if coeff == 2:
                    exec_map[(r, c_)] = (ex_r, ex_c)
                possible_moves.append((r, c_, coeff))
        c_ += 1

    # move top left till . jump if opponent
    r_ = r
    c_ = c
    ex_r = ex_c = 0
    coeff = 1
    total_jumps = 0
    while r_ >= 0 and c_ >= 0:
        if board[r_][c_] in "wW@":
            break
        if board[r_][c_] in "bB$":
            total_jumps += 1
            if total_jumps == 2:
                break
            ex_r = r_
            ex_c = c_
            coeff = 2
        else:
            if r_ != r and c_ != c:
                if coeff == 2:
                    exec_map[(r_, c_)] = (ex_r, ex_c)
                possible_moves.append((r_, c_, coeff))
        r_ -= 1
        c_ -= 1

    # move bottom right till . jump if opponent
    r_ = r
    c_ = c
    ex_r = ex_c = 0
    coeff = 1
    total_jumps = 0
    while r_ < len(board) and c_ < len(board[0]):
        if board[r_][c_] in "wW@":
            break
        if board[r_][c_] in "bB$":
            total_jumps += 1
            if total_jumps == 2:
                break
            ex_r = r_
            ex_c = c_
            coeff = 2
        else:
            if r_ != r and c_ != c:
                if coeff == 2:
                    exec_map[(r_, c_)] = (ex_r, ex_c)
                possible_moves.append((r_, c_, coeff))
        r_ += 1
        c_ += 1

    # move bottom left till . jump if opponent
    r_ = r
    c_ = c
    ex_r = ex_c = 0
    coeff = 1
    total_jumps = 0
    while r_ < len(board) and c_ >= 0:
        if board[r_][c_] in "wW@":
            break
        if board[r_][c_] in "bB$":
            total_jumps += 1
            if total_jumps == 2:
                break
            ex_r = r_
            ex_c = c_
            coeff = 2
        else:
            if r_ != r and c_ != c:
                if coeff == 2:
                    exec_map[(r_, c_)] = (ex_r, ex_c)
                possible_moves.append((r_, c_, coeff))
        r_ += 1
        c_ -= 1

    # move top right till . jump if opponent
    r_ = r
    c_ = c
    ex_r = ex_c = 0
    coeff = 1
    total_jumps = 0
    while r_ >= 0 and c_ < len(board[0]):
        if board[r_][c_] in "wW@":
            break
        if board[r_][c_] in "bB$":
            total_jumps += 1
            if total_jumps == 2:
                break
            ex_r = r_
            ex_c = c_
            coeff = 2
        else:
            if r_ != r and c_ != c:
                if coeff == 2:
                    exec_map[(r_, c_)] = (ex_r, ex_c)
                possible_moves.append((r_, c_, coeff))
        r_ -= 1
        c_ += 1

    for move in possible_moves:
        successors_board = copy.deepcopy(board)
        if move[2] == 1:
            successors_board[move[0]][move[1]] = "@"
        if move[2] == 2:
            ex_r, ex_c = exec_map[(move[0], move[1])]
            successors_board[ex_r][ex_c] = "."
            successors_board[move[0]][move[1]] = "@"
        boards.append(successors_board)

    return boards


def black_raichu_moves(r, c, board):
    boards = []
    possible_moves = []
    exec_map = {}
    board[r][c] = '.'

    # move up till . jump if opponent
    r_ = r
    total_jumps = 0
    coeff = 1
    ex_r = ex_c = 0
    while r_ >= 0:
        if board[r_][c] in "bB$":
            break
        if board[r_][c] in "wW@":
            total_jumps += 1
            if total_jumps == 2:
                break
            ex_r = r_
            ex_c = c
            coeff = 2
        else:
            if r_ != r:
                if coeff == 2:
                    exec_map[(r_, c)] = (ex_r, ex_c)
                possible_moves.append((r_, c, coeff))
        r_ -= 1

    # move down till . jump if opponent
    r_ = r
    total_jumps = 0
    coeff = 1
    ex_r = ex_c = 0
    while r_ < len(board):
        if board[r_][c] in "bB$":
            break
        if board[r_][c] in "wW@":
            total_jumps += 1
            if total_jumps == 2:
                break
            ex_r = r_
            ex_c = c
            coeff = 2
        else:
            if r_ != r:
                if coeff == 2:
                    exec_map[(r_, c)] = (ex_r, ex_c)
                possible_moves.append((r_, c, coeff))
        r_ += 1

    # move left till . jump if opponent
    c_ = c
    ex_r = ex_c = 0
    coeff = 1
    total_jumps = 0
    while c_ >= 0:
        if board[r][c_] in "bB$":
            break
        if board[r][c_] in "wW@":
            total_jumps += 1
            if total_jumps == 2:
                break
            ex_r = r
            ex_c = c_
            coeff = 2
        else:
            if c_ != c:
                if coeff == 2:
                    exec_map[(r, c_)] = (ex_r, ex_c)
                possible_moves.append((r, c_, coeff))
        c_ -= 1

    # move right till . jump if opponent
    c_ = c
    ex_r = ex_c = 0
    coeff = 1
    total_jumps = 0
    while c_ < len(board[0]):
        if board[r][c_] in "bB$":
            break
        if board[r][c_] in "wW@":
            total_jumps += 1
            if total_jumps == 2:
                break
            ex_r = r
            ex_c = c_
            coeff = 2
        else:
            if c_ != c:
                if coeff == 2:
                    exec_map[(r, c_)] = (ex_r, ex_c)
                possible_moves.append((r, c_, coeff))
        c_ += 1

    # move top left till . jump if opponent
    r_ = r
    c_ = c
    ex_r = ex_c = 0
    coeff = 1
    total_jumps = 0
    while r_ >= 0 and c_ >= 0:
        if board[r_][c_] in "bB$":
            break
        if board[r_][c_] in "wW@":
            total_jumps += 1
            if total_jumps == 2:
                break
            ex_r = r_
            ex_c = c_
            coeff = 2
        else:
            if r_ != r and c_ != c:
                if coeff == 2:
                    exec_map[(r_, c_)] = (ex_r, ex_c)
                possible_moves.append((r_, c_, coeff))
        r_ -= 1
        c_ -= 1

    # move bottom right till . jump if opponent
    r_ = r
    c_ = c
    ex_r = ex_c = 0
    coeff = 1
    total_jumps = 0
    while r_ < len(board) and c_ < len(board[0]):
        if board[r_][c_] in "bB$":
            break
        if board[r_][c_] in "wW@":
            total_jumps += 1
            if total_jumps == 2:
                break
            ex_r = r_
            ex_c = c_
            coeff = 2
        else:
            if r_ != r and c_ != c:
                if coeff == 2:
                    exec_map[(r_, c_)] = (ex_r, ex_c)
                possible_moves.append((r_, c_, coeff))
        r_ += 1
        c_ += 1

    # move bottom left till . jump if opponent
    r_ = r
    c_ = c
    ex_r = ex_c = 0
    coeff = 1
    total_jumps = 0
    while r_ < len(board) and c_ >= 0:
        if board[r_][c_] in "bB$":
            break
        if board[r_][c_] in "wW@":
            total_jumps += 1
            if total_jumps == 2:
                break
            ex_r = r_
            ex_c = c_
            coeff = 2
        else:
            if r_ != r and c_ != c:
                if coeff == 2:
                    exec_map[(r_, c_)] = (ex_r, ex_c)
                possible_moves.append((r_, c_, coeff))
        r_ += 1
        c_ -= 1

    # move top right till . jump if opponent
    r_ = r
    c_ = c
    ex_r = ex_c = 0
    coeff = 1
    total_jumps = 0
    while r_ >= 0 and c_ < len(board[0]):
        if board[r_][c_] in "bB$":
            break
        if board[r_][c_] in "wW@":
            total_jumps += 1
            if total_jumps == 2:
                break
            ex_r = r_
            ex_c = c_
            coeff = 2
        else:
            if r_ != r and c_ != c:
                if coeff == 2:
                    exec_map[(r_, c_)] = (ex_r, ex_c)
                possible_moves.append((r_, c_, coeff))
        r_ -= 1
        c_ += 1

    for move in possible_moves:
        successors_board = copy.deepcopy(board)
        if move[2] == 1:
            successors_board[move[0]][move[1]] = "$"
        if move[2] == 2:
            ex_r, ex_c = exec_map[(move[0], move[1])]
            successors_board[ex_r][ex_c] = "."
            successors_board[move[0]][move[1]] = "$"
        boards.append(successors_board)

    return boards


def white_successors_board(board):
    res = []

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'w':
                board_ = copy.deepcopy(board)
                res += white_pichu_moves(i, j, board_)
            if board[i][j] == 'W':
                board_ = copy.deepcopy(board)
                res += white_pikachu_moves(i, j, board_)
            if board[i][j] == '@':
                board_ = copy.deepcopy(board)
                res += white_raichu_moves(i, j, board_)

    return res


def black_successors_board(board):
    res = []

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'b':
                board_ = copy.deepcopy(board)
                res += black_pichu_moves(i, j, board_)
            if board[i][j] == 'B':
                board_ = copy.deepcopy(board)
                res += black_pikachu_moves(i, j, board_)
            if board[i][j] == '$':
                board_ = copy.deepcopy(board)
                res += black_raichu_moves(i, j, board_)

    return res


def successors(board, player):
    if player.lower() == "w":
        return white_successors_board(board)
    elif player.lower() == "b":
        return black_successors_board(board)
    else:
        raise Exception("Wrong player passed")


def check_win(board, player):
    board_ = to_string(board)
    if player.lower() == 'w':
        return "b" not in board_ and "B" not in board_ and "$" not in board_
    if player.lower() == 'b':
        return "w" not in board_ and "W" not in board_ and "@" not in board_


def h(board, player):
    c = 0
    if player.lower() == 'w':
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "w":
                    c += 2
                if board[i][j] == "W":
                    c += 4
                if board[i][j] == "@":
                    c += 16
                if board[i][j] == "b":
                    c -= 1
                if board[i][j] == "B":
                    c -= 2
                if board[i][j] == "$":
                    c -= 8

    if player.lower() == 'b':
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "b":
                    c += 2
                if board[i][j] == "B":
                    c += 4
                if board[i][j] == "$":
                    c += 16
                if board[i][j] == "w":
                    c -= 1
                if board[i][j] == "W":
                    c -= 2
                if board[i][j] == "@":
                    c -= 8

    return c


def count_board(board, player):
    c = 0
    c_w = 0
    c_b = 0
    b = to_string(board)
    if player.lower() == 'w':

        c_w += b.count("w")
        c_w += b.count("W") * 2
        c_w += b.count("@") * 4

        c_b += b.count("b")
        c_b += b.count("B") * 2
        c_b += b.count("$") * 4
        c = min(c_w, c_b)

    if player.lower() == 'b':
        c_b += b.count("b")
        c_b += b.count("B") * 2
        c_b += b.count("$") * 4
        c_w += b.count("w")
        c_w += b.count("W") * 2
        c_w += b.count("@") * 4
        c = min(c_w, c_b)

    if c < 8:
        return 1
    if c in range(8, 12):
        return 3
    else:
        return 4


def minmax_decision_white(board, player):
    val = float("-inf")
    b_ = []
    for s in successors(board, player):
        d = count_board(board, player)
        new_val = min_value_white(s, d, float("-inf"), float("inf"))
        if new_val >= val:
            val = new_val
            b_ = s

    return b_


def min_value_white(board, depth, alpha, beta):
    if depth == 0 or check_win(board, "w"):
        return h(board, "w")
    else:
        for s in successors(board, "b"):
            beta = min(beta, max_value_white(s, depth - 1, alpha, beta))
            if alpha <= beta:
                return beta
        return beta


def max_value_white(board, depth, alpha, beta):
    if depth == 0 or check_win(board, "w"):
        return h(board, "w")
    else:
        for s in successors(board, "w"):
            alpha = max(alpha, min_value_white(s, depth - 1, alpha, beta))
            if beta <= alpha:
                return alpha
        return alpha


def minmax_decision_black(board, player):
    val = float("-inf")
    b_ = []
    for s in successors(board, player):
        d = count_board(board, player)
        new_val = min_value_white(s, d, float("-inf"), float("inf"))
        if new_val >= val:
            val = new_val
            b_ = s

    return b_


def min_value_black(board, depth, alpha, beta):
    if depth == 0 or check_win(board, "b"):
        return h(board, "b")
    else:
        for s in successors(board, "w"):
            beta = min(beta, max_value_white(s, depth - 1, alpha, beta))
            if alpha <= beta:
                return beta
        return beta


def max_value_black(board, depth, alpha, beta):
    if depth == 0 or check_win(board, "b"):
        return h(board, "b")
    else:
        for s in successors(board, "b"):
            alpha = max(alpha, min_value_white(s, depth - 1, alpha, beta))
            if beta <= alpha:
                return alpha
        return alpha


def to_matrix(board, N):
    start = 0
    end = N
    res = []
    while end <= N * N:
        res.append([i for i in board[start:end]])
        start = end
        end = end + N

    return res


def to_string(board):
    s = ""
    for i in board:
        for j in i:
            s += j
    return s


def find_best_move(board, N, player, timelimit):
    # This sample code just returns the same board over and over again (which
    # isn't a valid move anyway.) Replace this with your code!
    #
    b = to_matrix(board, N)

    while True:
        # if i % 2 == 0:
        #     print("W PLAYS!!!!")
        #     b = minmax_decision_white(b, "w")
        #     yield board_to_string(to_string(b), 8)
        # if i % 2 == 1:
        #     print("B PLAYS!!!")
        #     b = minmax_decision_black(b, "b")
        #     yield board_to_string(to_string(b), 8)
        # print("-----------------------------------------")
        # if check_win(b, "w"):
        #     print("WHITE!!!!")
        #     break
        # elif check_win(b, "b"):
        #     print("BLACK!!!!")
        # i += 1
        # if i == 10:
        #     i = 0
        if player.lower() == "w":
            b = minmax_decision_white(b, player)
        elif player.lower() == "b":
            b = minmax_decision_black(b, player)
        yield to_string(b)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        raise Exception("Usage: Raichu.py N player board timelimit")

    (_, N, player, board, timelimit) = sys.argv
    N = int(N)
    timelimit = int(timelimit)
    if player not in "wb":
        raise Exception("Invalid player.")

    if len(board) != N * N or 0 in [c in "wb.WB@$" for c in board]:
        raise Exception("Bad board string.")

    print("Searching for best move for " + player + " from board state: \n" + board_to_string(board, N))
    print("Here's what I decided:")
    for new_board in find_best_move(board, N, player, timelimit):
        print(new_board)
