from flask import Flask, render_template, jsonify

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
    
    i, j = row - 1, col + 1
    while i >= 0 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1
    
    return True

def solve_n_queens(n):
    board = [['X' for _ in range(n)] for _ in range(n)]
    solutions = []
    
    def n_queens(board, row):
        if row == len(board):
            solutions.append([row[:] for row in board])
            return
        
        for col in range(len(board)):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                n_queens(board, row + 1)
                board[row][col] = 'X'
    
    n_queens(board, 0)
    return solutions

class sol:

    def __init__(self):
        self.solutions=[]
    def sollen(self):
        return len(self.solutions)
    def sol(self,n):
        self.solutions=solve_n_queens(n)
        return self.solutions
    

app = Flask(__name__)
s=sol()
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/l/<int:n>')
def length(n):
    l=s.sollen()
    return jsonify(l)

@app.route('/solve/<int:n>')
def solve(n):
    solutions = s.sol(n)
    return jsonify(solutions)

if __name__ == "__main__":
    app.run()
