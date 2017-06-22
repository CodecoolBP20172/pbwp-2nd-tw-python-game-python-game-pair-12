
import sys
import datetime


class color:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    END = '\033[0m'


def print_table():
    print("\n")
    print("  " + table[7] + "  |  " + table[8] + "  |  " + table[9] + "  ")
    print("-----------------")
    print("  " + table[4] + "  |  " + table[5] + "  |  " + table[6] + "  ")
    print("-----------------")
    print("  " + table[1] + "  |  " + table[2] + "  |  " + table[3] + "  ")
    print("\n")


def checkwin():
    if (table[1] == table[2] and table[2] == table[3]) or \
        (table[4] == table[5] and table[5] == table[6]) or \
        (table[7] == table[8] and table[8] == table[9]) or \
        (table[1] == table[4] and table[4] == table[7]) or \
        (table[2] == table[5] and table[5] == table[8]) or \
        (table[3] == table[6] and table[6] == table[9]) or \
        (table[1] == table[5] and table[5] == table[9]) or \
            (table[3] == table[5] and table[5] == table[7]):
        win()
    elif any(element.isdigit() for element in table) is False:
        draw()
    else:
        global counter
        counter += 1


def print_current_score():
    print("{}: {} - {}: {}".format(name1, name1_score, name2, name2_score))


def win():
    global name1_score
    global name2_score
    if counter % 2 != 0:
        print(name1 + " won!")
        name1_score += 1
        want_to_play_again()
    else:
        print(name2 + " won!")
        name2_score += 1
        want_to_play_again()


def draw():
    print("Tie!")
    want_to_play_again()


def cell_is_empty(cell_num):
    return table[cell_num] == str(cell_num)


def want_to_play_again():
    print_current_score()
    while True:
        try:
            more = input("Want to play again? (y/n)")
            more = more.upper()
            assert more == "Y" or more == "N"
        except Exception:
            print("Please choose between 'y' or 'n'.")
        else:
            break
    if more == "Y":
        global table
        table = ["X", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        print_table()
        global counter
        counter += 1
    elif more == "N":
        with open("scores.txt", "a") as scores:
            scores.write(str(datetime.datetime.now().date())+"\n")
            scores.write("{}: {}\n".format(name1, name1_score))
            scores.write("{}: {}\n".format(name2, name2_score))
            scores.write("◡◠◡◠◡◠◡◠◡"+"\n")
            sys.exit()


def start_game():
    print("""

    - For this game, two players are required.
    - Decide who starts.
    - The first player starts with "X".
    - After the first round, you can either continue or stop.
    - The loser starts next round.
    - After a finished game, scores can be reviewed in the "scores.txt" file.
    """)

    print_table()
    global name1
    global name2
    name1 = input("First player, enter your name: ")
    name2 = input("Second player, enter your name: ")


def game_play():
    global counter
    counter = 0
    more = "y"
    while more == "y":
        checkwin()
        if counter % 2 != 0:
            char = color.BLUE + "X" + color.END
            name = name1
        else:
            char = color.GREEN + "O" + color.END
            name = name2
        num = input("\nIt's your turn, " + name + ". Enter a number according to the table above: ")
        if len(num) != 1 or (not num.isdigit()):
            print("Please choose from 1-9.")
            counter -= 1
        elif cell_is_empty(int(num)):
            table[int(num)] = char
            print_table()
        else:
            print("This block is not empty.")
            counter -= 1


def main():
    global table
    global name1_score
    global name2_score
    table = ["X", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    name1_score = 0
    name2_score = 0
    start_game()
    game_play()


if __name__ == "__main__":
    main()
