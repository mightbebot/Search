# minimax_agent.py
# --------------
# Artificial Intelligence
# mighty-botter



from typing import Tuple
import operator
from agents import Agent
from game_engine.actions import Directions
from search_problems import AdversarialSearchProblem

Position = Tuple[int, int]
Positions = Tuple[Position]
State = Tuple[int, Position, Position, Positions, float, float]

import numpy as np

def manhattan_heuristic(pos1: Position, pos2: Position) -> int:
    """The Manhattan distance heuristic for a PositionSearchProblem."""

    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def euclidean_heuristic(pos1: Position, pos2: Position) -> float:
    """The Euclidean distance heuristic for a PositionSearchProblem"""

    return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5

class MinimaxAgent(Agent):
    """ The agent you will implement to compete with the black bird to try and
        save as many yellow birds as possible. """

    def __init__(self, max_player, depth="2"):
        """ Make a new Adversarial agent with the optional depth argument.
        """
        self.max_player = max_player
        self.depth = int(depth)

    def evaluation(self, problem: AdversarialSearchProblem, state: State) -> float:
        """
            (MinimaxAgent, AdversarialSearchProblem,
                (int, (int, int), (int, int), ((int, int)), number, number))
                    -> number
            Returned evaluation is sum of score + food_contribution + black_contribution
        """
        player, red_pos, black_pos, yellow_birds, score, yb_score = state
        evaluation = 0

        remaining_birds_list = list(yellow_birds)
        remaining_birds = len(remaining_birds_list)

        # game over
        if remaining_birds == 0:
          return float("inf")
        # total_prize = remaining_birds*yb_score # This shrinks rapidly 

        # Reciprocal of average distance to birds is used, as on avg it will lead red closer to the food
        bird_distances_from_current_position = [ 1.0 / problem.maze_distance(red_pos, each_location) for each_location in remaining_birds_list]
        # nearest_bird_distance = min(bird_distances_from_current_position)
        
        # this is bounded at 10 
        # food_contribution is 10 * avg of reciprocal distance
        food_contribution = 10 * float(sum(bird_distances_from_current_position)) / len(bird_distances_from_current_position)

        # If black is nearby is bad for red, so negative distance 
        black_contribution = - problem.maze_distance(red_pos, black_pos) / 3.0

        evaluation = score + food_contribution + black_contribution
        return evaluation

    def maximize(self, problem: AdversarialSearchProblem, state: State,
                 current_depth: int, alpha=float('-inf'), beta=float('inf')) -> Tuple[float, str]:
        """ This method should return a pair (max_utility, max_action).
            The alpha and beta parameters can be ignored if you are
            implementing minimax without alpha-beta pruning.
        """
        # Following the minimax with alpha-beta pruning algorithm from lecture slides 6 and 7 and textbook Chap 5, pg 170
       
        # Check if terminal state, return utility
        if problem.terminal_test(state):
            return problem.utility(state)
        
        # If cutoff reached return evaluation function
        if current_depth == self.depth:
            return self.evaluation(problem, state)

        # Initialise action to return STOP if nothing found. v_max as -inf
        max_value_v , max_action = float("-inf"), Directions.STOP

        # To iterate over the successors of a given state s
        # cost is 1 so not needed
        for next_state, new_action, _ in problem.get_successors(state):
            # Recursive call to min with the next state
            current_evaluated_v = self.minimize(problem,next_state,current_depth+1)

            # Keeping the highest evaluation and action only
            if current_evaluated_v > max_value_v: 
              max_value_v = current_evaluated_v
              max_action = new_action
            
            # Alpha-beta pruning step
            if max_value_v > beta:
              # print("Pruned maxi")
              return max_value_v
            alpha = max(alpha,max_value_v) # Update alpha

        # Polymorphic return
        # For root node return the tuple required, 
        # For non-root return the maximum evaluated v in the current branch
        if current_depth > 0:
            return max_value_v
        else:
            return (max_value_v , max_action)


    def minimize(self, problem: AdversarialSearchProblem, state: State,
                 current_depth: int, alpha=float('-inf'), beta=float('inf')) -> float:
        """ This function should just return the minimum utility.
            The alpha and beta parameters can be ignored if you are
            implementing minimax without alpha-beta pruning.
        """
         # Check if terminal state, return utility
        if problem.terminal_test(state):
          # print("Terminal in mini", "curr depth:", current_depth, "self.depth", self.depth)
            return problem.utility(state)
        
        # If cutoff reached return evaluation function
        if current_depth == self.depth:
          # print("cutoff mini")
            return self.evaluation(problem, state)
        
        # v_min as inf
        min_value_v = float("inf")

        # To iterate over the successors of a given state s
        # cost is 1 so not needed
        for next_state, _, _ in problem.get_successors(state):
            
            # Recursive call to max with the next state
            current_evaluated_v = self.maximize(problem, next_state, current_depth + 1, alpha, beta)
            
            # Keeping the lowest evaluation only as that is min best move
            if current_evaluated_v < min_value_v:
              min_value_v = current_evaluated_v
            
            # Alpha-beta pruning step
            if beta < alpha:
              return beta
            beta = min(beta, min_value_v) # Update beta
        # Return the minimum v
        return min_value_v


    def get_action(self, game_state):
        """ This method is called by the system to solicit an action from
            MinimaxAgent. It is passed in a State object.

            Like with all of the other search problems, we have abstracted
            away the details of the game state by producing a SearchProblem.
            You will use the states of this AdversarialSearchProblem to
            implement your minimax procedure. The details you need to know
            are explained at the top of this file.
        """
        # We tell the search problem what the current state is and which player
        # is the maximizing player (i.e. who's turn it is now).
        problem = AdversarialSearchProblem(game_state, self.max_player)
        state = problem.get_initial_state()
        utility, max_action = self.maximize(problem, state, 0)
        print("At Root: Utility:", utility, "Action:",
              max_action, "Expanded:", problem._expanded)
        return max_action
