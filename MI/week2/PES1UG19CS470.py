"""
You can create any other helper funtions.
Do not modify the given functions
"""
import heapq as priority_heap
from collections import deque
def search_in_ptyheap(frontier, find):
    for idx in range(len(frontier)):
        if frontier[idx][1] == find:
            return idx

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
    # TODO
    path = []
    # TODO
    alr_exp = deque()
    path = [start_point]
    frontier=[]
    priority_heap.heapify(frontier)
    priority_heap.heappush(frontier,(heuristic[start_point], path))
    while len(frontier) > 0:
        present_cost, present_path = priority_heap.heappop(frontier)
        n = present_path[-1]
        present_cost -= heuristic[n]
        if n in goals:
            return present_path
        alr_exp.append(n)
        chldrn = [i for i in range(len(cost[0]))
                    if cost[n][i] not in [0, -1]]
        for i in chldrn:
            new_present_path = present_path + [i]
            new_p_cost = present_cost + cost[n][i] + heuristic[i]
            if i not in alr_exp and new_present_path not in [i[1] for i in frontier]:
                priority_heap.heappush(frontier,(new_p_cost, new_present_path))
                priority_heap.heapify(frontier)
            elif new_present_path in [i[1] for i in frontier]:  
                idx = search_in_ptyheap(frontier, new_present_path)
                frontier[idx][0] = min(frontier[idx][0], new_p_cost)
                priority_heap.heapify(frontier)
                
	    	
    return list()
    
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
    # REMEMBER: NOT TO PRINT 7 
    path = []
    # TODO
    frontier_que = deque()
    num = len(cost)
    frontier_que.append(start_point)

    while len(frontier_que)!=0:
        current = frontier_que.pop()
        path.append(current)
        if current in goals:
            return path

        for i in range(num-1,0,-1):
            if cost[current][i]!=-1 and cost[current][i]!=0 and (i not in path):
                frontier_que.append(i)



    return path
