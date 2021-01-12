def analyzer(board: list):
    # wining combos
    combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6], [1, 4, 7],
              [0, 3, 6], [2, 5, 8]]
    for i in range(0, len(combos)):
        if (board[combos[i][0]] != 0
                and  # board[index] value will be either 1 or -1
                board[combos[i][0]] == board[combos[i][1]] and
                board[combos[i][0]] == board[combos[i][2]]):
            return board[combos[i][0]]
    return 0


def minmax(board: list, player: int):
    x = analyzer(board)
    if x != 0:
        return x * player
    pos = -1
    value = -2
    for i in range(0, len(board)):
        if board[i] == 0:
            board[i] = player
            score = -minmax(board, (player * -1))
            if score > value:
                value = score
                pos = i
            board[i] = 0
    if pos == -1:
        return 0
    return value


def computeBotTurn(board: list):
    pos = -1
    value = -2

    for i in range(0, len(board)):
        if board[i] == 0:
            board[i] = 1  #1 is for computer -1 for user
            score = -minmax(board, -1)
            board[i] = 0
            if score > value:
                value = score
                pos = i
    return pos