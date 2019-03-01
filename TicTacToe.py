import random


def score(board):
    win_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    for combo in win_positions:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] == player:
            return 10
        elif board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] == opponent:
            return -10
    return 0


def check_temp(play, temp, best):
    if play == player:
        best = max(temp, best)
    else:
        best = min(temp, best)
    return best


def minimax(board, depth, isMax):
    scores = score(board)
    # print(scores)
    if scores != 0:
        return scores

    for i in range(len(board)):
        if board[i] == '*':
            r = True
            break
        r = False

    if r == False:
        return 0

    if isMax:
        best = -1000
        play = player

    else:
        best = 1000
        play = opponent

    for i in range(len(board)):
        if board[i] == '*':
            board[i] = play
            temp = minimax(board, depth + 1, ~isMax)
            best = check_temp(play, temp, best)
            board[i] = '*'
    return best


def mid_comp(play, moveval, bestval):
    if play == player:
        if moveval > bestval:
            return True
    else:
        if moveval < bestval:
            return True


def check_minmax(board, play, depth):
    index = -1

    if play == player:
        bestval = -1000
        t = False

    else:
        bestval = 1000
        t = True

    for i in range(len(board)):
        if board[i] == '*':
            board[i] = play
            moveval = minimax(board, depth, t)
            board[i] = '*'
            if mid_comp(play, moveval, bestval):
                index = i
                bestval = moveval

    return index


def get_result(board):
    for j in range(0, 9):
        if board[j] == '*':
            print("* ", end='')
        else:
            print("%s " % board[j], end='')
        if (j + 1) % 3 == 0:
            print("\n")
    print("\n")


def initial_step(depth):
    flag = 0
    for i in range(8):
        if i % 2 == 0:
            x = opponent
        else:
            x = player

        rand = check_minmax(board, play=x, depth=depth)
        board[rand] = x
        get_result(board)
        ans = score(board)
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
board = [None] * 9
for i in range(0, 9):
    board[i] = '*'
board[rand] = player
depth = 0
get_result(board)
initial_step(depth)
