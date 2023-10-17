from typing import List, Tuple
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from queue import Queue
import random
import json

app = FastAPI()
 
import debugpy
debugpy.listen(("0.0.0.0", 5678))

# Store the path history
path_history: List[Tuple[int, int]] = []

def create_maze(rows, cols, start, end):
    # Initialize maze with walls (1)
    maze = [[1] * cols for _ in range(rows)]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 1

    def dfs(x, y):
        maze[x][y] = 0  # Mark the current cell as a path (0)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            new_x, new_y = x + 2 * dx, y + 2 * dy
            if is_valid(new_x, new_y):
                maze[x + dx][y + dy] = 0
                dfs(new_x, new_y)

    dfs(start[0], start[1])

    # Set the start and end positions
    maze[start[0]][start[1]] = 2
    maze[end[0]][end[1]] = 3

    return maze

def bfs(maze, start, end, visited, path):
    queue = Queue()
    queue.put(start)
    
    while not queue.empty():
        current = queue.get()
        if current == end:
            break
        visited.add(current)
        
        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                queue.put(neighbor)
                path.append(neighbor)
                path_history.append(list(path))  # Store the path history

def get_neighbors(maze, current):
    neighbors = []
    right = (current[0], current[1] + 1)
    down = (current[0] + 1, current[1])
    left = (current[0], current[1] - 1)
    up = (current[0] - 1, current[1])
    
    directions = [right, down, left, up]
    
    for neighbor in directions:
        if (0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0])):
            if maze[neighbor[0]][neighbor[1]] != 1:
                if maze[neighbor[0]][neighbor[1]] == 0 or maze[neighbor[0]][neighbor[1]] == 3:
                    neighbors.append(neighbor)
        
    return neighbors

@app.get("/generate_maze", response_class=JSONResponse)
def generate_maze(request: Request):
    global path_history
    path_history = []  # Clear the old path history
    
    rows = 11
    cols = 11
    start = (0, 0)
    end = (random.randint(0, rows - 1), random.randint(0, cols - 1))
    
    maze = create_maze(rows, cols, start, end)
    
    visited = set()
    path = [start]
    bfs(maze, start, end, visited, path)
    
    # Return the maze and path history as JSON
    return {
        "maze": maze,
        "path_history": path_history,
        "start": start,
        "end": end
    }

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Read the content of your HTML file
    with open("./src/index.html", "r") as file:
        html_content = file.read()
    # Set the data-path-history attribute with the path history
    html_content = html_content.replace(
        '<div id="maze" class="mt-4">',
        f'<div id="maze" class="mt-4" data-path-history=\'{json.dumps(path_history)}\'>'
    )

    return HTMLResponse(content=html_content)

@app.get("/path_history", response_class=JSONResponse)
def get_path_history(request: Request):
    global path_history
    return JSONResponse(content=path_history)