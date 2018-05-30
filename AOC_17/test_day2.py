import unittest

from day2 import get_input, row_checksum, grid_checksum, total_even_divis, find_even_divis


class TestGetInput(unittest.TestCase):
    def test_get_input(self):
        puzzle_in = get_input()
        self.assertEqual(
            puzzle_in[0],
            [515, 912, 619, 2043, 96, 93, 2242, 1385, 2110, 860, 2255, 621, 1480, 118, 1230, 99],
        )
        self.assertEqual(
            puzzle_in[-1],
            [707, 668, 1778, 1687, 2073, 1892, 62, 1139, 908, 78, 1885, 800, 945, 712, 57, 65],
        )
        self.assertEqual(
            puzzle_in[-2],
            [1112, 1260, 809, 72, 1104, 156, 104, 1253, 793, 462, 608, 84, 99, 1174, 449, 929],
        )


class TestRowChecksum(unittest.TestCase):
    def test_row_checksum(self):
        self.assertEqual(row_checksum([5, 1, 9, 5]), 8)
        self.assertEqual(row_checksum([7, 5, 3]), 4)
        self.assertEqual(row_checksum([2, 4, 6, 8]), 6)


class TestGridChecksum(unittest.TestCase):
    def test_grid_checksum(self):
        grid = [[5, 1, 9, 5], [7, 5, 3],[2, 4, 6, 8]]
        self.assertEqual(grid_checksum(grid), 18)

    def test_solves_pt1(self):
        puz_in = get_input()
        self.assertEqual(grid_checksum(puz_in), 45972)


class TestFindEvenDivis(unittest.TestCase):
    def test_find_even_divis(self):
        self.assertEqual(find_even_divis([5, 9, 2, 8]), 4)
        self.assertEqual(find_even_divis([9, 4, 7, 3]), 3)
        self.assertEqual(find_even_divis([3, 8, 6, 5]), 2)


class TestTotalEvenDivis(unittest.TestCase):
    def test_total_even_divis(self):
        grid = [[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]]
        self.assertEqual(total_even_divis(grid), 9)

    def test_solves_pt2(self):
        puz_in = get_input()
        self.assertEqual(total_even_divis(puz_in), 326)
