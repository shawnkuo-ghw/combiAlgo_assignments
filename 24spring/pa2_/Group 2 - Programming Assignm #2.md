# Group 2 - Programming Assignment #2

| Grop Number |                        Group Members                         |
| :---------: | :----------------------------------------------------------: |
|    **2**    | **Hansong Qi, 99901449<br />Ruibo Jing, 999015852<br/>Zhihao Zhao, 999014525<br/>Zhi Mai, 999009350<br/>Hongwei Guo, 999014780** |



## Exercise A 

### 1. Define a graph class

We ues this graph class to generatec graph object.

```python
class graph:
    def __init__(g, numberOfvertice):
        g.numberOfvertice = numberOfvertice
        g.adjmat = [[0] * numberOfvertice for _ in range(numberOfvertice)]

    def add_edge(g, u, v):
        g.adjmat[u][v] = 1
        g.adjmat[v][u] = 1
        
    def add_color(g, vertex, color):
        g.adjmat[vertex][vertex] = color

    def get_color(g, vertex):
        return g.adjmat[vertex][vertex]
```



### 2. The criteria function of clique

According to the definition of clique, we define a fucntion to check whether the current solution is a clique

```python
def IsClique(g, curr):
    for a in range(0, len(curr)):
        for b in range(a+1, len(curr)):
            if(curr[a] == curr[b]):
                return 0
    for i in curr:
        for j in curr:
            if(i != j  and (g.adjmat[i][j] == 0 or g.adjmat[i][i] == g.adjmat[j][j])):
                return 0
    return 1
```



### 3.  The $Choice$ function adapting to MCP

```python
def ComputeAl(g, l, solution) -> set:
    Al = set()
    isnew = False
    for i in range(0, g.numberOfvertice):
        if(g.adjmat[l][i] != 0 and i != l):
            isnew = False
            for element in solution:
                if (g.get_color(element) == g.get_color(i)):
                    isnew = False
                    break
                isnew = True
            if(isnew):    
                Al.add(i)
    return Al

def ComputeBl(g, solution) -> set:
    copy = []
    copy = solution.copy()
    Bl = set()
    for i in range(0, g.numberOfvertice):
        Bl.add(i)
    for element in copy:
        Bl.remove(element)
    return Bl

def ComputeCl(g, l, solution, choice_set) -> set:
    Cl = ComputeAl(g,l, solution) & ComputeBl(g, solution) & choice_set
    #print('C', l, ' = ', Cl, sep='')
    return Cl
```



### 4. The $Bounding$​ Function adapting to MCP

```python
def GreedyColour(g, solution):
    #Colour = []
    k = 0
    ColourClass = []
    for i in range(g.numberOfvertice):
        if (g.adjmat[i][i] != 0):
            ColourClass.append(0)
            ColourClass[-1] = set()
    for i in range(g.numberOfvertice):
        if (g.adjmat[i][i] == 0):
            continue
        h = 0
        while(h < k and  not (ComputeAl(g, i, solution) & ColourClass[h])):
            h = h + 1
        if(h == k):
            k = k + 1
            ColourClass[h].clear()
        ColourClass[h].add(i)
    return k
```



```python
def GreedyBound(g, Cl, solution):
    k = GreedyColour(RestrictionGraph(g, Cl), solution)
    return len(solution) + k
```



```python
def RestrictionGraph(g, Cl):
    h = graph(g.numberOfvertice)
    for element in Cl:
        h.add_color(element, g.get_color(element))
        for dest in Cl:
            if (g.adjmat[element][dest] != 0 and element != dest):
                h.add_edge(element, dest)
    return h
```



### 5. The Structure of  $Branch-and-Bound$  Algorithm

``` python
def BranchAndBound_final(g):
    global global_OptP
    global global_OptX

    MaxSize = 0
    count = 0
    AllClique = []
    Cl = set()
    for i in range(g.numberOfvertice):
        Cl.add(i)
    for i in range(0, g.numberOfvertice):
        solution = []
        solution.append(0)
        solution[0] = i
        choice_set = Cl.copy()
        BranchAndBound(g,1,solution, choice_set)
        
        AllClique.append(global_OptX)

        if(global_OptP > MaxSize):
            MaxSize = global_OptP

        global_OptP = 0
        global_OptX = []
        count = count + 1

    print("Overall Maxsize = ", MaxSize)
    print("AllClique = ", AllClique)
```


