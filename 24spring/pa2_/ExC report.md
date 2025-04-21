This exercise is done by Hansong Qi and Zhihao Zhao

## First step: define a graph

```python
class Graph:
    def __init__(self, number_of_vertices, colors):
        self.number_of_vertices = number_of_vertices
        self.adjmat = [[0] * number_of_vertices for _ in range(number_of_vertices)]
        self.vertex_colors =colors

    def add_edge(self, u, v):
        self.adjmat[u][v] = 1
        self.adjmat[v][u] = 1
```

The graph has 3 attributes "number of vertices, adjacent matrix and vertices' colors" and there is an "add edge" function to determine which edges are connected.

## for example

```python
colors = [0, 1,2,3,4,5]  # Example colors for vertices
g1 = Graph(6, colors)
edges = [(0, 1), (0, 3), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5)]
for u, v in edges:
    g1.add_edge(u, v)
```

This defines a graph with different-color vertices and the edges are E={(0, 1), (0, 3), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5)}

## second step: define a neighbor function 

```python
def neighbor(g, solution):
    copy_solution = solution.copy()
    origin = copy_solution[-1]
    candidates = []
    #Find candidates(possible solution)
    for i in range(g.number_of_vertices):
        if i != origin and g.adjmat[origin][i] == 1 and i not in copy_solution:
            is_clique = True
            #check whether it is connected with other vertices in the current solution
            for vertex in copy_solution:
                if g.adjmat[vertex][i] == 0:
                    is_clique = False
                    break
            if is_clique:
                candidates.append(i)
    
    if candidates:
        #Check the color
        new_vertex = random.choice(candidates)
        if g.vertex_colors[new_vertex] not in [g.vertex_colors[v] for v in copy_solution]:
            copy_solution.append(new_vertex)
    
    return copy_solution
```

by this function we can find a good neighbor to be added to the solution. And then we have a cost function which is used to judge whether the solution is good.

```python
def cost(solution):
    return -len(solution)  # when the clique gets bigger the cost is smaller 
```

 when the clique gets bigger the cost is smaller which means we get a better solution if the cost gets smaller.

## Third Step: define simulated_annealing_search

We use the "neighbor" function and the "cost" function to implement the simulated annealing search.

First, we initialize parameters

```python
def simulated_annealing_search(graph, start_vertex, initial_temp=1000, cooling_rate=0.99, min_temp=1e-3, max_iter=1000):
    current_solution = [start_vertex]
    best_solution = current_solution.copy()
    current_temp = initial_temp         #T
```

Then, we implement the simulated annealing algrithm

```python
    for _ in range(max_iter):
        if current_temp < min_temp:
            break
		#new_solution is the parameter "Y" of the pseudo-code shown in the class
        #and current_solution is X
        new_solution = neighbor(graph, current_solution)
        
        delta_cost = cost(new_solution) - cost(current_solution)
        #judge which one is better
        
        if delta_cost < 0 or random.uniform(0, 1) < math.exp(-delta_cost / current_temp):
            current_solution = new_solution                 #good solution
            #update the current solution and best solution
            if len(new_solution) > len(best_solution):
                best_solution = new_solution.copy()
        
        current_temp *= cooling_rate #T=aT

    return best_solution
```

every time we use neighbor function to find a new solution we compare it with current solution. if it is better(the cost is smaller),update solutions. If it's not a better solution but satisfies the probability also updates. And the T=a*T after each loop until it reach the boundary(min_temp) .

## forth step: Implement MCP function

we implement the MCP_SA function by using simulated_annealing_search function

```python
def MCP_SA(graph):
    #initialize
    vertices = list(range(graph.number_of_vertices))
    
    random.shuffle(vertices)
    
    min_clique_size = float('-inf')
    max_clique_size = float('inf')
    total_clique_size = 0
    optimal_clique_size = 3  # Example optimal size
    non_optimal_count = 0
    #start from each point to find a best solution
    for vertex in vertices:
        solution = simulated_annealing_search(graph, vertex)
        clique_size = len(solution)
        #update solution
        if clique_size < min_clique_size:
            min_clique_size = clique_size
        if clique_size > max_clique_size:
            max_clique_size = clique_size
        if clique_size != optimal_clique_size:
            non_optimal_count += 1
        
        total_clique_size += clique_size
        print(solution)
    
    avg_clique_size = total_clique_size / len(vertices)
    
    print(f'min = {min_clique_size}, max = {max_clique_size}, avg = {avg_clique_size}, Nopt = {non_optimal_count} when = {len(vertices)}')
```

explanations are commented.

## Finally: apply the examples in ExA 