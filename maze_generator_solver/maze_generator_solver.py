import random
import time

# Maze dimensions (odd numbers work best)
WIDTH, HEIGHT = 21, 21

# Maze symbols
WALL = "█"
PATH = " "
START = "S"
END = "E"
VISITED = "·"

def initialize_maze():
    """Create a full wall maze."""
    return [[WALL for _ in range(WIDTH)] for _ in range(HEIGHT)]

def carve_passages(x, y, maze):
    """Generate maze using recursive DFS."""
    directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
    random.shuffle(directions)

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 1 <= nx < WIDTH-1 and 1 <= ny < HEIGHT-1 and maze[ny][nx] == WALL:
            maze[ny - dy//2][nx - dx//2] = PATH
            maze[ny][nx] = PATH
            carve_passages(nx, ny, maze)

def print_maze(maze):
    for row in maze:
        print("".join(row))
    print()

def solve_maze(maze, x, y, end_x, end_y, visited):
    """Simple DFS pathfinder."""
    if (x, y) == (end_x, end_y):
        maze[y][x] = END
        print_maze(maze)
        return True

    if maze[y][x] == WALL or (x, y) in visited:
        return False

    visited.add((x, y))
    maze[y][x] = VISITED
    print_maze(maze)
    time.sleep(0.05)  # visual effect

    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        if solve_maze(maze, x + dx, y + dy, end_x, end_y, visited):
            return True

    maze[y][x] = PATH
    return False

def main():
    maze = initialize_maze()
    maze[1][1] = PATH
    carve_passages(1, 1, maze)

    start_x, start_y = 1, 1
    end_x, end_y = WIDTH - 2, HEIGHT - 2
    maze[start_y][start_x] = START
    maze[end_y][end_x] = END

    print("🌀 Generated Maze:\n")
    print_maze(maze)

    input("Press Enter to see the solving process...\n")
    solve_maze(maze, start_x, start_y, end_x, end_y, set())

    print("\n✅ Maze solved!")

if __name__ == "__main__":
    main()
