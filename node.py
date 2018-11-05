"""
class node is supposed to represent a node in a coloring problem

sudoku node is a node in sudoku, inheriting from node
"""

class SudokuSquare:
	#initialize a sqaure, given it's coordinates, neighbor coordinates
	#and a value if given one
	def init(self, coordinates, neighbors, value = None):
		self.coordinates = coordinates
		self.neighbors = neighbors
		self.possibleNumbers = set()
		self.value = value
		#set has all possible values, will need to wittle it down
		if self.value is None:
			for i in range(1, 10):
				selfpossibleNumbers.add(i)
