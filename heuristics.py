# heuristics.py
# ----------------
# Artificial Intelligence
# mighty-botter

""" This class contains heuristics which are used for the search procedures that
    you write in search_strategies.py.

    The first part of the file contains heuristics to be used with the algorithms
    that you will find in search_strategies.py.

    In the second part you will write a heuristic for Q4 to be used with a
    MultiplePositionSearchProblem.
"""

from typing import Tuple

from search_problems import (MultiplePositionSearchProblem,
                             PositionSearchProblem)

Position = Tuple[int, int]
YellowBirds = Tuple[Position]
State = Tuple[Position, YellowBirds]

# -------------------------------------------------------------------------------
# A set of heuristics which are used with a PositionSearchProblem
# You do not need to modify any of these.
# -------------------------------------------------------------------------------


def null_heuristic(pos: Position, problem: PositionSearchProblem) -> int:
    """The null heuristic. It is fast but uninformative. It always returns 0"""

    return 0


def manhattan_heuristic(pos: Position, problem: PositionSearchProblem) -> int:
    """The Manhattan distance heuristic for a PositionSearchProblem."""

    return abs(pos[0] - problem.goal_pos[0]) + abs(pos[1] - problem.goal_pos[1])


def euclidean_heuristic(pos: Position, problem: PositionSearchProblem) -> float:
    """The Euclidean distance heuristic for a PositionSearchProblem"""

    return ((pos[0] - problem.goal_pos[0]) ** 2 + (pos[1] - problem.goal_pos[1]) ** 2) ** 0.5


# Abbreviations
null = null_heuristic
manhattan = manhattan_heuristic
euclidean = euclidean_heuristic

# -------------------------------------------------------------------------------
# You have to implement the following heuristics for task 4 of the project.
# It is used with a MultiplePositionSearchProblem
# -------------------------------------------------------------------------------

# You can make helper functions here, if you need them


def bird_counting_heuristic(state: State,
                            problem: MultiplePositionSearchProblem) -> float:
    position, yellow_birds = state
    heuristic_value = len(yellow_birds) # it is just the length of the yello_birds

    return heuristic_value


bch = bird_counting_heuristic


def every_bird_heuristic(state: State,
                         problem: MultiplePositionSearchProblem) -> float:
    position, yellow_birds = state
    
    # From graph theory maths - least expensive path between nodes is the minimum spanning tree which is the most optimum (I think?) type of heuristic in this case
    # https://en.wikipedia.org/wiki/Minimum_spanning_tree 
    # We can create a min spanning tree between all the birds using Kruskals algorithm and similar data structures from the following algorithms
    #  https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/ 
    # https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
    # This is an admissible and informative heurisitc, as it finds the min number of steps that birds can be collected
    # It is efficient -> works really fast on the hardest maze. 
        # ./test.sh heuristic every_bird mazeMultiSearch
        # [SearchAgent] using function astar and heuristic every_bird_heuristic
        # [SearchAgent] using problem type MultiplePositionSearchProblem 
        # Search time 0.06577700000000003 seconds
        # Path found with total cost of 215 in 0.068181 seconds
        # Search nodes expanded: 474

    # Convert the yellow birds location into a list
    remaining_birds_list = list(yellow_birds)
    remaining_birds_number = len(remaining_birds_list)

    # If no birds then game is over => heuristic = 0
    if remaining_birds_number == 0:
        return 0

    # Find nearest bird distance
    bird_distances_from_current_position = [problem.maze_distance(position, each_location) for each_location in remaining_birds_list]
    nearest_bird_distance = min(bird_distances_from_current_position)

    # Find distances between each birds
    distance_between_yellow_birds_list = []
    for grid_x in range(remaining_birds_number):
        for grid_y in range(grid_x, remaining_birds_number):
            if grid_x != grid_y:
                bird_x , bird_y = remaining_birds_list[grid_x], remaining_birds_list[grid_y]
                dist = problem.maze_distance(remaining_birds_list[grid_y] , remaining_birds_list[grid_x])
                distance_between_yellow_birds_list.append((dist , bird_x , bird_y))
    
    # Sort in ascending order
    distance_between_yellow_birds_list = sorted(distance_between_yellow_birds_list, key= lambda x:x[0])

    # Starting min span tree search
    parent_tree = {}
    ordering_tree = {}

    # Recursively find root/mother node
    def path_finding_recursion(index, mother):
        if mother[index] is None:
            return index
        return path_finding_recursion(mother[index], mother)
    
    # Function similar to "union" in above link
    # Combines trees based on heirarchy
    def combine_trees(parent, order, x, y):
        bird_x = path_finding_recursion(x, parent) 
        bird_y = path_finding_recursion(y, parent) 

        # Whoever is younger gets combined under elder tree
        # If both same generation, Otherwise doesnt matter, join one under the other
        if order[bird_x] > order[bird_y]:
            parent[bird_y] = bird_x
        elif order[bird_x] < order[bird_y]: 
            parent[bird_x] = bird_y
        else:
            parent[bird_x] = bird_y
            order[bird_y] += 1

    # Init to 0
    for Tuple in remaining_birds_list:
        parent_tree[Tuple] = None
        ordering_tree[Tuple] = 0
    
    # Initialise with 0
    counter = 0
    min_spanning_distance = 0 
    i = 0
    while counter < remaining_birds_number -1: # Loop until each bird cost has been added
        # Starting from the smallest distance we find path
        cost , grid_x, grid_y = distance_between_yellow_birds_list[i]        
        i+=1
        bird_x = path_finding_recursion(grid_x, parent_tree)
        bird_y = path_finding_recursion(grid_y, parent_tree)

        # Check if cyclic graph made, else increment and combine tree. Otherwise continue processing
        if bird_x != bird_y:             
            counter += 1
            min_spanning_distance += cost
            combine_trees(parent_tree, ordering_tree, bird_x, bird_y)

    return nearest_bird_distance + min_spanning_distance

every_bird = every_bird_heuristic
