from random import randint


def draw_grid(nest):
    print("---------")
    for i in nest:
        print(f"| {' '.join(i)} |")
    print("---------")


def decide(x_wins1, x_wins2, x_wins3, o_wins1, o_wins_2, o_wins3):
    global cells_nest
    for i in cells_nest:
        if i == ['X', 'X', "X"]:
            print("X wins")
            return "X wins"
        elif i == ['O', "O", "O"]:
            print("O wins")
            return "O wins"
    else:
        if any(x_wins1) or any(x_wins2) or any(x_wins3):
            print("X wins")
        elif any(o_wins1) or any(o_wins_2) or any(o_wins3):
            print("O wins")
    for i in cells_nest:
        for j in i:
            if j == ' ':
                return " "
    return


def get_coord(nest):
    li = []
    try:
        li[0:2] = list(map(int, input("Enter the coordinates: ").split()))
    except ValueError:
        print("You should enter numbers!")
        li[0:] = (get_coord(nest))
        print(li)
    xc, yc = tuple(li)
    if xc > 3 or yc > 3:
        print("Coordinates should be from 1 to 3!")
        li[0:2] = get_coord(nest)
    elif nest[xc - 1][yc - 1] != ' ':
        print("This cell is occupied! Choose another one!")
        li[0:2] = get_coord(nest)
    return tuple(li)


def place(xc, yc):
    global cells_nest
    n_o, n_x = 0, 0
    for i in cells_nest:
        for j in i:
            if j == 'X':
                n_x += 1
            elif j == 'O':
                n_o += 1
    if n_o == n_x:
        cells_nest[xc - 1][yc - 1] = 'X'
    elif n_o < n_x:
        cells_nest[xc - 1][yc - 1] = 'O'
    return cells_nest


def play():
    xc, yc = randint(1, 3), randint(1, 3)
    while cells_nest[xc - 1][yc - 1] != ' ':
        xc, yc = randint(1, 3), randint(1, 3)
    place(xc, yc)
    print('Making move level "easy"')
    return


winner = ""
cells_nest = [[" ", " ", " "],
              [" ", " ", " "],
              [" ", " ", " "]]


def user_x_vs_pc(cells):
    while True:
        x_col_wins = [[cells[0][0], cells[1][0], cells[2][0]] == ['X', "X", "X"],
                      [cells[0][2], cells[1][2], cells[2][2]] == ['X', "X", "X"],
                      [cells[2][1], cells[1][1], cells[0][1]] == ['X', "X", "X"]]
        o_col_wins = [[cells[0][0], cells[1][0], cells[2][0]] == ['O', "O", "O"],
                      [cells[0][2], cells[1][2], cells[2][2]] == ['O', "O", "O"],
                      [cells[2][1], cells[1][1], cells[0][1]] == ['O', "O", "O"]]
        x_row_wins = [[cells[0][0], cells[0][1], cells[0][2]] == ['X', "X", "X"],
                      [cells[1][0], cells[1][1], cells[1][2]] == ['X', "X", "X"],
                      [cells[2][0], cells[2][0], cells[2][0]] == ['X', "X", "X"]]
        o_row_wins = [[cells[0][0], cells[0][1], cells[0][2]] == ['O', "O", "O"],
                      [cells[1][0], cells[1][1], cells[1][2]] == ['O', "O", "O"],
                      [cells[2][0], cells[2][1], cells[2][2]] == ['O', "O", "O"]]
        x_cross_wins = [[cells[0][0], cells[1][1], cells[2][2]] == ['X', "X", "X"],
                        [cells[2][0], cells[1][1], cells[0][2]] == ['X', "X", "X"]]
        o_cross_wins = [[cells[0][0], cells[1][1], cells[2][2]] == ['O', "O", "O"],
                        [cells[2][0], cells[1][1], cells[0][2]] == ['O', "O", "O"]]
        draw_grid(cells)
        wins = decide(x_cross_wins, x_col_wins, x_row_wins, o_cross_wins, o_col_wins, o_row_wins)
        if wins == "O wins" or wins == "X wins":
            break
        x, y = get_coord(cells)
        cells = place(x, y)
        draw_grid(cells)
        play()
        draw_grid(cells)
    return wins


