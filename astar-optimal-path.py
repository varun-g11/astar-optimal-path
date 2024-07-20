import heapq
import math
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display
import numpy as np

class Cell:
    def __init__(self, x, y, traversable=True):
        self.x = x
        self.y = y
        self.traversable = traversable

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[Cell(x, y) for y in range(height)] for x in range(width)]

    def set_obstacle(self, x, y):
        self.grid[x][y].traversable = False

    def is_traversable(self, x, y):
        return self.grid[x][y].traversable

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def a_star(grid, start, goal):
    open_set = [(0, id(start), start)]
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, _, current = heapq.heappop(open_set)
        if current == goal:
            return reconstruct_path(came_from, goal)

        for neighbor in get_neighbors(grid, current):
            tentative_g_score = g_score[current] + 1  # Assuming each move costs 1
            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + euclidean_distance(neighbor.x, neighbor.y, goal.x, goal.y)
                heapq.heappush(open_set, (float(f_score), id(neighbor), neighbor))  # Pushing with unique identifier

    return None  # No path found


def get_neighbors(grid, cell):
    neighbors = []
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_x, new_y = cell.x + dx, cell.y + dy
        if 0 <= new_x < grid.width and 0 <= new_y < grid.height and grid.is_traversable(new_x, new_y):
            neighbors.append(grid.grid[new_x][new_y])
    return neighbors

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]  # Reverse the path to start from the beginning

def visualize(grid, start, goal):
    path = a_star(grid, start, goal)
    if path is None:
        print("No path found")
        return

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(0, grid.width)
    ax.set_ylim(0, grid.height)
    ax.set_aspect('equal', adjustable='box')

    for x in range(grid.width):
        for y in range(grid.height):
            cell = grid.grid[x][y]
            if not cell.traversable:
                ax.add_patch(plt.Rectangle((x, y), 1, 1, color='black'))

    for cell in path:
        ax.add_patch(plt.Rectangle((cell.x, cell.y), 1, 1, color='green'))

    ax.plot(start.x + 0.5, start.y + 0.5, 'ob', markersize=15)  # Start point
    ax.plot(goal.x + 0.5, goal.y + 0.5, 'or', markersize=15)  # Goal point

    ax.grid(True)
    ax.invert_yaxis()
    plt.show()

def main():
    style = {'description_width': 'initial'}
    width = widgets.IntSlider(description="Width:", min=5, max=20, value=10, style=style)
    height = widgets.IntSlider(description="Height:", min=5, max=20, value=10, style=style)
    obstacles_button = widgets.Button(description="Add Obstacle", style=style)
    obstacle_x = widgets.IntSlider(description="X:", min=0, max=width.value-1, value=0, style=style)
    obstacle_y = widgets.IntSlider(description="Y:", min=0, max=height.value-1, value=0, style=style)
    start_x = widgets.IntSlider(description="Start X:", min=0, max=width.value-1, value=0, style=style)
    start_y = widgets.IntSlider(description="Start Y:", min=0, max=height.value-1, value=0, style=style)
    goal_x = widgets.IntSlider(description="Goal X:", min=0, max=width.value-1, value=width.value-1, style=style)
    goal_y = widgets.IntSlider(description="Goal Y:", min=0, max=height.value-1, value=height.value-1, style=style)
    visualize_button = widgets.Button(description="Visualize", style=style)
    
    obstacles = []

    def add_obstacle(b):
        x = obstacle_x.value
        y = obstacle_y.value
        if (x, y) not in obstacles:
            obstacles.append((x, y))
            grid.set_obstacle(x, y)

    def on_visualize_button_clicked(b):
        grid = Grid(width.value, height.value)
        for x, y in obstacles:
            grid.set_obstacle(x, y)
        start = grid.grid[start_x.value][start_y.value]
        goal = grid.grid[goal_x.value][goal_y.value]
        visualize(grid, start, goal)

    obstacles_button.on_click(add_obstacle)
    visualize_button.on_click(on_visualize_button_clicked)

    display(widgets.VBox([
        widgets.HBox([width, height]),
        widgets.HBox([obstacle_x, obstacle_y, obstacles_button]),
        widgets.HBox([start_x, start_y]),
        widgets.HBox([goal_x, goal_y]),
        visualize_button
    ]))

if __name__ == "__main__":
    main()
