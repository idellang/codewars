def is_solved(board):
    import ast

    # fix wrong data input
    try:
        board = [ast.literal_eval(innerboard) for innerboard in board[0]]
    except ValueError:
        board = board

    all_nums = [item for innerlist in board for item in innerlist]
    rows = board
    cols = [[rows[i] for rows in board] for i in range(3)]
    diag1 = [rows[i][i] for i in range(3)]
    diag2 = [rows[2 - i][i] for i in range(2, -1, -1)]

    for row in board:
        if len(set(row)) == 1 and (row[0] == 1 or row[0] == 2):
            return row[0]

    for col in cols:
        if len(set(col)) == 1 and (col[0] == 1 or col[0] == 2):
            return col[0]

    if len(set(diag1)) == 1 and (diag1[0] == 1 or diag1[0] == 2):
        return diag1[0]

    if len(set(diag2)) == 1 and (diag2[0] == 1 or diag2[0] == 2):
        return diag2[0]

    if 0 in all_nums:
        return -1
    else:
        return 0


board1 = [["[0,1,1]", "[2,0,2]", "[2,1,0]"]]
board = [[1, 1, 1], [0, 2, 2], [0, 0, 0]]
print(is_solved(board1))
# print(is_solved(board1))