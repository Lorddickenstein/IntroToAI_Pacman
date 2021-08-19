"""
Depth-first search (DFS)
    - is an algorithm for tree traversal on graph or tree data structures.
    - it can be implemented using recursion and data structures like dictionaries and sets

Algorithm
    1. Pick any node. If it is unvisited, mark it as visited an and recur on all its adjacent nodes
    2. Repeat until all nodes are visited, or the node to be searched is found.
"""

import util

# Using a Python dictionary to act as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

stack = util.Stack()
visited = set()  # keep track of visited nodes
solution = []
exist = True


def dfs(visited, graph, node):
    if node not in visited:
        print node
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


def test():
    stack.push('green')
    stack.push('white')
    stack.push('orange')

    while not stack.isEmpty():
        print stack.pop()


def dfs_using_stack_with_goal_recursion(visited, graph, node, goal, met):
    if node not in visited:
        visited.add(node)
        if node != goal and not met:
            stack.push(node)
            if len(graph[node]) != 0:  # check if node has children
                for neighbour in graph[node]:
                    dfs_using_stack_with_goal_recursion(visited, graph, neighbour, goal, met)
            else:
                stack.pop()
            # if len(graph) == len(visited):
            #     exist = False
        else:
            met = True


def dfs_using_stack_1(visited, graph, node):
    stack.push(node)
    while not stack.isEmpty():
        node = stack.pop()
        if node not in visited:
            print node
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    stack.push(neighbour)


def dfs_using_stack_2(visited, graph, node):
    if node not in visited:
        print node
        stack.push(node)
        visited.add(node)
        if len(graph[node]) == 0:
            stack.pop()
        else:
            for neighbour in graph[node]:
                dfs_using_stack_2(visited, graph, neighbour)


def dfs_using_stack_3(visited, graph, node):
    stack.push(node)
    if node not in visited:
        print node
        visited.add(node)
        if len(graph[node]) == 0:
            stack.pop()
        else:
            for neighbour in graph[node]:
                dfs_using_stack_3(visited, graph, neighbour)
    while not stack.isEmpty():
        stack.pop()


def dfs_iteration():
    pass


def dfs_pre_order_recursion(visited, graph, node):
    print node
    visited.add(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs_pre_order_recursion(visited, graph, neighbour)


def dfs_post_order_recursion(visited, graph, node):
    visited.add(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs_post_order_recursion(visited, graph, neighbour)
    print node


# dfs(visited, graph, 'A')
print "dfs type 1"
dfs_using_stack_1(visited, graph, 'A')
visited = set()
print "dfs type 2"
dfs_using_stack_2(visited, graph, 'A')
visited = set()
print "dfs type 3"
dfs_using_stack_3(visited, graph, 'A')
visited = set()
print "dfs pre-order recursive"
dfs_pre_order_recursion(visited, graph, 'A')
visited = set()
print "dfs post-order recursive"
dfs_post_order_recursion(visited, graph, 'A')
if stack.isEmpty():
    print "Stack empty"
else:
    print "Stack not empty"
visited = set()
print "dfs using stack with goal recursion"
dfs_using_stack_with_goal_recursion(visited, graph, 'A', 'E', False)
while not stack.isEmpty():
    solution.append(stack.pop())
print(solution.reverse())
