from Point import Point

class Board:
    def __init__(self, row=0,column=0):
        self._row=row
        self._column=column
        self._board=[]

    def get_row(self):
        return self._row

    def get_column(self):
        return self._column

    def set_row(self, row):
        self._row=row

    def set_column(self, column):
        self._column=column

    def ok_move(self):
        move=[]
        for x in range(self.get_row()):
            for y in range(self.get_column()):
                if self._board[x][y]==0:
                    move.append(Point(x,y))

        return move

    def board_move(self,point):
        x=point.get_x()
        y=point.get_y()

        if x-1>=0 and y-1>=0 and self._board[x-1][y-1]==0:
            self._board[x-1][y-1]=-1
        if x-1>=0 and y+1<self._column and self._board[x-1][y+1]==0:
            self._board[x-1][y+1]=-1

        if x-1>=0 and self._board[x-1][y]==0:
            self._board[x-1][y]=-1
        if y-1>=0 and self._board[x][y-1]==0:
            self._board[x][y-1]=-1

        if y+1< self._column and self._board[x][y+1]==0:
            self._board[x][y+1]=-1
        if x+1<self._row and self._board[x+1][y]==0:
            self._board[x+1][y]=-1
        if x+1<self._row and y+1 < self._column and self._board[x+1][y+1]==0:
            self._board[x+1][y+1]=-1
        if x+1<self._row and y-1>=0 and self._board[x+1][y-1]==0:
            self._board[x+1][y-1]=-1

    def __len__(self):
        return len(self._board)

    def __str__(self):
        s="\n "
        for x in range(self._column):
            s=s+" "+str(x)+"   "
        for x in range(self._row):
            s=s+"\n"
            s=s+"-"*(4*self._column+1)
            s=s+"\n"
            s=s+str(x)+" |"
            for y in range(self._column):
                if self._board[x][y]==1:
                    s=s+" "+"X"+" "+"|"
                elif self._board[x][y]==2:
                    s=s+" "+"0"+" "+"| "
                elif self._board[x][y]==-1:
                    s=s+" * "+"|"
                else:
                    s=s+" "+" "+" "+"|"
            s=s+"\n"
            s=s+"-"*(4*self._column+1)+"\n"
        return s

    def get_board(self):
        return self._board


    def create_board(self):
        for x in range(self._row):
            row=[]
            for y in range(self._column):
                row.append(0)
            self._board.append(row)

    def clear_board(self):
        self._board=[]
        self._row=0
        self._column=0

class ValidatePoint:
    @staticmethod
    def validate_point(x,y,board):
        try:
            x=int(x)
            y=int(y)
        except ValueError:
            raise Exception("need integers")
        if y<0 or x<0 or y>board.get_column() or x>board.get_row():
            raise Exception("point out of border")
        if board.get_board()[x][y]==-1 or board.get_board()[x][y]==1 or board.get_board()[x][y]==2:
            raise Exception("square taken")










