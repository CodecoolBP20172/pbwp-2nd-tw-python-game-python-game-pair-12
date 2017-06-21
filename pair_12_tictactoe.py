
import sys


def print_table():
    print("\n")
    print("  " + table[7] + "  |  " + table[8] + "  |  " + table[9] + "  ")
    print("-----------------")
    print("  " + table[4] + "  |  " + table[5] + "  |  " + table[6] + "  ")
    print("-----------------")
    print("  " + table[1] + "  |  " + table[2] + "  |  " + table[3] + "  ")
    print("\n")


def win():
    if counter % 2 != 0:
        print(name1 + " won!")
        want_to_play_again()
    else:
        print(name2 + " won!")
        want_to_play_again()


def draw():
    print("Tie!")
    want_to_play_again()


def checkwin():
    global game
    if (table[1] == table[2] and table[2] == table[3]) or \
        (table[4] == table[5] and table[5] == table[6]) or \
        (table[7] == table[8] and table[8] == table[9]) or \
        (table[1] == table[4] and table[4] == table[7]) or \
        (table[2] == table[5] and table[5] == table[8]) or \
        (table[3] == table[6] and table[6] == table[9]) or \
        (table[1] == table[5] and table[5] == table[9]) or \
            (table[3] == table[5] and table[5] == table[7]):
        win()
    elif (table[1].isalpha() and table[2].isalpha() and table[3].isalpha()
          and table[4].isalpha() and table[5].isalpha() and table[6].isalpha()
          and table[7].isalpha() and table[8].isalpha() and table[9].isalpha()):
        draw()
    else:
        global counter
        counter += 1


def cell_is_empty(cell_num):
    return table[cell_num] == str(cell_num)


def want_to_play_again():
    more = input("Want to play again? (y/n)")
    more = more.upper()
    if more == "Y":
        global table
        table.clear()
        table = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        print_table()
        global counter
        counter += 1
    else:
        sys.exit()


table = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
print_table()
counter = 0

name1 = input("Name (player X): ")
name2 = input("Name (player O): ")

more = "y"

while more == "y":
    checkwin()
    if counter % 2 != 0:
        char = "X"
        name = name1
    else:
        char = "O"
        name = name2
    num = input("It's your turn, " + name + ". Enter a number according to the table above: ")
    if len(num) != 1 or (not num.isdigit()):
        print("Please choose from 1-9.")
        counter -= 1
    elif cell_is_empty(int(num)):
        table[int(num)] = char
        print_table()
    else:
        print("This block is not empty.")
        counter -= 1
