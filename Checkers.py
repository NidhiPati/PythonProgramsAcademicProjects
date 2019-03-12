import sys
from copy import deepcopy


def main():
    for arg in sys.argv[1:]:
        print(arg)


class Board:
    EMPTY = " "

    def __init__(self):
        self.the_end = False
        self.count = 0
        self.num_of_jumps = list()
        self.max_number_of_jumps = 0
        self._board = []
        for row in range(8):
            self._board.append([])
            for column in range(8):
                self._board[row].append(Board.EMPTY)
        for row in range(0, 8, 2):
            for column in range(1, 8, 2):
                self._board[row][column] = "*"
        for row in range(1, 8, 2):
            for column in range(0, 8, 2):
                self._board[row][column] = "*"

    def print(self):
        return "\n".join(str(row) for row in self._board)

    def add_checker(self, row, col, who):
        if 0 <= row < 8 and 0 <= col < 8:
            if self._board[row][col] == "*":
                print("This is an invalid location on the board. So, not adding the piece: ", row, col)
                # not adding checker - input 5
            elif self._board[row][col] == who:   # if same piece is already present, then continuing
                print("Duplicate piece present, so not adding the piece: ", row, col)     # input 13
                pass
            elif self._board[row][col] != Board.EMPTY:
                raise ValueError("This location is not empty")
            else:
                self._board[row][col] = who
        else:
            raise ValueError("Invalid row/col")

    def reset(self):
        for row in range(0, 8, 2):
            for column in range(1, 8, 2):
                self._board[row][column] = "*"
        for row in range(1, 8, 2):
            for column in range(0, 8, 2):
                self._board[row][column] = "*"
        for row in range(8):
            for column in range(8):
                if self._board[row][column] != "*":
                    self._board[row][column] = Board.EMPTY

    def can_jump(self, row, col):
        if row < 0 or row > 7 or col < 0 or col > 7:
            return False
        elif self._board[row][col] != Board.EMPTY:
            return False
        else:
            return True

    def move_checker(self, old_row, old_col, new_row, new_col, what):
        self._board[old_row][old_col] = Board.EMPTY
        self._board[new_row][new_col] = what

    def solve(self, row, col, count):
        if board1.the_end is False:
            board1.num_of_jumps.append(count)
            starting_row = row
            starting_col = col
            left_up_board = deepcopy(board1._board)
            left_down_board = deepcopy(board1._board)
            right_up_board = deepcopy(board1._board)
            right_down_board = deepcopy(board1._board)
            board1._board = left_up_board
            Board.numJumps(self, starting_row, starting_col, 'LEFT_UP', count)
            board1._board = left_down_board
            Board.numJumps(self, starting_row, starting_col, 'LEFT_DOWN', count)
            board1._board = right_up_board
            Board.numJumps(self, starting_row, starting_col, 'RIGHT_UP', count)
            board1._board = right_down_board
            Board.numJumps(self, starting_row, starting_col, 'RIGHT_DOWN', count)

    def numJumps(self, row, col, which_direction, count):
        leftuprow = row-1
        leftupcolumn = col-1
        leftdownrow = row+1
        leftdowncolumn = col - 1
        rightuprow = row-1
        rightupcolumn = col + 1
        rightdownrow = row+1
        rightdowncolumn = col+1
        if (which_direction == 'LEFT_UP') or (which_direction == 'NA' and 0 <= leftuprow < 8 and 0 <= leftupcolumn < 8
                                            and self._board[leftuprow][leftupcolumn] == "E"):
            if 0 <= leftuprow < 8 and 0 <= leftupcolumn < 8:
                if self._board[leftuprow][leftupcolumn] == "E":
                    row_ = leftuprow
                    col_ = leftupcolumn
                    is_jump_possible = Board.can_jump(self, row_-1, col_-1)
                    if is_jump_possible is True:
                        Board.move_checker(self, row, col, row_-1, col_-1, 'N')
                        self._board[row_][col_] = " "
                        board1.count = board1.count + 1
                        count = count + 1
                        board1.solve(row_-1, col_-1, count)
                        # Board.numJumps(self, row_ - 1, col_ - 1, 'NA')
                    else:
                        pass
            else:
                pass

        elif (which_direction == 'LEFT_DOWN') or (which_direction == 'NA' and 0 <= leftdownrow < 8 and 0 <= leftdowncolumn < 8
                                              and self._board[leftdownrow][leftdowncolumn] == "E"):
            if 0 <= leftdownrow < 8 and 0 <= leftdowncolumn < 8:
                if self._board[leftdownrow][leftdowncolumn] == "E":
                    row_ = leftdownrow
                    col_ = leftdowncolumn
                    is_jump_possible = Board.can_jump(self, row_+1, col_-1)
                    if is_jump_possible is True:
                        Board.move_checker(self, row, col, row_+1, col_-1, 'N')
                        self._board[row_][col_] = " "
                        board1.count = board1.count + 1
                        count = count + 1
                        board1.solve(row_+1, col_-1, count)
                        # Board.numJumps(self, row_+1, col_-1, 'NA')
                    else:
                        pass
            else:
                pass

        elif (which_direction == 'RIGHT_UP') or (which_direction == 'NA' and 0 <= rightuprow < 8 and 0 <= rightupcolumn < 8
                                             and self._board[rightuprow][rightupcolumn] == "E"):
            if 0 <= rightuprow < 8 and 0 <= rightupcolumn < 8:
                if self._board[rightuprow][rightupcolumn] == "E":
                    row_ = rightuprow
                    col_ = rightupcolumn
                    is_jump_possible = Board.can_jump(self, row_-1, col_+1)
                    if is_jump_possible is True:
                        Board.move_checker(self, row, col, row_-1, col_+1, 'N')
                        self._board[row_][col_] = " "
                        board1.count = board1.count + 1
                        count = count + 1
                        board1.solve(row_-1, col_+1, count)
                        # Board.numJumps(self, row_-1, col_+1, 'NA')
                    else:
                        pass
            else:
                pass

        elif (which_direction == 'RIGHT_DOWN') or (which_direction == 'NA' and 0 <= rightdownrow < 8 and 0 <= rightdowncolumn < 8
                                               and self._board[rightdownrow][rightdowncolumn] == "E"):
            if 0 <= rightdownrow < 8 and 0 <= rightdowncolumn < 8:
                if self._board[rightdownrow][rightdowncolumn] == "E":
                    row_ = rightdownrow
                    col_ = rightdowncolumn
                    is_jump_possible = Board.can_jump(self, row_+1, col_+1)
                    if is_jump_possible is True:
                        Board.move_checker(self, row, col, row_+1, col_+1, 'N')
                        self._board[row_][col_] = " "
                        board1.count = board1.count + 1
                        count = count + 1
                        board1.solve(row_+1, col_+1, count)
                        # Board.numJumps(self, row_+1, col_+1, 'NA')
                    else:
                        pass
            else:
                pass

        else:
            board1.the_end = True
            print("The End")


