import random


def score(board, depth):
    win_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    for i, j, k in win_positions:
        if board[i] == board[j] == board[k] and board[i] != '*':
            if board[i] == player:
                return 10
            elif board[i] == opponent:
                return -10
    return 0


def imin(board, depth):
    scores = score(board, depth)

    if scores == 10:
        return depth - scores

    if scores == -10:
        return scores - depth

    for i in range(len(board)):
        if board[i] == '*':
            r = True
        r = False

    if r == False:
        return 0
    else:
        best = 1000

        for i in range(len(board)):
            if board[i] == '*':
                board[i] = opponent
                temp = imax(board, depth + 1)
                best = min(temp, best)
                board[i] = '*'
        return best


def imax(board, depth):
    scores = score(board, depth)

    if scores == 10:
        return scores

    if scores == -10:
        return scores

    for i in range(len(board)):
        if board[i] == '*':
            r = True
        r = False

    if r == False:
        return 0

    else:
        best = -1000

        for i in range(len(board)):
            if board[i] == '*':
                board[i] = player
                temp = imin(board, depth + 1)
                best = max(temp, best)
                board[i] = '*'
        return best

def findbestmove(board, play, depth):
    index = -1

    if play == player:
        bestval = -1000
        for i in range(len(board)):
            if board[i] == '*':
                board[i] = player
                moveval = imax(board, depth)
                board[i] = '*'
                if moveval > bestval:
                    index = i
                    bestval = moveval

    else:
        bestval = 1000
        for i in range(len(board)):
            if board[i] == '*':
                board[i] = opponent
                moveval = imin(board, depth)
                board[i] = '*'
                if moveval < bestval:
                    index = i
                    bestval = moveval
    return index


def print_board(board):
    for j in range(0, 9, 3):
        for i in range(3):
            if board[j + i] == '*':
                print("* ", end='')
            else:
                print("%s " % board[j + i], end='')

        print("\n")
    print("\n")


def initial_step(depth, flag):
    for i in range(8):
        if i % 2 == 0:
            x = opponent
        else:
            x = player

        rand = findbestmove(board, play=x, depth=depth)
        board[rand] = x
        print_board(board)
        ans = score(board, depth)
        if ans == 10:
            print('Player X Wins!')
            flag = 1
            break

        if ans == -10:
            print('Player O Wins!')
            flag = 1
            break
        depth += 1

    if flag == 0:
        print('Draw Game')


rand = random.randint(0, 8)
player = 'x'
opponent = 'o'
board = ['*', '*', '*', '*', '*', '*', '*', '*', '*']
board[rand] = player
depth = 0
play = 0
print_board(board)
flag = 0
initial_step(depth, flag)