```python
def BranchAndBound(g, l, solution, choice_set):
    global global_OptP
    global global_OptX
    if(IsClique(g, solution)):
        P = len(solution)
        if(P > global_OptP):
            global_OptP = P
            global_OptX = solution.copy()
    Cl = ComputeCl(g, solution[-1], solution, choice_set)
    
    nextchoice = []
    nextbound = []
        
    count = 0
    for x in Cl:
        nextchoice.append(0)
        nextchoice[count] = x
        nextbound.append(0)
        nextbound[count] = GreedyBound(g, Cl, solution)
        count = count + 1
    
    nextbound,nextchoice = Sortnext(nextbound,nextchoice)

    for i in range(0, count):
        if(nextbound[i] <= global_OptP):
            return
        BranchAndBound(g, l+1, solution + [nextchoice[i]], Cl)
```



```python
def Sortnext(nextbound, nextchoice):
    for i in range(0, len(nextbound) - 1):
        for j in range(0, len(nextbound) - 1 - i):
            if (nextbound[j] < nextbound[j + 1]):
                nextbound[j], nextbound[j + 1] = nextbound[j + 1], nextbound[j]
                nextchoice[j], nextchoice[j + 1] = nextchoice[j + 1], nextchoice[j]
    return nextbound, nextchoice
```



### 6. Random k-colored Graph Generator

```python
def Random_Graph_Generator(g, density):
    h = graph(g.numberOfvertice)
    for i in range(g.numberOfvertice - 2):
        for j in range(i + 1, g.numberOfvertice - 1):
            r = random.uniform(0, 1)
            if (r >= 1 - density):
                h.add_edge(i - 1, j - 1)
    for i in range(g.numberOfvertice):
        r = random.randint(1, g.numberOfvertice / 2)
        h.adjmat[i][i] = r
    return h
```



### 7. Main Body

```python
global_OptP = 0
global_OptX = []
g2 = graph(50)
g2 = Random_Graph_Generator(g2, 0.5)
BranchAndBound_final(g2)
```



## Exercise B

### 1. Keep the definition of graph class as Ex. A

```python
class graph:
    def __init__(g, numberOfvertice):
        g.numberOfvertice = numberOfvertice
        g.adjmat = []
```

### 2. Define $neighbour$ Function

```python
def neighbor(g: graph, solution: list):
    copy_solution = []
    copy_solution = copy.copy(solution)
    origin = copy_solution[-1]
    isnew = False
    for i in range(0, g.numberOfvertice):
        if (i != origin and g.adjmat[origin][i] != 0):
            for element in copy_solution:
                if (element == i):
                    isnew = False
                    break
                if (g.adjmat[element][i] == 0):
                    isnew = False
                    break
                if (g.adjmat[element][element] == g.adjmat[i][i]):
                    isnew = False
                    break
                isnew = True
        
        if (isnew):
            solution.append(i)
            break 
    return solution
```

### 3.  Define $Hill\ Climbing\ Search$ Funtion

```python
def hill_climbing_search(g, vertex):
    solution = []
    solution.append(vertex)
    searching = True

    while (searching):
        current = len(solution)
        solution = neighbor(g, solution)
        if (len(solution) == current):
            searching = False

    return solution
```

### 4. Implement $Hill\ Climbing$ Algorithm

```python
def hill_climbing_search(g, vertex):
    solution = []
    solution.append(vertex)
    searching = True

    while (searching):
        current = len(solution)
        solution = neighbor(g, solution)
        if (len(solution) == current):
            searching = False

    return solution

def MCP_HC(g):
    solution = []
    vertice = []

    for i in range(0, g.numberOfvertice):
        vertice.append(i)
    
    random.shuffle(vertice)
    vertex = vertice[0]
    solution = hill_climbing_search(g, vertex)
    min = len(solution)
    max = len(solution)
    avg = 0
    optimal = 3
    Nopt = 0
    for element in vertice:
        solution = hill_climbing_search(g, element)
        if (len(solution) < min):
            min = len(solution)
        if (len(solution) > max):
            max = len(solution)
        if (len(solution) != optimal):
            Nopt += 1
        avg = avg + len(solution)
        print(solution)

    avg = avg / len(vertice)

    print('min = ' + str(min) + ', max = ' + str(max) + ', avg = ' + str(avg) + ', Nopt = ' + str(Nopt) + ' when = ' + str(len(vertice)))
    
    return
```



## Exercise C
### 1. First step: define a graph

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

### for example

```python
colors = [0, 1,2,3,4,5]  # Example colors for vertices
g1 = Graph(6, colors)
edges = [(0, 1), (0, 3), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5)]
for u, v in edges:
    g1.add_edge(u, v)
```

This defines a graph with different-color vertices and the edges are E={(0, 1), (0, 3), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5)}

### 2. second step: define a neighbor function 

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

### 3. Third Step: define simulated_annealing_search

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

### 4. forth step: Implement MCP function

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
