from Board import Board
from Controller import Controller
from Console import Console

controller=Controller(Board())
ui=Console(controller)
ui.start()