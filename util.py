"""
what do i want utility to have?
utility is a class in which i need to do simple and monotonous checks
revolving around solving sudoku

brainstorm methods:
- getNeighborSquares(sudoku problem, square): sudoku is almost llike a graph coloring problem
  This method could retrieve a list of all squares directly associated
  with a given square, 3x3 its in and row/col

- we need a method to extract the next node to analyze.
  like a good policy it choose the next square is to 
  use the most constraining square, that is, the square with
  the most least possible options

- possibly a method to check to see if the sudoku problem is complete
- a method to check if constraints are correct possibly...
"""


class Utility:
	def doStuff(self):

		return "yes"