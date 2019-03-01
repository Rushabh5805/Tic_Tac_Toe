board = ['*', '*', '*', '*', '*', '*', '*', '*', '*']

for j in range(0, 9):
        if board[j] == '*':
            print("*", end='')
        else:
            print("%s " % board[j], end='')
        if((j+1)%3==0):
            print("\n")
print("\n")