if __name__ == "__main__":
    board1 = Board()
    file_name = sys.argv[1]
    file_content = open(file_name, "r").readlines()
    line = int(file_content[0])
    file_line_counter = 1
    print(line)
    for each_test_case in range(line):
        board1.reset()
        temp = file_content[file_line_counter]
        temp_array = temp.split(" ")
        file_line_counter = file_line_counter + 1
        first_piece = file_content[file_line_counter]
        i = first_piece.split(" ")
        row1 = int(i[0])
        col1 = int(i[1])
        for loop in range(int(temp_array[0])):
            row_col_split = file_content[file_line_counter]
            a = row_col_split.split(" ")
            board1.add_checker(int(a[0]), int(a[1]), 'N')   # me
            file_line_counter = file_line_counter + 1
        for loop in range(int(temp_array[1])):
            row_col_split = file_content[file_line_counter]
            a = row_col_split.split(" ")
            board1.add_checker(int(a[0]), int(a[1]), 'E')   # Enemy
            file_line_counter = file_line_counter + 1
        board1.num_of_jumps.clear()
        board1.solve(row1, col1, 0)
        board1.max_number_of_jumps = max(board1.num_of_jumps)
        # print(board1.print())
        # print("Number of Jumps: ", board1.num_of_jumps)
        print("Maximum number of Jumps: ", board1.max_number_of_jumps)




