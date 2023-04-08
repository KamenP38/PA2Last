import csv
import curses
import time


class BackTrack:

    def __init__(self, filename):
        self.filename = filename
        self.allValues = []
        self.todo = {} # THE EMPTY VALUES (AKA = "X")
        self.puzzle = []
        
        # get the values we are going to work with
        with open(self.filename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            # we want to keep looping until we exhaust all possible combinations
            i = 0
            for row in reader:
                for value in row:
                    
                    self.allValues.append(value)
                    # print(self.allValues[i])
                    # Do something with the value
                    if value == "X":
                        self.todo[i] = value   # THE EMPTY VALUES (AKA = "X")
                    i += 1
    
        # now that we have the values with "X", we will assign values to them
        # whenever it's not value --> BACKTRACK (RECURSIVELY)
        
        # That means we need a method to check the validity
        r = 0
        for i in range(0, 9):
            row = []
            for _ in range(0, 9):
                row.append(self.allValues[r])
                r += 1
            self.puzzle.append(row)
    
    def print_puzzle(self, puzzle, stdscr):
        stdscr.clear()
        for i in range(len(self.puzzle)):
            if i % 3 == 0 and i != 0:
                stdscr.addstr("-" * 21 + "\n")
            for j in range(len(self.puzzle[i])):
                if j % 3 == 0 and j != 0:
                    stdscr.addstr("| ")
                if self.puzzle[i][j] == 'X':
                    stdscr.addstr("_ ")
                else:
                    stdscr.addstr(str(self.puzzle[i][j]) + " ")
                if j == len(self.puzzle[i]) - 1:
                    stdscr.addstr("\n")
            if i == len(self.puzzle) - 1:
                stdscr.addstr("\n")
        stdscr.refresh()
        time.sleep(0.1)

    def print_puzzle_final(self):
        for i in range(len(self.puzzle)):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            for j in range(len(self.puzzle[i])):
                if j % 3 == 0 and j != 0:
                    print("| ", end="")
                print(str(self.puzzle[i][j]) + " ", end="")
                if j == len(self.puzzle[i]) - 1:
                    print("")
    
    def is_valid(self, row, col, val):
        # I: Check ROWS
        for i in range(9):
            if self.puzzle[row][i] == val:
                # print("ROW")
                return False
        
        
        # II: Check COLS 
        for i in range(9):
            if self.puzzle[i][col] == val:
                # print("COL")
                return False
                
        # III: Check Boxes (3x3)
        boxRow = (row // 3) * 3
        boxCol = (col // 3) * 3
        for i in range(boxRow, boxRow + 3):
            for j in range(boxCol, boxCol + 3):
                if self.puzzle[i][j] == val:
                    # print("BOX")
                    return False
        return True  


    # Process:
    # Start by choosing a value from a certain domain
    # Each box will have a domain of available values
    # If in domain choose value 
    # keep choosing values until you see a conflict
    # if you see a conflict --> backtrack

    def CSP(self):
        # this is the backtracking algorithm
        row = None
        col = None
        for r in range(9):
            for c in range(9):
                if self.puzzle[r][c] == "X":
                    row = r
                    col = c        
                    
        
        if row == None and col == None:
            return True
        
        for val in range(1, 10):
            # puz = self.puzzle.copy()
            # puz[row][col] = str(val)
            # curses.wrapper(lambda stdscr: self.print_puzzle(puz, stdscr))
            if self.is_valid(row, col, str(val)):
                self.puzzle[row][col] = str(val)
                if self.CSP():
                    return True
                self.puzzle[row][col] = "X"
                

        print("FAILURE :(\n")
        #self.print_puzzle_final()
        return self.puzzle
        
        
        
        
