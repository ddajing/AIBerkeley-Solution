# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    from util import Stack
    from collections import defaultdict
    stack = Stack()
    visited = defaultdict()
    
    if problem.isGoalState(problem.getStartState()):
        return []
    
    stack.push((problem.getStartState(), []))
    visited[problem.getStartState()] = 1

    while not stack.isEmpty():
        coord, path = stack.pop()
        visited[coord] = 1
        if problem.isGoalState(coord):
            return path 
        
        successors = problem.getSuccessors(coord)

        for succ in successors:
            if succ[0] not in visited:
                stack.push((succ[0], path + [succ[1]]))
    
    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue
    from collections import defaultdict

    queue = Queue()
    visited = defaultdict()

    if problem.isGoalState(problem.getStartState()):
        return []

    queue.push((problem.getStartState(), []))
    visited[problem.getStartState()] = 1

    while not queue.isEmpty():
        coord, path = queue.pop()

        if problem.isGoalState(coord):
            return path

        successors = problem.getSuccessors(coord)

        for succ in successors:
            if succ[0] not in visited:
                visited[succ[0]] = 1
                queue.push((succ[0], path + [succ[1]]))

    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    from collections import defaultdict
    pq = PriorityQueue()
    min_cost = defaultdict()
    path = defaultdict(list)
    visited = defaultdict()

    if problem.isGoalState(problem.getStartState()):
        return []

    min_cost[problem.getStartState()] = 0
    path[problem.getStartState()] = []
    pq.push(problem.getStartState(), 0)

    while not pq.isEmpty():
        coord = pq.pop()
        if problem.isGoalState(coord):
            return path[coord]

        if coord in visited:
            continue
        else:
            visited[coord] = True

        successors = problem.getSuccessors(coord)

        for succ in successors:
            if succ[0] not in visited:
                new_path = path[coord] + [succ[1]]
                new_cost = problem.getCostOfActions(new_path)

                if succ[0] not in min_cost or new_cost < min_cost[succ[0]]:
                    min_cost[succ[0]] = new_cost
                    path[succ[0]] = new_path
                    pq.update(succ[0], new_cost)

    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    from collections import defaultdict
    pq = PriorityQueue()
    heuristic_cost = defaultdict()
    path = defaultdict(list)
    visited = defaultdict()

    if problem.isGoalState(problem.getStartState()):
        return []

    heuristic_cost[problem.getStartState()] = heuristic(problem.getStartState(), problem)
    path[problem.getStartState()] = []
    pq.push(problem.getStartState(), heuristic_cost[problem.getStartState()])

    while not pq.isEmpty():
        coord = pq.pop()
        if problem.isGoalState(coord):
            return path[coord]

        if coord in visited:
            continue
        else:
            visited[coord] = True

        successors = problem.getSuccessors(coord)

        for succ in successors:
            if succ[0] not in visited:
                new_path = path[coord] + [succ[1]]
                new_cost = problem.getCostOfActions(new_path) + heuristic(succ[0], problem)

                if succ[0] not in heuristic_cost or new_cost < heuristic_cost[succ[0]]:
                    heuristic_cost[succ[0]] = new_cost
                    path[succ[0]] = new_path
                    pq.update(succ[0], new_cost)

    return []



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
