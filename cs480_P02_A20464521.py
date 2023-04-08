import curses
import sys
import csv
import os
from BruteForce_A20464521 import BruteForce
from CSPbacktrack import BackTrack
from Checker import Checker

def main():
    if len(sys.argv) == 3:
        fileName = sys.argv[1]
        mode = sys.argv[2]
        if (mode != 1 and mode != 2 and mode != 3 and mode != 4 and os.path.exists(fileName) == False):
           print('ERROR: Illegal input arguments.')
           exit() 
    else:
        print('ERROR: Not enough or too many input arguments.')
        exit()

    print("Petkov, Kamen, A20464521 solution: ")
    print("Input file: ", fileName)
    print("Algorithm: ", mode)
    print("Input puzzle: \n")
    # Open the CSV file
    rowString = ""
    with open(fileName, newline='') as csvfile:
        # Create a CSV reader object
        reader = csv.reader(csvfile)

        # Loop through each row in the CSV file
        for row in reader:
            # Loop through each value in the 
            rowString = ""
            for value in row:
                # Do something with the value
                rowString += value + ","
            print(rowString[:len(rowString) - 1])
    print()
    
    
    
    
    # BF = BruteForce(fileName)
    # BF.BruteForce()
    CSP = BackTrack(fileName)
    CSP.CSP()
    CSP.print_puzzle_final()
    print("\nNow checker will run to see if that is correct: \n")
    checker = Checker(CSP.puzzle)
    print(checker.is_valid())
    
    
main()

