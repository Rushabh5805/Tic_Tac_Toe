player = 'x'
opponent = 'o'


def move_left(board):
    for i in range(len(board)):
        if board[i] == '*':
            return True
    return False


def score(board, depth):
    win_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    for i, j, k in win_positions:
        if board[i] == board[j] == board[k] and board[i] != '*':
            if board[i] == player:
                return 10
            elif board[i] == opponent:
                return -10
    return 0


def minimax(board, depth, isMax):
    scores = score(board, depth)

    if scores == 10:
        return depth - scores

    if scores == -10:
        return scores - depth

    if move_left(board) == False:
        return 0

    if isMax:
        best = -1000

        for i in range(len(board)):
            if board[i] == '*':
                board[i] = player
                temp = minimax(board, depth + 1, isMax=(~isMax))
                best = max(temp, best)
                board[i] = '*'
        return best

    else:
        best = 1000

        for i in range(len(board)):
            if board[i] == '*':
                board[i] = opponent
                temp = minimax(board, depth + 1, isMax=(~isMax))
                best = min(temp, best)
                board[i] = '*'
        return best


def findbestmove(board, play, depth):
    index = -1

    if play == player:
        bestval = -1000
        for i in range(len(board)):
            if board[i] == '*':
                board[i] = player
                moveval = minimax(board, depth, isMax=False)
                board[i] = '*'
                if moveval > bestval:
                    index = i
                    bestval = moveval

    else:
        bestval = 1000
        for i in range(len(board)):
            if board[i] == '*':
                board[i] = opponent
                moveval = minimax(board, depth, isMax=True)
                board[i] = '*'
                if moveval < bestval:
                    index = i
                    bestval = moveval
    return index


def print_board(board):
    for j in range(0, 9, 3):
        for i in range(3):
            if board[j + i] == '*':
                print("*", end='')
            else:
                print("%s " % board[j + i], end='')

        print("\n")
    print("\n")

from random import randint

rand = randint(0, 8)
player = 'x'
opponent = 'o'
board = ['*', '*', '*', '*', '*', '*', '*', '*', '*']
board[rand] = player
depth = 0
play = 0
print_board(board)
# rand = findbestmove(board,play = opponent,depth=depth)
# board[rand] = opponent
# print_board(board)

# rand = findbestmove(board,play = opponent,depth=depth)
# board[rand] = opponent
# print_board(board)
flag = 0

for i in range(8):
    if play % 2 == 0:
        rand = findbestmove(board, play=opponent, depth=depth)
        board[rand] = opponent
        print_board(board)
        ans = score(board, depth)
        if ans == 10:
            print('Result: X Wins!')
            flag = 1
            break

        if ans == -10:
            print('Result: O Wins!')
            flag = 1
            break
        play += 1
        depth += 1

    else:
        rand = findbestmove(board, play=player, depth=depth)
        board[rand] = player
        print_board(board)
        ans = score(board, depth)
        if ans == 10:
            print('Result: X Wins!')
            flag = 1
            break

        if ans == -10:
            print('Result: O Wins!')
            flag = 1
            break
        play += 1
        depth += 1

if flag == 0:
    print('Draw Game')
