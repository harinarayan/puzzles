
#!/usr/bin/python3

"""
Sudoku
Git : https://github.com/harinarayan/puzzles
Date : 5 Apr 2020
"""

from typing import List

class Sudoku():
    """
    Solves sudoku using backtracking.
    Usage: Initialize an object with a board and call solve().
            A board is a list of 81 integers. Empty cells contain 0.
    """

    def __init__(self, board: List[int]):
        """
        board - list of 81 ints. Empty cells contain 0.
        """
        self.board = board
        self.a = board[:]
        self.found = False

    def solve(self, pretty_output: bool = True) -> None:
        """
        pretty_output if set to true, prints the board in a human readable form after solving.
        If set to false, a string of 81 integers will be printed
        """
        self.display()
        for i, c in enumerate(self.a):
            if not c:
                self.branch(i)
                break
        #print(self.a, sep="")
        if pretty_output:
            self.display()
        else:
            print(self.a)


    def display(self):
        """
        Pretty printing the current board state
        """
        for i, c in enumerate(self.a):
            if not i%9: print()
            if not i%27: print()
            if not i%3: print(" ", end="")
            print(c if c else ".", " ", end="")
        print("\n")

    def process(self) -> None:
        """
        What needs to be done when a solution is found is defined here.
        """
        self.found = True

    def branch(self, k: int) -> None:
        """
        Method for recursion. Calls itself with next index. Exits recursion when if pruneable.
        """
        #print("branch", k)
        #self.display()
        if k == 81:
            self.process()
            return
        possible_values = [self.board[k]] if self.board[k] else list(range(1, 10))
        for i in possible_values:
            self.a[k] = i
            if not self.prune(k): self.branch(k+1)
            if self.found: break
            self.a[k] = self.board[k] if self.board[k] else 0

    def prune(self, k: int) -> bool:
        """
        Hypothesis tester. Returns true if this branch has to be pruned and
        has to be backtracked
        """
        #print("prune", k, self.a[k], " ", end="")
        #vertical duplicate check
        for x in range(k-9, 0, -9):
            if self.a[x] == self.a[k]:
                #print("vd pre")
                return True
        for x in range(k+9, 81, 9):
            if self.a[x] == self.a[k]:
                #print("vd post")
                return True

        #horizontal duplicate check
        for x in range(k - k%9, k):
            if self.a[x] == self.a[k]:
                #print("hd pre")
                return True
        for x in range(k+1, k+9 - (k+9)%9):
            if self.a[x] == self.a[k]:
                #print("hd post")
                return True

        #sub-box duplicate check
        j = (k-k%27) + (k - (k-k%27))%9
        subbox_indices = [j-j%3, j-j%3+1, j-j%3+2]
        subbox_indices.extend([i+9 for i in subbox_indices[:3]])
        subbox_indices.extend([i+18 for i in subbox_indices[:3]])
        for i in subbox_indices:
            if k != i and self.a[k] == self.a[i]:
                #print("sb", subbox_indices)
                return True

        #print("ok")
        return False

if __name__ == "__main__":
    """
    Reads nine lines from stdin. Use 0 for empty cells.
    To use this as a standalone program
        $> cat sudoku.input
        700028003
        000000409
        000000000
        000006020
        070010900
        640300008
        008000310
        500069000
        000000002
        $> cat sudoku.input | python3 sudoku.py
        7  .  .   .  2  8   .  .  3
        .  .  .   .  .  .   4  .  9
        .  .  .   .  .  .   .  .  .

        .  .  .   .  .  6   .  2  .
        .  7  .   .  1  .   9  .  .
        6  4  .   3  .  .   .  .  8

        .  .  8   .  .  .   3  1  .
        5  .  .   .  6  9   .  .  .
        .  .  .   .  .  .   .  .  2

        7  9  1   4  2  8   5  6  3
        2  5  6   7  3  1   4  8  9
        3  8  4   6  9  5   2  7  1

        1  3  5   9  8  6   7  2  4
        8  7  2   5  1  4   9  3  6
        6  4  9   3  7  2   1  5  8

        9  6  8   2  4  7   3  1  5
        5  2  3   1  6  9   8  4  7
        4  1  7   8  5  3   6  9  2
    """
    #board = "000020608" + "000508010" + "010040009" + "900000004" +
        #"700304001" + "800000002" + "200010070" + "060207000" + "403050000"
    board = ""
    for i in range(9):
        board = board + input()
    assert len(board) == 81, board
    board = [int(c) for c in board]
    Sudoku(board).solve(pretty_output=1)
