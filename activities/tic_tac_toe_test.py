import unittest
from tac_tac_bug_toe import is_win, tally_wins

class TestIsWin(unittest.TestCase):

    def test_row_win(self):
        """Test that a full row is detected as a win."""
        board = [['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertTrue(is_win('X', board))

    def test_column_win(self):
        """Test that a full column is detected as a win."""
        board = [['O', ' ', ' '], ['O', ' ', ' '], ['O', ' ', ' ']]
        self.assertTrue(is_win('O', board))

    def test_diagonal_win(self):
        """Test that a top-left to bottom-right diagonal is detected as a win."""
        board = [['X', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'X']]
        self.assertTrue(is_win('X', board))

    def test_right_diagonal_win(self):
        """Test that a top-right to bottom-left diagonal is detected as a win."""
        board = [[' ', ' ', 'O'], [' ', 'O', ' '], ['O', ' ', ' ']]
        self.assertTrue(is_win('O', board))

    def test_no_win_empty_board(self):
        """Test that an empty board returns no win."""
        board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertFalse(is_win('X', board))

    def test_no_win_partial_board(self):
        """Test that a partially filled board with no winner returns False."""
        board = [['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', ' ']]
        self.assertFalse(is_win('X', board))


class TestTallyWins(unittest.TestCase):

    def test_tally_all_wins(self):
        """Test tally with all wins."""
        self.assertEqual(tally_wins([True, True, True]), 3)

    def test_tally_no_wins(self):
        """Test tally with no wins."""
        self.assertEqual(tally_wins([False, False, False]), 0)

    def test_tally_empty(self):
        """Test tally with an empty list."""
        self.assertEqual(tally_wins([]), 0)


if __name__ == "__main__":
    unittest.main()
