import random
from math import inf, isinf
from tsp_bounding import tsp_bounding

def tsp_generate_test_cases(fname: str, tests_num: int, init: int, step: int, maxDist: int, conRate: float) -> None:
    '''
    Generate valid test cases for TSP problem that must guarentee the triangular inequality.

    Arguments:
        - fname:     the name of file that stores all the test cases
        - tests_num: the number of test cases to generate
        - init:      the initial value of nodes number
        - step:      the step nodes number is increased each loop
        - maxDist:   the maximun distance between nodes
        - conRate:   the posibility rate of connection between two nodes, range from 0 to 1
    '''

    assert 0 < conRate and conRate < 1 and f"Error: conRate = {conRate} is invalid, conRate is in (0, 1)."

    file = open(fname, 'w')

    count = 1
    nodes_num = init

    while count <= tests_num:

        '''
        Step 1: Generate an empty graph
        '''
     
        graph = valid_graph(nodes_num, maxDist, conRate)

        '''
        Step 4: Generate a TSP solution to the graph
        '''

        sol = tsp_bounding(graph)

        if len(sol) != nodes_num:

            continue

        # for row in graph: print(row)
        # print(f'sol: {sol}')
        sol_ = ' '.join(map(str, sol))

        '''
        Step 5: Print graph and sol into file {fname}
        '''
        
        test_case = ''
        
        for i in range(nodes_num):
            
            row = ' '.join(map(str, graph[i]))
            test_case += row + '#'

        test_case += sol_
        
        # print(test_case)
        
        if count != tests_num:
            test_case += '\n'

        file.write(test_case)

        count += 1
        nodes_num += step

    file.close()


def valid_graph(nodes_num: int, maxDist: int, conRate: float) -> list[list]:
    '''
    Generate a valid graph that satisfies triangle inequality.
    Arguments:
        - nodes_num: number of nodes
        - maxDist:   maximum value of edge distance
        - conRate:   possibility rate of the connection between two nodes
    '''
    
    graph = []

    for r in range(nodes_num):
        row = [0] * nodes_num
        row[r] = inf
        graph.append( row )
    
    def set_edges(currNode, vistedNodes) -> None:

        nonlocal graph

        if currNode == nodes_num - 1:

            return

        nodesLeft = [ node for node in range(currNode+1, nodes_num) ]

        for newNode in nodesLeft:

            randInt = random.randint(1, 100)
            connInt = int(conRate * 100)

            newEdge = inf # new edge between currNode and newNode

            # 1. Decide whether newNode and currNode is connnected
            if randInt <= connInt:
                
                # 2. Set the distance of newEdge according to triangle inequelity
                if len(vistedNodes) != 0:
 
                    # Found the bound of newEdge
                    
                    maxBound = maxDist
                    minBound = 1

                    for vNode in vistedNodes:

                        edge1 = graph[vNode][newNode]
                        edge2 = graph[vNode][currNode]
                        
                        if not isinf(edge1) and not isinf(edge2):
                        
                            newMaxBound = edge1 + edge2
                            newMinBound = abs(edge1 - edge2)
                        
                            if newMaxBound < maxBound: maxBound = newMaxBound
                            if newMinBound > minBound: minBound = newMinBound

                    # set new edge between currNode and newNode

                    if minBound < maxBound:

                        newEdge = random.randint(minBound, min(maxDist, maxBound))

                    elif minBound == maxBound:

                        newEdge = min(maxDist, maxBound)

                    # if minBound > maxBound, then currNode and newNode cannot be connected.

                else:

                    newEdge = random.randint(1, maxDist)

            graph[currNode][newNode] = newEdge
            graph[newNode][currNode] = newEdge

        set_edges( currNode + 1, vistedNodes + [currNode] )
    
    set_edges(0, [])

    return graph


def build_tests(fname: list) -> list:
    '''
    Return a list consisting of all test cases in file {fname}.
    '''

    file  = open(fname, "r")
    lines = file.read().split("\n")
    file.close()

    tests = []

    for line in lines:

        test = line.split("#")

        nodes_num = len(test) - 1
        
        graph = []
        sol = list(map(int, test[nodes_num].split()))
        
        
        for i in range(nodes_num):
            
            row = []
            currRow = list(test[i].split(' '))

            for i in range(nodes_num):

                currEdge = currRow[i]

                if currEdge == 'inf': row.append(inf)
                else: row.append( int(currEdge) )

            graph.append( row )

        tests += [(graph,sol)]
    
    return tests