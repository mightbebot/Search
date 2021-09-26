# ids_search.py
# mighty-botter

from typing import List

from game_engine.util import raise_not_defined
from search_problems import SearchProblem

from search_strategies import SearchNode
from frontiers import Queue , Stack

def solve(problem: SearchProblem) -> List[str]:
    max_depth = 100
    s = search(problem,max_depth)
    s.IIDS()


    return s.path()


# supporting classes
class Node(SearchNode):
    def __init__(self,state,action=None,path_cost=0,parent=None,depth=0,visited=None):
        super().__init__(state,action,path_cost,parent,depth)
        self.visited = visited


class search():
    def __init__(self,problem,depth):
        self.stack = None
        self.problem = problem
        self.max_depth   = depth

    def IIDS(self):
        for d in range(1, self.max_depth):
            r = self.DLS(d)
            if r == "cutoff":
                print("no solution at depth",d)
                continue
            if r == "goal":
                print("goal found depth",d)
                return 
        print("failure")
        raise ValueError


    # def DLS(self, current_depth):
    #     visited = set()
    #     self.stack = Stack() # memory reset
    #     self.stack.push(SearchNode(state=self.problem.get_initial_state(), action=[], path_cost=0, parent=None, depth=0))

    #     while not self.stack.is_empty():
    #         currentNode = self.stack.pop()
    #         if self.problem.goal_test(currentNode.state):
    #             return "goal"

    #         if currentNode.state not in visited:
    #             visited.add(currentNode.state)
    #             if currentNode.depth == current_depth:
    #                 return "cutoff"
    #             for succ, action, cost in self.problem.get_successors(currentNode.state):
    #                 # wall check
    #                 if self.problem.get_walls()[succ[0]][succ[1]]:
    #                     continue

                    
    #                 if self.problem.goal_test(succ):
    #                     return "goal"
    #                 self.stack.push(SearchNode(state=succ, action=action,path_cost=currentNode.path_cost+cost, parent=currentNode, depth=currentNode.depth+1 ))

    #     return "failure"
                    


    def DLS(self,depth):
        self.stack = Stack()
        self.visited = set()
        return self.r_DLS(depth,Node(state=self.problem.get_initial_state()))

    def r_DLS(self,limit,node):
        self.visited.add(node.state)
        if self.problem.goal_test(node.state): return "goal"
        if node.depth == limit: return "cutoff"

        for succ,action,cost in self.problem.get_successors(node.state):  
            # wall check
            if self.problem.get_walls()[succ[0]][succ[1]]:
                continue
            # loop check
            if succ in self.visited:
                continue

            self.visited.add(succ)
            succ = Node(state=succ,action=action,parent=node.state,depth=node.depth+1)
            
            self.stack.push(succ)
            r = self.r_DLS(limit=limit,node=succ)
            if r == "cutoff":
                garbage = self.stack.pop()
                continue
            if r == "goal":
                return r
        return "cutoff"


    def path(self):
        actions = []
        while not self.stack.is_empty():
            node = self.stack.pop()
            actions.append(node.action)
        return actions[::-1]







# def solve(problem: SearchProblem) -> List[str]:
#     """See 2_implementation_notes.md for more details.

#     Your search algorithms needs to return a list of actions that reaches the
#     goal from the start state in the given problem. The elements of this list
#     need to be one or more references to the attributes NORTH, SOUTH, EAST and
#     WEST of the class Directions.
#     """

#     # Remove this line when you have implemented Iterative Deepening Depth First Search
#     raise_not_defined()
#     # *** YOUR CODE HERE ***


# def DLS(problem,depth):
#     return RDLS(problem,depth,Node(state=problem.get_initial_state()))

# def R_DLS(problem,limit,node):
#     c_flag = False
#     if problem.goal_test(node.state): return node
#     if node.depth == limit: return False # cutoff

#     for succ,action,cost in problem.get_successors(node.state):
        
#         if problem.get_walls()[succ[0]][succ[1]]: continue
#         network.push(Node(state=succ,action=action,parent=node,depth=node.depth+1))
#         result = self.R_DLS(problem,limit,network[succ])
#         if result == False:
#          c_flag = True
#          network_stack.pop()
#         elif result is not None: return result
#     if c_flag: return False # cutoff
#     else: return None # failure

# def IIDS(max_depth):
#     for d in range(max_depth):
#         network = Stack()
#         r = DLS(problem,d,network)
#         if not(r == False) and r is not None: return r
#     return None







# def solve(problem: SearchProblem) -> List[str]:
#     max_depth = 

#     for d in range(max_depth):
#         network = Stack()
#         network.push(Node(state=problem.get_initial_state()))
#         if DLS(problem,d) is not None: return network
#         else: return None 
