import unittest as ut
import board as bo

class TestBoard(ut.TestCase):
    board = bo.Board()

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
            TestBoard.board._clean_board())

if __name__ == '__main__':
    ut.main()