def pc_vs_pc(cells):
    while True:
        x_col_wins = [[cells[0][0], cells[1][0], cells[2][0]] == ['X', "X", "X"],
                      [cells[0][2], cells[1][2], cells[2][2]] == ['X', "X", "X"],
                      [cells[2][1], cells[1][1], cells[0][1]] == ['X', "X", "X"]]
        o_col_wins = [[cells[0][0], cells[1][0], cells[2][0]] == ['O', "O", "O"],
                      [cells[0][2], cells[1][2], cells[2][2]] == ['O', "O", "O"],
                      [cells[2][1], cells[1][1], cells[0][1]] == ['O', "O", "O"]]
        x_row_wins = [[cells[0][0], cells[0][1], cells[0][2]] == ['X', "X", "X"],
                      [cells[1][0], cells_nest[1][1], cells_nest[1][2]] == ['X', "X", "X"],
                      [cells_nest[2][0], cells_nest[2][0], cells_nest[2][0]] == ['X', "X", "X"]]
        o_row_wins = [[cells_nest[0][0], cells_nest[0][1], cells_nest[0][2]] == ['O', "O", "O"],
                      [cells_nest[1][0], cells_nest[1][1], cells_nest[1][2]] == ['O', "O", "O"],
                      [cells_nest[2][0], cells_nest[2][1], cells_nest[2][2]] == ['O', "O", "O"]]
        x_cross_wins = [[cells_nest[0][0], cells_nest[1][1], cells_nest[2][2]] == ['X', "X", "X"],
                        [cells_nest[2][0], cells_nest[1][1], cells_nest[0][2]] == ['X', "X", "X"]]
        o_cross_wins = [[cells_nest[0][0], cells_nest[1][1], cells_nest[2][2]] == ['O', "O", "O"],
                        [cells_nest[2][0], cells_nest[1][1], cells_nest[0][2]] == ['O', "O", "O"]]
        wins = decide(x_cross_wins, x_col_wins, x_row_wins, o_cross_wins, o_col_wins, o_row_wins)
        draw_grid(cells)
        if wins == "O wins" or wins == "X wins":
            break
        play()
        draw_grid(cells)
        play()
    return wins


def user_vs_user(cells):
    draw_grid(cells)
    while True:
        x_col_wins = [[cells_nest[0][0], cells_nest[1][0], cells_nest[2][0]] == ['X', "X", "X"],
                      [cells_nest[0][2], cells_nest[1][2], cells_nest[2][2]] == ['X', "X", "X"],
                      [cells_nest[2][1], cells_nest[1][1], cells_nest[0][1]] == ['X', "X", "X"]]
        o_col_wins = [[cells_nest[0][0], cells_nest[1][0], cells_nest[2][0]] == ['O', "O", "O"],
                      [cells_nest[0][2], cells_nest[1][2], cells_nest[2][2]] == ['O', "O", "O"],
                      [cells_nest[2][1], cells_nest[1][1], cells_nest[0][1]] == ['O', "O", "O"]]
        x_row_wins = [[cells_nest[0][0], cells_nest[0][1], cells_nest[0][2]] == ['X', "X", "X"],
                      [cells_nest[1][0], cells_nest[1][1], cells_nest[1][2]] == ['X', "X", "X"],
                      [cells_nest[2][0], cells_nest[2][0], cells_nest[2][0]] == ['X', "X", "X"]]
        o_row_wins = [[cells_nest[0][0], cells_nest[0][1], cells_nest[0][2]] == ['O', "O", "O"],
                      [cells_nest[1][0], cells_nest[1][1], cells_nest[1][2]] == ['O', "O", "O"],
                      [cells_nest[2][0], cells_nest[2][1], cells_nest[2][2]] == ['O', "O", "O"]]
        x_cross_wins = [[cells_nest[0][0], cells_nest[1][1], cells_nest[2][2]] == ['X', "X", "X"],
                        [cells_nest[2][0], cells_nest[1][1], cells_nest[0][2]] == ['X', "X", "X"]]
        o_cross_wins = [[cells_nest[0][0], cells_nest[1][1], cells_nest[2][2]] == ['O', "O", "O"],
                        [cells_nest[2][0], cells_nest[1][1], cells_nest[0][2]] == ['O', "O", "O"]]
        draw_grid(cells)
        wins = decide(x_cross_wins, x_col_wins, x_row_wins, o_cross_wins, o_col_wins, o_row_wins)
        if wins == "O wins" or wins == "X wins":
            break
        x, y = get_coord(cells)
        cells = place(x, y)
        draw_grid(cells)
        x, y = get_coord(cells)
        cells = place(x, y)
        draw_grid(cells)
    return wins


