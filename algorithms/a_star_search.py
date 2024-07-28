# author:   trieunvt
# file:     a_star_search.py
# date:     28 Jul 2024
# version:  v1.0.0
# brief:    The A* search algorithm implementation.

import math as m
import numpy as np

# User-defined macros
SEARCH_MAZE     = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 1, 0, 0],
                   [0, 0, 1, 1, 1, 1, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0]]
START_POINT     = (0, 0)
END_POINT       = (8, 8)
WALKABLE_VALUE  = 0
PATH_VALUE      = 9

# The neighbor square
neighbor_square = [(-1, -1), (-1, 0), (-1, 1),
                   ( 0, -1),          ( 0, 1),
                   ( 1, -1), ( 1, 0), ( 1, 1)]

# neighbor_square = [          (-1, 0),
#                    ( 0, -1),          ( 0, 1),
#                              ( 1, 0)]

# The A* search algorithm node class
class Node():
    def __init__(self, parent = None, position = None) -> None:
        self.f = 0
        self.g = 0
        self.h = 0
        self.position = position
        self.parent = parent

    def __eq__(self, other) -> bool:
        return self.position == other.position

# The A* search algorithm implementation
def a_star_search(search_maze, start_point, end_point):
    # Create start and end nodes
    start_node = Node(None, start_point)
    end_node = Node(None, end_point)

    # Create open (with the start node) and closed lists
    open_list = []
    open_list.append(start_node)
    closed_list = []

    # Loop until reaching the end node or the open list is empty
    while len(open_list) > 0:
        # Find the current node in the open list
        current_index = 0
        current_node = open_list[0]
        for index, node in enumerate(open_list):
            if node.f < current_node.f:
                current_index = index
                current_node = node

        # Pop the current node off the open list and append it to the closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Reached the end node
        if end_node == current_node:
            search_path = []
            while current_node is not None:
                search_path.insert(0, current_node.position)
                current_node = current_node.parent

            return search_path

        # Create neighbor nodes of the current node and append to the open list
        for neighbor_position in neighbor_square:
            # Add the neighbor position to the current node position
            neighbor_position = (current_node.position[0] + neighbor_position[0],
                                 current_node.position[1] + neighbor_position[1])

            # Make sure the neighbor position within the search maze's range and in the walkable terrain
            if 0 <= neighbor_position[0] < len(search_maze) \
            and 0 <= neighbor_position[1] < len(search_maze[0]) \
            and WALKABLE_VALUE == search_maze[neighbor_position[0]][neighbor_position[1]]:
                # Create the new neighbor node
                neighbor_node = Node(current_node, neighbor_position)

                # Check the neighbor node's existence in the closed list
                is_existed = False
                for closed_node in closed_list:
                    if closed_node == neighbor_node:
                        is_existed = True

                if (True == is_existed): continue

                # Create the f, g, and h values
                neighbor_node.g = current_node.g + 1
                neighbor_node.h = m.sqrt((neighbor_node.position[0] - end_node.position[0]) ** 2 +
                                         (neighbor_node.position[1] - end_node.position[1]) ** 2)
                neighbor_node.f = neighbor_node.g + neighbor_node.h

                # Check the neighbor node's existence in the open list
                for open_node in open_list:
                    if open_node == neighbor_node and open_node.g < neighbor_node.g:
                        is_existed = True

                if (True == is_existed): continue

                # Append the neighbor node to the open list
                open_list.append(neighbor_node)

    return "The search path not found!"

# The main program
def main():
    print("A* SEARCH ALGORITHM", end="\n\n")

    # Create the search maze
    search_maze = SEARCH_MAZE
    print("The search maze:")
    print(np.matrix(search_maze), end="\n\n")

    # Create the start and end points
    start_point = START_POINT
    end_point = END_POINT
    print("The start point: ", start_point)
    print("The end point:   ", end_point, end="\n\n")

    # The example
    search_path = a_star_search(search_maze, start_point, end_point)
    print("Points of the search path:")
    print(search_path, end="\n\n")

    # The result visualization
    for point in search_path:
        search_maze[point[0]][point[1]] = PATH_VALUE

    print("Visualization of the search path:")
    print(np.matrix(search_maze))

if __name__ == "__main__":
    main()
