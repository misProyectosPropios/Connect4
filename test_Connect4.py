import unittest
from Connect4 import Connect4, Status

class TestConnect4(unittest.TestCase):
    def setUp(self):
        """Initialize a new game before each test."""
        self.game = Connect4()

    def test_status_invert(self):
        """Verify that players switch correctly."""
        self.assertEqual(Status.YELLOW.invert(), Status.RED)
        self.assertEqual(Status.RED.invert(), Status.YELLOW)

    def test_status_string_representation(self):
        """Verify string output for players."""
        self.assertEqual(str(Status.YELLOW), "1")
        self.assertEqual(str(Status.RED), "2")

    def test_drop_piece_success(self):
        """Test dropping a piece into an empty column."""
        success = self.game.drop(3)
        self.assertTrue(success)
        # Piece should land at the bottom (row 5)
        self.assertEqual(self.game.board[5][3], Status.YELLOW)
        # Player should have switched to RED
        self.assertEqual(self.game.current_player, Status.RED)

    def test_drop_piece_column_full(self):
        """Test that dropping a piece in a full column returns False."""
        for _ in range(6):
            self.game.drop(0)
        # The 7th drop should fail
        success = self.game.drop(0)
        self.assertFalse(success)

    def test_is_finished_horizontal(self):
        """Test horizontal win detection."""
        for i in range(4):
            self.game.board[5][i] = Status.YELLOW
        self.assertTrue(self.game.isFinished())

    def test_is_finished_vertical(self):
        """Test vertical win detection."""
        for i in range(4):
            self.game.board[5-i][0] = Status.YELLOW
        self.assertTrue(self.game.isFinished())

    def test_is_finished_diagonal_down_right(self):
        """Test diagonal win (\) detection."""
        for i in range(4):
            self.game.board[i][i] = Status.YELLOW
        self.assertTrue(self.game.isFinished())

    def test_is_finished_diagonal_down_left(self):
        """Test diagonal win (/) detection."""
        # Column 3, 2, 1, 0 across rows 0, 1, 2, 3
        for i in range(4):
            self.game.board[i][3-i] = Status.YELLOW
        self.assertTrue(self.game.isFinished())

    def test_is_not_finished_empty(self):
        """Ensure a new game is not marked as finished."""
        self.assertFalse(self.game.isFinished())

    def test_is_complete_logic(self):
        """Verify the board completion check."""
        self.assertFalse(self.game.isComplete())
        # Fill the top row (index 0)
        for i in range(7):
            self.game.board[0][i] = Status.YELLOW
        self.assertTrue(self.game.isComplete())

    def test_game_str_output(self):
        """Ensure the board prints as a string without crashing."""
        self.assertIsInstance(str(self.game), str)

if __name__ == '__main__':
    unittest.main()