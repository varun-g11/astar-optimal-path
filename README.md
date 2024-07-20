## Optimal Path Finding Using A* Algorithm

This repository contains the implementation of the A* search algorithm to find the shortest path in a grid-based environment. The algorithm is designed to navigate around obstacles while minimizing the total cost of reaching the goal.

### Overview

The A* algorithm is a widely used pathfinding algorithm in computer science and artificial intelligence. It is an informed search algorithm that efficiently finds the shortest path between two points on a graph or grid. A* combines the advantages of Dijkstra's algorithm (guaranteed shortest path) and greedy best-first search (efficiency) by using a heuristic to guide its search.

### How It Works

A* selects nodes from the open list with the lowest combined cost (actual cost + heuristic) for expansion, gradually moving towards the goal node. By intelligently prioritizing nodes to explore, A* can efficiently find the optimal path while avoiding unnecessary exploration of less promising paths.

One key feature of A* is its optimality and completeness under certain conditions, ensuring that it will always find the shortest path if one exists. However, the performance of A* heavily depends on the quality of the heuristic function used. A well-designed heuristic can significantly improve search efficiency by guiding A* towards the goal more effectively.

### Components

#### Class Definitions
- **Cell:** Represents a single cell in the grid. Each cell has attributes for its coordinates (x, y) and whether it is traversable.
- **Grid:** Initializes a grid of cells with a specified width and height. It also includes functions to manipulate individual cells, such as setting them as obstacles or checking their traversability status.

#### Distance Calculation
- **euclidean_distance:** Computes the Euclidean distance between two points in a two-dimensional space using the Pythagorean theorem.

#### A* Search Algorithm
- **a_star:** Performs the A* search algorithm to find the optimal path from a starting cell to a goal cell on the grid. It manages an open set as a priority queue to evaluate nodes based on their estimated total cost (f_score). The algorithm iterates through neighboring cells, updates the path if a better route is found, and adds unvisited neighbors to the open set until the goal cell is discovered.

#### Neighborhood Generation
- **get_neighbors:** Generates neighboring cells that are traversable and within the grid boundaries. It searches for cells in the cardinal directions (left, right, top, bottom) relative to the given cell.

#### Path Reconstruction
- **reconstruct_path:** Reconstructs the optimal path from the `came_from` dictionary generated during A* search. It traces the parent cells backward from the goal cell to the starting cell.

#### Graphical User Interface (GUI)
- **main:** Creates an interactive GUI using IPywidgets for users to input grid dimensions, add obstacles, set start and goal positions, and visualize the pathfinding process. When the visualize button is clicked, the grid, obstacles, start, goal, and optimal path are displayed using Matplotlib.

