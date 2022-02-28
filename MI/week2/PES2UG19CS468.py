#Yousha Mahamuni
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
    path = []
    # TODO
    
    start=[start_point]
    n=[[0+heuristic[start_point],start]]
    while len(n)>0:
        path_cost,ppath=n.pop(0)
        p=ppath[-1]
        path_cost=path_cost-heuristic[p]
        if p in goals:
            return ppath
        path.append(p)
        c=[l for l in range(len(cost[0])) if cost[p][l] not in [0,-1]]
        for l in c:
            new_path=ppath+[l]
            new_cp=path_cost+cost[p][l] + heuristic[l]
            if l not in path and new_path not in [l[1] for l in n]:
                n.append((new_cp,new_path))
                n=sorted(n,key=lambda y:(y[0],y[1]))
            elif new_path in [l[1] for l in n]:
                i=equ(n,new_path)
                n[i][0]=min(n[i][0],new_cp)
                n=sorted(n,key=lambda y:(y[0],y[1]))
                
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
    path = []
    # TODO
    arr1=[]
    
    arr1.append(start_point)
    while len(arr1)!=0:
        f=arr1.pop()
        path.append(f)
        for k in range(len(cost)-1,0,-1):
            if(cost[f][k]!=0 and cost[f][k]!=-1):
                if(k not in path):
                    arr1.append(k)
        if f in goals:
            break
    
    return path


def equ(arr1,path):
    for i in range(len(arr1)):
        if(arr1[i][1]==path):
            return i
            
