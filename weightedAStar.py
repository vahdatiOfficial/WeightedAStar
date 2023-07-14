from heapq import heappush , heappop

class Problem:
    def __init__(self,initialState,goalState) -> None:
        self.initialState = initialState.split(" ")
        self.goalState = goalState.split(" ")
class Node:
    def __init__(self,father,action,root,gn) -> None:
        self.father = father
        self.action = action
        self.gn = gn
        self.root = list(root)
        self.evaluationFun = evaluationFunction(self.gn,self.root)
        
#----------------------------------------------------------------------------------------
    def __eq__(self, object):
        if isinstance(object , self.__class__):
            return self.father == object.father and self.action == object.action and self.evaluationFun == object.evaluationFun and self.root == object.root
        else:
            return NotImplemented
#----------------------------------------------------------------------------------------    
    def __hash__(self):
        return hash((self.father ,self.action ,self.evaluationFun ,self.root))   
#----------------------------------------------------------------------------------------  
    """
    def __str__(self):
        node = "\nNode :"
        for i in range(0,n**2):
            if(i % n == 0):
                node += "\n" + self.root[i] + "\t"
            else:
                node += self.root[i] + "\t"
        return node
    """
    def __lt__(self,object):
        if isinstance(object ,self.__class__):
            return self.evaluationFun < object.evaluationFun
        return NotImplemented
#----------------------------------------------------------------------------------------
def evaluationFunction(gn,node):
    return gn + heuristicFun(node)
#---------------------------------------------------------------------------------------
"""
def heuristicFun(node):
    conter = 0
    for i in node:
        if(i == '0'):
            if(node.index(i) != len(node)-1):
                conter += 1
        else:
            if(str(node.index(i)+1) != i):
                conter += 1
    return conter

"""
def heuristicFun(node):
    if(node == problem.goalState):
        return 0
    else:
        conter = 0
        myit = iter(problem.goalState)
        for i in node:
            if (i != next(myit)):
                conter += 1
        return conter * 10
#---------------------------------------------------------------------------------------
def empty(frontier):
    if(len(frontier) == 0):
        return True
    else:
        return False

def problemActions(node):
    index = node.root.index('0')
    lis = []
    if((index - n) > -1):
        lis.append("U")
    if((index + 1) % n != 0):
        lis.append("R")
    if((index + n) < (n**2)):
        lis.append("D")
    if(index % n != 0):
        lis.append("L")
    return lis

def newChildNode(node,action):
    index = node.root.index('0')
    temp = node.root
    if(action == "U"):
        temp[index] , temp[index - n] = temp[index - n] , temp[index]
        node1 = Node(node,action,temp,node.gn + 1)
        temp[index - n] , temp[index] = temp[index] , temp[index - n]
        return node1
    if(action == "D"):
        temp[index] , temp[index + n] = temp[index + n] , temp[index]
        node1 = Node(node,action,temp,node.gn + 1)
        temp[index + n] , temp[index] = temp[index] , temp[index + n]
        return node1
    if(action == "R"):
        temp[index] , temp[index + 1] = temp[index + 1] , temp[index]
        node1 = Node(node,action,temp,node.gn + 1)
        temp[index + 1] , temp[index] = temp[index] , temp[index + 1]
        return node1
    if(action == "L"):
        temp[index] , temp[index - 1] = temp[index - 1] , temp[index]
        node1 = Node(node,action,temp,node.gn + 1)
        temp[index - 1] , temp[index] = temp[index] , temp[index - 1]
        return node1
def solution(node):
    def slu(nodes):
        lia = ""
        if(nodes.father is not None):
            n = nodes.father
            lia = slu(n)
        if(nodes.action != None):
            lia += nodes.action + " "
        return lia
    soloList = slu(node)
    soloList = soloList[:-1]
    return soloList
    
def aStarSearch(problem):
    frontier = []
    reached = {}
    i = 0
    if(problem.initialState == problem.goalState):
        return 0
    nodeState = Node(None,None,problem.initialState,0)
    heappush(frontier,nodeState)
    reached.update({"".join(problem.initialState) : nodeState})
    while not empty(frontier):
        node = heappop(frontier)
        if(node.root == problem.goalState):
            return solution(node) , i
        i += 1
        for action in problemActions(node):
            child = newChildNode(node,action)
            s = "".join(child.root)
            if(s not in reached or child.evaluationFun < reached[s].evaluationFun):
                reached[s] = child
                heappush(frontier,child)
        
    return "no solution found" , i
global n
global problem
n = int(input())
initialState = input()
goalState = input()
problem = Problem(initialState,goalState)
solution = aStarSearch(problem)
if(solution != 0):
    print(solution[1])
    print(solution[0])
else:
    print(0)