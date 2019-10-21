# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        closest_ghost = min([manhattanDistance(newPos, ghost.getPosition()) for ghost in newGhostStates])

        # closer ghost lead to smaller score
        if closest_ghost:
            ghost_dist = -5 / closest_ghost
        else:
            ghost_dist = -1000

        newFood = newFood.asList()

        # closer food lead to bigger score
        if len(newFood):
            food_dist = -min([manhattanDistance(newPos, food) for food in newFood])
        else:
            food_dist = 0

        # more food left lead to smaller score
        food_left = -100 * len(newFood)

        score = food_dist + ghost_dist + food_left

        return score

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"

        def minimax(state, index, depth):
            if index == state.getNumAgents():
                if depth == self.depth:
                    return self.evaluationFunction(state)
                return minimax(state, 0, depth + 1)

            actions = state.getLegalActions(index)
            if len(actions) == 0:
                return self.evaluationFunction(state)
            next_states = [minimax(state.generateSuccessor(index, action), index + 1, depth) for action in actions]
            if index == 0:
                return max(next_states)
            else:
                return min(next_states)


        best_action = max(gameState.getLegalActions(0), key = lambda x: minimax(gameState.generateSuccessor(0, x), 1, 1))

        return best_action

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        def min_search(state, agent_index, depth, alpha, beta):
            #print alpha, beta
            if agent_index == state.getNumAgents():
                return max_search(state, 0, depth + 1, alpha, beta)

            best_value = None
            for action in state.getLegalActions(agent_index):
                succ_value = min_search(state.generateSuccessor(agent_index, action), agent_index + 1, depth, alpha, beta)

                if best_value is None:
                    best_value = succ_value
                else:
                    best_value = min(best_value, succ_value)

                if alpha is not None and best_value < alpha:
                    return best_value

                if beta is None:
                    beta = best_value
                else:
                    beta = min(beta, best_value)

            if best_value is not None:
                return best_value
            else:
                return self.evaluationFunction(state)

        def max_search(state, agent_index, depth, alpha, beta):
            if depth > self.depth:
                return self.evaluationFunction(state)

            best_value = None
            for action in state.getLegalActions(agent_index):
                succ_value = min_search(state.generateSuccessor(agent_index, action), agent_index + 1, depth, alpha, beta)

                if best_value is None:
                    best_value = succ_value
                else:
                    best_value = max(best_value, succ_value)

                if beta is not None and best_value > beta:
                    return best_value

                if alpha is None:
                    alpha = best_value
                else:
                    alpha = max(alpha, best_value)

            if best_value is None:
                return self.evaluationFunction(state)
            else:
                return best_value

        best_action = None
        alpha, beta = None, None

        for action in gameState.getLegalActions(0):
            value = min_search(gameState.generateSuccessor(0, action), 1, 1, alpha, beta)
            if alpha is None:
                alpha = value
                best_action = action
            else:
                if value > alpha:
                    alpha, best_action = value, action

        return best_action



class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        def expectimax_search(state, agent_index, depth):
            if agent_index == state.getNumAgents():
                if depth == self.depth:
                    return self.evaluationFunction(state)
                else:
                    return expectimax_search(state, 0, depth + 1)

            actions = state.getLegalActions(agent_index)
            if len(actions) == 0:
                return self.evaluationFunction(state)

            nexts = [expectimax_search(state.generateSuccessor(agent_index, action), agent_index + 1, depth) for action in actions]

            if agent_index == 0:
                return max(nexts)
            else:
                return sum(nexts) / len(nexts)
        best_action = max(gameState.getLegalActions(0), key = lambda x:expectimax_search(gameState.generateSuccessor(0, x), 1, 1))
        return best_action

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    newPos = currentGameState.getPacmanPosition()
    newFood = currentGameState.getFood()
    newGhostStates = currentGameState.getGhostStates()
    newCapsules = currentGameState.getCapsules()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

    closest_ghost = min([manhattanDistance(newPos, ghost.getPosition()) for ghost in newGhostStates])

    # closer ghost lead to smaller score
    if closest_ghost:
        ghost_dist = -5 / closest_ghost
    else:
        ghost_dist = -1000

    newFood = newFood.asList()

    # closer food lead to bigger score
    if len(newFood):
        food_dist = -min([manhattanDistance(newPos, food) for food in newFood])
    else:
        food_dist = 0

    if len(newCapsules):
        capsule_dist = -5 / min([manhattanDistance(newPos, capsule) for capsule in newCapsules])
    else:
        capsule_dist = -1000

    # more food left lead to smaller score
    food_left = -100 * len(newFood)

    score = food_dist + ghost_dist + capsule_dist + food_left

    return score

# Abbreviation
better = betterEvaluationFunction

