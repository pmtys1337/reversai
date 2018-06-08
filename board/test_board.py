import unittest as ut
import board as bo

class TestBoard(ut.TestCase):
    board = bo.Board()
    # test private method for expected behavior
    def test_clean_board(self):
        self.assertEqual(
            [[None,None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None,None],
             [None,None,None,"w", "b", None,None,None],
             [None,None,None,"b", "w", None,None,None],
             [None,None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None,None]
            ],
            TestBoard.board._Board__clean_board())

    def test_get_dcboard(self):
        # equal but not the same
        self.assertEqual(
            TestBoard.board._Board__board,
            TestBoard.board._Board__get_dcboard())
        self.assertEqual(
            True,
            TestBoard.board._Board__board is not \
                TestBoard.board._Board__get_dcboard())

    def test_get_valid_moves(self):
        self.assertEqual(
            [(2,4),(3,5),(4,2),(5,3)],
            TestBoard.board._Board__valid_moves)


    def test_is_valid_move(self):
        # move on an empty board
        self.assertEqual(
            False,
            TestBoard.board._Board__is_valid_move(3, 3)) # row_idx, col_idx
        self.assertEqual(
            True,
            TestBoard.board._Board__is_valid_move(2, 4)) # row_idx, col_idx

    def test_make_a_move(self):
        self.assertEqual(
            [[None,None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None,None],
             [None,None,None,None,"w", None,None,None],
             [None,None,None,"w", "w", None,None,None],
             [None,None,None,"b", "w", None,None,None],
             [None,None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None,None]
            ],
            TestBoard.board._Board__make_a_move(2,4))
        self.assertEqual(
            None,
            TestBoard.board._Board__make_a_move(3,3))

if __name__ == '__main__':
    ut.main()
