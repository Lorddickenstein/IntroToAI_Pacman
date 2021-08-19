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
    return [s, s, w, s, w, w, s, w]

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

    """
        References:
            Reducible, youtube link: https://www.youtube.com/watch?v=PMMc4VsIacU&t=897s&ab_channel=Reducible
            Go Gate It, https://www.youtube.com/watch?v=iaBEKo5sM7w&ab_channel=GoGATEIIT
    """
    # get the current state of pacman
    node = {
        'state': problem.getStartState(),
        'path-cost': 0
    }
    # initialization
    stack = util.Stack()
    explored = []
    solution = []

    # push start state
    stack.push(node)
    # loop until solution is found or if stack is empty
    while not stack.isEmpty():
        node = stack.pop()
        if node['state'] not in explored:
            if problem.isGoalState(node['state']):
                path_node = node
                # trace the path from goal to the root using the parent
                while 'parent' in path_node:
                    # add actions to the solution
                    solution.append(path_node['action'])
                    path_node = path_node['parent']
                solution.reverse()
                return solution
            # add nodes to explored to mark as visited
            explored.append(node['state'])
            # if goal state is not found then get all the successors
            for successor in problem.getSuccessors(node['state']):
                # create the child
                child = {
                    'state': successor[0],
                    'action': successor[1],
                    'path-cost': successor[2],
                    'parent': node
                }
                #  Add to stack if not visited
                if child['state'] not in explored:
                    stack.push(child)
    raise Exception('No Solution')


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    """
        References: 
        Artificial Intelligence: A Modern Approach 3rd Edition
        James Foster, youtube link: https://www.youtube.com/watch?v=MMCUepjSoLQ&ab_channel=JamesFoster
        William Fiset, youtube link: https://www.youtube.com/watch?v=oDqjPvD54Ss&t=1s&ab_channel=WilliamFiset
    """
    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", problem.getSuccessors(problem.getStartState())
    # get the current state of pacman
    node = {
        'state': problem.getStartState(),
        'path-cost': 0
    }
    # initialization
    solution = []
    frontier = util.Queue()
    explored = []  # keep track of explored nodes

    # add current state to queue
    frontier.push(node)

    # loop until solution is found or if queue is empty
    while not frontier.isEmpty():
        node = frontier.pop()
        if node['state'] not in explored:
            if problem.isGoalState(node['state']):
                path_node = node
                # trace the path from goal to the root using the parent
                while 'parent' in path_node:
                    # append the action to the solution
                    solution.append(path_node['action'])
                    path_node = path_node['parent']
                solution.reverse()
                return solution

            # add nodes to explored to mark as visited
            explored.append(node['state'])

            # if goal state is not found then get all the successors
            for successor in problem.getSuccessors(node['state']):
                # create the child
                child = {
                    'state': successor[0],
                    'action': successor[1],
                    'path-cost': successor[2],
                    'parent': node
                }
                # add them to queue if not visited
                if child['state'] not in explored:
                    frontier.push(child)
    # if program reaches here then no solution is found
    raise Exception('No solution')
    # util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    """
        References:
            Artificial Intelligence: A Modern Approach 3rd Edition
            John Levine, youtube link: https://www.youtube.com/watch?v=dRMvK76xQJI&ab_channel=JohnLevine
            Cacti council, youtube link: https://www.youtube.com/watch?v=qXdt1AHMB2o&ab_channel=CactiCouncil 
    """
    # get the current state of pacman
    node = {
        'state': problem.getStartState(),
        'path-cost': 0
    }
    # initialization
    frontier = util.PriorityQueue()
    explored = []
    solution = []

    # push start state
    frontier.push(node, node['path-cost'])

    # loop until solution is found or if queue is empty
    while not frontier.isEmpty():
        node = frontier.pop()
        if node['state'] not in explored:
            if problem.isGoalState(node['state']):
                path_node = node
                # trace the path from goal to the root using the parent
                while 'parent' in path_node:
                    solution.append(path_node['action'])
                    path_node = path_node['parent']
                solution.reverse()
                return solution

            explored.append(node['state'])
            # if goal state is not found then get all the successors
            for successor in problem.getSuccessors(node['state']):
                # create the child
                child = {
                    'state': successor[0],
                    'action': successor[1],
                    'path-cost': successor[2] + node['path-cost'],  # represents priority
                    'parent': node
                }
                # add them to queue if not visited
                if child['state'] not in explored:
                    frontier.update(child, child['path-cost'])
                    """
                        There are three ways the child node can be and three ways to deal with the child node:
                            1. child node already in queue but with cost higher than its older cost
                                - child node updates the cost of that node in the heaps tree so that it will be moved to
                                    a different much lower priority
                            2. child node already in queue but with cost lower or equal its older cost
                                - it does nothing
                            3. child node not in queue
                                - in this case update function just adds them in the queue
                    """
    # if program reaches here then no solution is found
    raise Exception('No solution')
    # util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    """
        References:
    """
    # get the current state of pacman
    node = {
        'state': problem.getStartState(),
        'path-cost': 0
    }
    # initialization
    frontier = util.PriorityQueue()
    explored = []
    solution = []

    # push start state
    frontier.push(node, node['path-cost'])

    while not frontier.isEmpty():
        node = frontier.pop()
        if node['state'] not in explored:
            if problem.isGoalState(node['state']):
                # trace the path from goal to the root using the parent
                path_node = node
                while 'parent' in path_node:
                    solution.append(path_node['action'])
                    path_node = path_node['parent']
                solution.reverse()
                return solution

            explored.append(node['state'])
            # get all the successors
            for successor in problem.getSuccessors(node['state']):
                # get the heuristic of each state
                heuristic_cost = heuristic(successor[0], problem)
                # create the child
                child = {
                    'state': successor[0],
                    'action': successor[1],
                    'path-cost': successor[2] + node['path-cost'],  # represent priority
                    'parent': node
                }
                # update or add unexplored child nodes with new heuristic cost
                if child['state'] not in explored:
                    frontier.update(child, child['path-cost'] + heuristic_cost)
    # if program reaches here then no solution is found
    raise Exception('No solution')
    # util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
