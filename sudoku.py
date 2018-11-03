# this class will model the sudoku problem itself

"""
What to consider, how to go about solving this problem
 we can think of this problem as a tree search...
 consider the "state" of the sudoku problem as a node in a tree
 from this "state", we can assign some square in sudoku, producing
 a new "state".

 So, we can bruteforce it and do a bunch of backtracking. we can do
 forward tracking, detecting failure earlier(keep a set of potential values
 for each square). But forward checking could still fail....

 Lastly, we can do arc consistency, that would work but could potentially be
 incredibly slow.

 Methods to consider:
 -a method to solve the problem
 -a method to get the next state in sudoku(determine a value of a square)
 -a method to initialize the sudoku problem, or set the sudoku grid

"""

class SudokuProblem:
	def __init__(self):
		#do stuff



