from enum import Enum

class Status(Enum):
    YELLOW  = 1
    RED = 2
    SPECTATOR = 3

    def invert(self):
        if self == Status.YELLOW:
            return Status.RED
        elif self == Status.RED:
            return Status.YELLOW
        
    def __str__(self):
        if self == Status.YELLOW:
            return "1"
        if self == Status.RED:
            return "2"

class Connect4:
    def __init__(self):
        self.board = [[0]*7 for _ in range(6)]
        self.current_player = Status.YELLOW

    def __str__(self):
        string = []
        for row in self.board:
            for cell in row:
                string.append(f"{cell} | ")
            string.append("\n")
        return "".join(string)
    
    def drop(self, column):
        for row in reversed(range(6)):
            if self.board[row][column] == 0:
                self.board[row][column] = self.current_player
                self.current_player = self.current_player.invert()
                return True
        return False
    
    def play(self):
        while not self.isFinished() and not self.isComplete():
            print(self)
            value = input("Input some value")
            self.drop(int(value))

    def isFinished(self):
            board = self.board
            rows, cols = 6, 7

            for row in range(rows):
                for col in range(cols):
                    player = board[row][col]
                    if player == 0:
                        continue

                    # Horizontal →
                    if col + 3 < cols and all(board[row][col + i] == player for i in range(4)):
                        return True

                    # Vertical ↓
                    if row + 3 < rows and all(board[row + i][col] == player for i in range(4)):
                        return True

                    # Diagonal ↘
                    if row + 3 < rows and col + 3 < cols and all(board[row + i][col + i] == player for i in range(4)):
                        return True

                    # Diagonal ↙
                    if row + 3 < rows and col - 3 >= 0 and all(board[row + i][col - i] == player for i in range(4)):
                        return True
            return False


    def isComplete(self):
        row = 0
        for col in range(6):
            if self.board[row][col] == 0:
                return False
        return True


if __name__ == "__main__":
    game = Connect4()
    game.play()