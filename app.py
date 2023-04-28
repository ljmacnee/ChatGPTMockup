from flask import Flask, jsonify,request, render_template
from game import Game

app = Flask(__name__)

# Instantiate the Game class
game = Game()

@app.route('/')
def index():
    return render_template('index.html')

# Route to get the current game board state
@app.route('/game_board')
def game_board():
    return jsonify(game.board)

@app.route('/play_move', methods=['POST'])
def play_move():
    data = request.get_json()
    row = data['row']
    col = data['col']

    # Check if the game is over
    if game.game_over:
        return jsonify({'error': 'Game over'})

    # Check if the move is valid
    if not (0 <= row <= 2 and 0 <= col <= 2 and game.board[row][col] == ''):
        return jsonify({'error': 'Invalid move'})

    # Call the play_move method of the Game instance
    game.play_move(row, col)

    # Check if there is a winner
    if game.winner:
        status = f'{game.winner} wins!'
    elif game.game_over:
        status = 'It\'s a tie!'
    else:
        status = f"It's {game.current_player}'s turn"

    # Return a JSON response with the updated board state and game status
    return jsonify({'board': game.board, 'status': status, 'symbol': game.current_player})


if __name__ == '__main__':
    app.run(debug=True)