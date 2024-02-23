class Console:
    def __init__(self,controller):
        self._controller=controller
        self._computerstart=False
        self._in_turn=1

    def start(self):
        continue_game=True
        while continue_game:
            try:
                x=int(input("board's height:"))
                y=int(input("board's width:"))
                if x<1 or y<1:
                    raise ValueError
                set_player=input("do you want to start?\n a)yes\nb)no")
                self._controller.set_row(x)
                self._controller.set_column(y)
                self._controller.create_board()

                if set_player=='a':
                    self._in_turn=1
                    self._computerstart=False
                elif set_player=='b':
                    self._in_turn=2
                    self._computerstart=True

                while self._controller.game_over():
                    if self._in_turn==1:
                        try:
                            print(str(self._controller.get_board()))
                            x=int(input("x="))
                            y=int(input("y="))
                            self._controller.player_move(x,y)
                            self._in_turn=2
                        except Exception as error:
                            print(error)
                    elif self._in_turn==2:
                        self._controller.move_ai(self._computerstart,x,y)

                        self._in_turn=1
                print(str(self._controller.get_board()))
                if self._in_turn==2:
                    print("you have won")
                else:
                    print("computer won")
                cont=input("You want another round?\na)yes\nb)no")
                if cont =='a':
                    self._controller.destroy_board()
                elif cont=='b':
                    continue_game=False
                else:
                    print("invalid option")
            except ValueError:
                print("invalid coordinates")




