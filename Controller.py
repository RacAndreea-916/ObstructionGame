from Board import ValidatePoint
from Point import Point
from random import randint

class Controller:
    def __init__(self,board):
        self._board=board
        self._valid=ValidatePoint()
        self._aifirst=False

    def get_board(self):
        return self._board
    def set_row(self,row):
        self._board.set_row(row)

    def set_column(self,column):
        self._board.set_column(column)
    def create_board(self):
        self._board.create_board()
        self._aifirst=False
    def destroy_board(self):
        self._board.clear_board()

    def player_move(self,x,y):
        self._valid.validate_point(x,y,self._board)
        point=Point(x,y)
        self._board.get_board()[point.get_x()][point.get_y()]=1
        self._board.board_move(point)

    def check_odd(self,x,y):
        return x%2 and y%2

    def get_mirror(self,x,y):
        row=self._board.get_row()
        column=self._board.get_column()

        if self._board.get_board()[row-x-1][column-y-1]==0:
            return Point(row-x-1,column-y-1)
        if self._board.get_board()[x][column-y-1]==0:
            return Point(x,column-y-1)
        if self._board.get_board()[row-x-1][y]==0:
            return Point(row-x-1,y)

    def decide_move(self,computer,row,column,moves):
        if computer==True and len(moves)==row*column:
            if self.check_odd(row,column):
                return 1
        if self._aifirst==True and len(moves)!=row*column:
            return 1
        return 2

    def first_odd(self,row, column,moves, x, y):
        if len(moves)==row*column:
            row_x=row//2
            column_y=column//2
            self._board.get_board()[int(row_x)][int(column_y)]=2
            move=Point(row_x,column_y)
            self._board.board_move(move)
            self._aifirst=True
            return move


        if len(moves)!=row*column:
            move=self.get_mirror(int(x),int(y))
            self._board.get_board()[int(move.get_x())][int(move.get_y())]=2
            self._board.board_move(move)
            return move

    def random_move(self,moves):
        move =randint(0,len(moves)-1)
        self._board.get_board()[moves[move].get_x()][moves[move].get_y()]=2
        self._board.board_move(moves[move])
        return moves[move]

    def move_ai(self,computer,x,y):
        moves=self._board.ok_move()
        row=self._board.get_row()
        column=self._board.get_column()
        next_move=self.decide_move(computer,row,column,moves)

        if next_move == 1:
            return self.first_odd(row, column, moves, x, y)
        elif next_move == 2:

            return self.random_move(moves)

    def game_over(self):
        if self._board.ok_move():
            return True
        return False





