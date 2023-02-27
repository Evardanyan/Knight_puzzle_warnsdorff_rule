def get_moves(x, y, w, h, visited):
    """Returns a list of all possible moves from the current position."""
    moves = []
    for dx, dy in ((2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)):
        nx, ny = x + dx, y + dy
        if 1 <= nx <= w and 1 <= ny <= h and (nx, ny) not in visited:
            moves.append((nx, ny))
    return moves


def get_degree(x, y, w, h, visited):
    """Returns the number of possible moves from the current position."""
    return len([1 for dx, dy in ((2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1))
                if 1 <= x + dx <= w and 1 <= y + dy <= h and (x + dx, y + dy) not in visited])


def warnsdorff(start_x, start_y, w, h, visited=None, path=None):
    """Finds a knight's tour using Warnsdorff's rule."""
    if visited is None:
        visited = set()
        visited.add((start_x, start_y))
    if path is None:
        path = [(start_x, start_y)]
    if len(visited) == h * w:
        return path
    x, y = path[-1]
    moves = [(nx, ny, get_degree(nx, ny, w, h, visited)) for nx, ny in get_moves(x, y, w, h, visited)]
    if not moves:
        return None
    nx, ny, _ = min(moves, key=lambda m: m[2])
    visited.add((nx, ny))
    path.append((nx, ny))
    solution = warnsdorff(nx, ny, w, h, visited, path)
    if solution is not None:
        return solution
    visited.remove((nx, ny))
    path.pop()
    return None


def print_board(path, w, h):
    board = [[0] * w for _ in range(h)]
    for i, (x, y) in enumerate(path):
        board[y - 1][x - 1] = i + 1
    print("Here's the solution!")
    print(" ------------------")
    for i in range(h - 1, -1, -1):
        print("{}|".format(i + 1), end="")
        for j in range(w):
            print("{:3}".format(board[i][j]), end="")
        print(" |")
    print(" ------------------")
    print("   ", end="")
    for i in range(1, w + 1):
        print('{:2}'.format(i), end=" ")
    print()
