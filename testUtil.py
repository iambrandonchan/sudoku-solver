from io import StringIO
from unittest import main, TestCase
from util import Utility

class TestSudoku(TestCase):
	def test(self):
		utility = Utility()
		self.assertEquals(1, 1)

	def test1(self):
		utility = Utility()
		testNeighbors = [(1, 0), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0)]
		output = utility.getNeighboringCoordinates((0, 0))
		for neighbor in testNeighbors:
			self.assertIn(neighbor, output)

		self.assertEquals(len(output), len(testNeighbors))


if __name__ == "__main__":  # pragma: no cover
    main()