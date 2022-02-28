"""
You can create any other helper funtions.
Do not modify the given functions
"""
from collections import deque
import heapdict


def A_star_Traversal(cost, heuristic, start_point, goals):
    """
    Perform A* Traversal and find the optimal path
    Args:
        cost: cost matrix (list of floats/int)
        heuristic: heuristics for A* (list of floats/int)
        start_point: Staring node (int)
        goals: Goal states (list of ints)
    Returns:
        path: path to goal state obtained from A*(list of ints)
    """
    n = len(cost)
    path = []
    closed = []
    parent = {}
    parent[start_point] = start_point
    open_pq = heapdict.heapdict()
    open_pq[start_point] = 0
    s = open_pq.peekitem()
    while open_pq:
        curr = open_pq.popitem()
        closed.append(curr)
        if curr in goals:
            path = []
            while parent[curr] != curr
                path.append(curr)
                curr = parent[curr]
            path.append[start_point]
            path = reverse(path)
            return path
        for neighbour in range(n - 1, 0, -1):
            if cost[curr][neighbour] > 0 and neighbour not in closed and neighbour not in open_pq:
                cost[start_point][neighbour] = cost[start_point][curr] + h[neighbour]
                parent[neighbour] = curr
            else:
                if cost[start_point][neighbour] > (cost[start_point][curr] + h[neighbour]):
                    cost[start_point][neighbour] = cost[start_point][curr] + h[neighbour]
                    parent[neighbour] = curr

                    if neighbour in closed:
                        closed.remove(neighbour)
                        open_pq[neighbour] = cost[start_point][neighbour] + h[neighbour]
        open_pq.popitem()
        closed.append(curr)

    # TODO
    return path


def DFS_Traversal(cost, start_point, goals):
    """
    Perform DFS Traversal and find the optimal path
        cost: cost matrix (list of floats/int)
        start_point: Staring node (int)
        goals: Goal states (list of ints)
    Returns:
        path: path to goal state obtained from DFS(list of ints)
    """
    # pseudo code from Medium BFS and DFS by Tyler Elliot
    path = []
    len_cost = len(cost)
    frontier_stack = deque()
    frontier_stack.append(start_point)
    while(frontier_stack):
        curr_node = frontier_stack.pop()
        path.append(curr_node)
        if curr_node in goals:
            return path
        for neighbour in range(len_cost - 1, 0, -1):
            if cost[curr_node][neighbour] > 0 and neighbour not in path:
                frontier_stack.append(neighbour)

    # TODO
    return path
