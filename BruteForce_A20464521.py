import csv
import sys
import curses
import time
import itertools

class BruteForce:
    def __init__(self, fileName):
        self.fileName = fileName
        self.boxes = {}
        self.allValues = {}
        self.puzzle = []
    
    
    def get_box(self, puzzle, start_row, start_col):
        box = []
        for row in range(start_row, start_row + 3):
            box_row = []
            for col in range(start_col, start_col + 3):
                box_row.append(puzzle[row][col])
            box.append(box_row)
        return box
    
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
    
    def is_valid(self):
        checklst = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        
        #print(self.puzzle)
        # I: Check ROWS
        lst = checklst.copy()
        for i in range(9):
            for j in range(9):
                if self.puzzle[i][j] in lst:
                    lst.remove(self.puzzle[i][j])
                else:
                    # print("Repetition! Puzzle is wrong ROW!")
                    # print(self.puzzle[i][j], ', ROW #', i+1)
                    return False
            lst = checklst.copy()
        
        
        # II: Check COLS 
        
        lst = checklst.copy()
        for i in range(9):
            for j in range(9):
                if self.puzzle[j][i] in lst:
                    lst.remove(self.puzzle[j][i])
                else:
                    # print("Repetition! Puzzle is wrong COL!")
                    # print(self.puzzle[j][i], ', COL #', i+1)
                    return False
            lst = checklst.copy()
        
                
        # III: Check Boxes (3x3)
        lst = checklst.copy()
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                box = self.get_box(self.puzzle, row, col)
                for rows in box:
                    for value in rows:
                        if value in lst:
                            lst.remove(value)
                        else:
                            # print("Repetition! Puzzle is wrong BOX!")
                            # print(value)
                            return False 
                lst = checklst.copy()
        return True  
    

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
        time.sleep(0.01)
    
    def BruteForce(self):           
        with open(self.fileName, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            # we want to keep looping until we exhaust all possible combinations
            i = 0
            for row in reader:
                for value in row:
                    self.allValues[i] = value
                    # Do something with the value
                    if value == "X":
                        self.boxes[i] = value
                    i += 1
        
        
        r = 0
        for i in range(0, 9):
            row = []
            for _ in range(0, 9):
                row.append(self.allValues[r])
                r += 1
            self.puzzle.append(row)
        
        keylst = []
        for key in self.boxes.keys():
            keylst.append(key)
        
        while True:
            for guess in itertools.product(range(1, 10), repeat=len(self.boxes)):
                i = 0
                vals = list(guess)
                for index in self.boxes.keys():
                    # for every combination that we try, we put the values in the puzzle 
                    # we have to check if puzzle is correct                    
                    self.puzzle[int(index/9)][index%9] = str(vals[i])
                    
                    curses.wrapper(lambda stdscr: self.print_puzzle(self.puzzle, stdscr))
                    
                    if self.is_valid():
                        print("SOLUTION FOUND: ")
                        self.print_puzzle_final()
                        return self.puzzle
                    i += 1
            print("COULDN'T FIND A SOLUTION :(")
            self.print_puzzle_final()
            return self.puzzle
        

        