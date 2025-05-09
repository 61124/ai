import heapq

class Node:
    def __init__(self, board, g, h):
        self.board = board  # The board configuration
        self.g = g          # Cost from the start node
        self.h = h          # Heuristic cost (number of attacking pairs)
        self.f = g + h      # Total cost

    def __lt__(self, other):
        return self.f < other.f  # For priority queue sorting

def heuristic(board):
    h = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                h += 1
    return h

def get_successors(board):
    successors = []
    n = len(board)
    for row in range(n):
        for col in range(n):
            if board[row] != col:  # Move queen to a new column
                new_board = board[:]
                new_board[row] = col
                successors.append(new_board)
    return successors

def solve_n_queens(n=8):
    if n==3 or n==2:
        return None
    open_list=[]
    initial_board=[0]*n
    heapq.heappush(open_list,Node(initial_board,0,heauristic(initial_board)))
    while open_list:
        node = heapq.heappop(open_list)
        board = node.board
        if node.h == 0:
            return board
            # print_board(board)
        for successor in get_successors(board):
            h=heauristic(successor)
            heapq.heappush(open_list,Node(successor,node.g+1,h))
    return None

def print_board(board):
    if board:
        for row in range(len(board)):
            line = ['.'] * len(board)
            line[board[row]] = 'Q'
            print(''.join(line))
    else:
        print("No solution found.")

# Solve and print the board
solution = solve_n_queens()
print_board(solution)
