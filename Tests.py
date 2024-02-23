import unittest
from Board import Board
from Controller import Controller


class TestBoard(unittest.TestCase):
    def test_board(self):
        board=[[0,0,0,0]]
        self.board=Board(1,4)
        self.board.create_board()
        self.assertEqual(board, self.board.get_board())

        self.board.clear_board()
        self.assertEqual(self.board.clear_board(),None)

        self.board=Board(3,3)
        self.board.create_board()
        available_moves=self.board.ok_move()
        self.assertEqual(len(available_moves),9)

        self.board.set_column(7)
        self.assertEqual(self.board.get_column(),7)

        self.board.set_row(4)
        self.assertEqual(self.board.get_row(),4)


class TestController(unittest.TestCase):
    def test_controller(self):
        board = Board(3,7)
        self.board1=Controller(board)
        self.board1.create_board()
        self.assertNotEqual(self.board1.get_board(),None)
        self.assertEqual(str(board),str(self.board1.get_board()))

        self.board2=Controller(Board(2,2))
        self.board2.create_board()
        self.board2.player_move(0,0)
        self.assertFalse(self.board2.game_over())

        self.board2 = Controller(Board(3, 3))
        self.board2.create_board()
        self.board2.move_ai(True,1, 1)
        self.assertFalse(self.board2.game_over())

if __name__=='__main__':
    unittest.main()








