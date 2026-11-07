# Worlu-Ezechima-Ohms-law-calculator-
Ohm's Law and Power Calculator developed with Python for CTE123 Mini Project.

# Ohm's Law and Power Calculator

## What it does
This program lets you calculate voltage, current, resistance or power using Ohm's Law and the common power formulas.  
You choose what you want to find, enter the known values, and get a clear answer with units.  
The program keeps running until you decide to quit.

## How to run it
Install Python 3, then run:

## Sample output
==================================================
OHM'S LAW AND POWER CALCULATOR
ND1 Mechatronics Engineering - YabaTech
What do you want to calculate?
Voltage (V)
Current (I)
Resistance (R)
Power (P)
Quit
Enter 1-5: 1
Calculate Voltage (V = I × R)
Enter current in Amperes (I): 2
Enter resistance in Ohms (R): 10
Voltage = 20.0000 V
Formula used: V = I × R
Do another calculation? (y/n): n
==================================================
SESSION SUMMARY
You performed 1 calculation(s):
Voltage: 20.0000 V
Formula: V = I × R
Inputs:  I = 2.0 A, R = 10.0 Ω
Thank you for using the calculator. Goodbye!
## My own twist
I added a **session history**. Every successful calculation is stored. When you quit, the program prints a clean summary showing:
- how many calculations you did
- the result of each one
- the exact formula that was used
- the values you entered

This makes it easy to review your work without writing anything down.

## What I learned
- How to use functions to organise code and avoid repetition
- How to handle wrong input (letters instead of numbers, or division by zero) so the program does not crash
- How lists can be used to keep a simple history of what the user has done

## Author
Worlu Eze Chima, ND1 Mechatronics Engineering, YabaTech.