# mighty-botter
# Artificial Intelligence

from typing import Callable, List

from game_engine.util import raise_not_defined
from search_problems import SearchProblem



# def solve(problem: SearchProblem, heuristic: Callable) -> List[str]:
#     # TO-DO:: YOUR CODE HERE
#     raise_not_defined()



#___________________________________________________________________
#                     SOLUTION
#___________________________________________________________________
# if you want to implement your algorithm, comment everything below 
# here and uncomment above code to start working

#____________________________________________________________________

from search_strategies import SearchNode
from frontiers import PriorityQueue

def solve(problem: SearchProblem, heuristic: Callable) -> List[str]:
    """See 2_implementation_notes.md for more details.

    Your search algorithms needs to return a list of actions that reaches the
    goal from the start state in the given problem. The elements of this list
    need to be one or more references to the attributes NORTH, SOUTH, EAST and
    WEST of the class Directions.
    """

    pq = PriorityQueue()# Using priority queue data structure to expand on the minimum f-value node
    # Initialising queue using SearchNode class with initial state, and null/empty/0 values for root node, and 0 priority cost
    pq.push(SearchNode(state =problem.get_initial_state(), action = [], path_cost = 0, parent = None, depth = 0) , 0)
    
    seen = set() # Using set/"hash map" for checking membership is fastest 0(1)
    
    # Finding a path to required node using A* search
    # Continue processing queue until it becomes empty or the goal_test state has been reached
    # Following same structure as previous two algorithms for ease of reading
    while not pq.is_empty():
        searchnode =  pq.pop() # Extract lowest priority node from the queue, this is O(1)
        
        # If we have reached goal location, then return the path so far
        # action is concatenated list of all actions required to get to the location
        if problem.goal_test(searchnode.state):
            return searchnode.action
        
        # If the current state has not been seen, create new nodes with its succesors for exploration later in the priorityqueue
        if searchnode.state not in seen :
            seen.add(searchnode.state)
            
            # Iterating through succesors of the state, and pushing them into the priorityqueue
            # Note that the "parent" is the original searchnode itself
            # Concatenating the actions, adding the path costs, incrementing the depth
            for next_state, next_action, next_cost in problem.get_successors(searchnode.state):
                
                new_searchnode = SearchNode(state =next_state, action = searchnode.action + [next_action], path_cost = searchnode.path_cost + next_cost, parent = searchnode, depth = searchnode.depth +1)
                new_priority = new_searchnode.path_cost + heuristic(next_state, problem) # new_priority is the estimated total cost of path through this searchnode to goal state
                
                pq.push(new_searchnode, new_priority)
