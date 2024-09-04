class TicTacToe:
    def __init__(self):
        self.board = [[" "] * 3 for i in range(3)]
        self._current = "X"
    
    def move(self):
        print("It is " + self._current +"'s turn.\n")
        print("Here is the board.")

        for row in self.board:
            print(row)
        
        print("In which position would you like to play?\nInput it into the console with the following format: 'row column'.\n-> ", end ="")
        while True:
            try:
                position = self.parse_position()
                break
            except:
                print("Invalid input. Try again.\n->", end = "")
                continue

        self.board[position[0]][position[1]] = self._current
        
        print("Here is the board after your move.")

        for row in self.board:
            print(row)

    def move_checker(self, position):
        if len(position) != 2:
            raise ValueError("Input a two-list of position")
        
        if self.board[position[0]][position[1]] == " ":
            return True
        else:
            return False
    
    def parse_position(self):
        argument = input()

        if len(argument) != 3:
            raise ValueError("Input should be of the format 'row column'.")
        else:
            pass

        position = [int(pos) for pos in list(argument.replace(" ", ""))]

        if self.move_checker(position):
            pass
        else:
            raise ValueError("Position not empty.")
        
        return position
    
    def gameover(self):
        for row in self.board:
            for entry in row:
                if entry == " ":
                    return False
        
        print("Game over. It's a tie.")
        return True
    
    def player_switch(self):
        if self._current == "X":
            self._current = "O"
        else:
            self._current = "X"

    def winner(self):
        # Vertical
        win_boolean = False

        for rank in range(3):
            count = 0
            for row in self.board:
                if row[rank] == self._current:
                    count += 1
                    pass
                else:
                    break

                if count == 3:
                    win_boolean = True

                    return win_boolean

        # Horizontal
        for row in self.board:
            count = 0
            for element in row:
                if element == self._current:
                    count += 1
                    pass
                else:
                    win_boolean = False
                    break
                
                if count == 3:
                    win_boolean = True

                    return win_boolean
            
        # Diagonal
        if (self.board[0][0] == self._current and self.board[1][1] == self._current and self.board[2][2] == self._current) \
            or (self.board[0][2] == self._current and self.board[1][1] == self._current and self.board[2][0] == self._current): # Did not index well here. As a result, game wasn't appropriately checking for win.
            win_boolean = True # Had a `==` instead of a `=` here. Silly me.
            
            return win_boolean

def main():
    game = TicTacToe()
    while not game.gameover():
        game.move()

        if game.winner():
            print(game._current + " is the winner.")
            print("Game over.")
            break
        game.player_switch()


if __name__ == "__main__":
    main()