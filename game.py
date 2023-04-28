class Game:
  def __init__(self):
    self.board = [['', '', ''] for _ in range(3)]
    self.current_player = 'X'
    self.winner = None
    self.game_over = False

  def toggle_player(self):
    if self.current_player == 'X':
      self.current_player = 'O'
    else:
      self.current_player = 'X'

  def play_move(self, row, col):
    print("Received move:", row, col)
    if self.board[row][col] == '':
      self.board[row][col] = self.current_player
      self.check_for_winner()
      self.toggle_player()

  def check_for_winner(self):
    # Check rows
    for row in self.board:
      if row.count(row[0]) == len(row) and row[0] != '':
        self.winner = row[0]
        self.game_over = True
        return

    # Check columns
    for col in range(len(self.board[0])):
      if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != '':
        self.winner = self.board[0][col]
        self.game_over = True
        return

    # Check diagonals
    if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != '':
      self.winner = self.board[0][0]
      self.game_over = True
      return

    if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != '':
      self.winner = self.board[0][2]
      self.game_over = True
      return

    # Check for tie
    if all(cell != '' for row in self.board for cell in row):
      self.game_over = True