def user_o_vs_pc(cells):
    while True:
        x_col_wins = [[cells_nest[0][0], cells_nest[1][0], cells_nest[2][0]] == ['X', "X", "X"],
                      [cells_nest[0][2], cells_nest[1][2], cells_nest[2][2]] == ['X', "X", "X"],
                      [cells_nest[2][1], cells_nest[1][1], cells_nest[0][1]] == ['X', "X", "X"]]
        o_col_wins = [[cells_nest[0][0], cells_nest[1][0], cells_nest[2][0]] == ['O', "O", "O"],
                      [cells_nest[0][2], cells_nest[1][2], cells_nest[2][2]] == ['O', "O", "O"],
                      [cells_nest[2][1], cells_nest[1][1], cells_nest[0][1]] == ['O', "O", "O"]]
        x_row_wins = [[cells_nest[0][0], cells_nest[0][1], cells_nest[0][2]] == ['X', "X", "X"],
                      [cells_nest[1][0], cells_nest[1][1], cells_nest[1][2]] == ['X', "X", "X"],
                      [cells_nest[2][0], cells_nest[2][0], cells_nest[2][0]] == ['X', "X", "X"]]
        o_row_wins = [[cells_nest[0][0], cells_nest[0][1], cells_nest[0][2]] == ['O', "O", "O"],
                      [cells_nest[1][0], cells_nest[1][1], cells_nest[1][2]] == ['O', "O", "O"],
                      [cells_nest[2][0], cells_nest[2][1], cells_nest[2][2]] == ['O', "O", "O"]]
        x_cross_wins = [[cells_nest[0][0], cells_nest[1][1], cells_nest[2][2]] == ['X', "X", "X"],
                        [cells_nest[2][0], cells_nest[1][1], cells_nest[0][2]] == ['X', "X", "X"]]
        o_cross_wins = [[cells_nest[0][0], cells_nest[1][1], cells_nest[2][2]] == ['O', "O", "O"],
                        [cells_nest[2][0], cells_nest[1][1], cells_nest[0][2]] == ['O', "O", "O"]]
        draw_grid(cells)
        wins = decide(x_cross_wins, x_col_wins, x_row_wins, o_cross_wins, o_col_wins, o_row_wins)
        if wins == "O wins" or wins == "X wins":
            break
        play()
        draw_grid(cells)
        x, y = get_coord(cells)
        cells = place(x, y)
        draw_grid(cells)
    return wins


while True:
    command = input("Input command: ")
    if "start" in command:
        if "easy easy" in command:
            pc_vs_pc(cells_nest)
        elif "easy user" in command:
            user_o_vs_pc(cells_nest)
        elif "user easy" in command:
            user_x_vs_pc(cells_nest)
        elif "user user" in command:
            user_vs_user(cells_nest)
        else:
            print("Bad parameters!")
    elif "exit" in command:
        break
    else:
        print('The medium mode is not defined yet..')
        break
