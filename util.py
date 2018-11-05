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
from node import SudokuSquare
from sudoku import SudokuProblem


class Utility:
	def doStuff(self):

		return "stuff"

	def getNextNode(self, sudokuProblem):
		for row in range(0, 9):
			for col in range(0, 9):
				square = sudokuProblem.grid[row][col]
				if square.value is not None and len(square.possibleNumbers) is 1:
					return square
		return None
	#we need to extract "neighboring" squares given a square in sudoku
	def getNeighboringCoordinates(self, coordinate):
		#we need to retrieve the neighboring squares in
		#a 3x3, and also row and column
		x, y = coordinate

		xBlock = x // 3
		yBlock = y // 3

		# return (xBlock, yBlock)
		neighboringCoordinates = []

		# add all neighbor nodes in a 3x3 square
		for row in range(xBlock * 3, xBlock * 3 + 3):
			for col in range(yBlock * 3, yBlock * 3 + 3):
				neighborCoordinate = (row, col)
				if neighborCoordinate != coordinate:
					neighboringCoordinates.append(neighborCoordinate)

		for rowOrCol in range(0, 9):
			if rowOrCol != x and (rowOrCol, y) not in neighboringCoordinates:
				neighboringCoordinates.append((rowOrCol, y))
			if rowOrCol != y and (rowOrCol, y) not in neighboringCoordinates:
				neighboringCoordinates.append((x, rowOrCol))

		return neighboringCoordinates



