from tsp_general import distance
from tsp_test_cases import build_tests
import time
import matplotlib.pyplot as plt

def compare_tsp_algos( fname: str, algos: list, names: list, if_plt: bool) -> None:

    count = 0
    tests = build_tests( fname )
    nodes_numbers = []
    running_times = []

    for test in tests:

        graph, sol = test
        nodes_num = len(graph)
        
        print('------------------ ' + f'Test No.{count+1}' + ' ------------------\n')
        print(f'graph: ')
        for row in graph: 
            print(f'       {row}')
        print(f'\nsolution:')
        print(f'       {sol}\n\n')

        nodes_numbers.append( nodes_num )
        case_running_times = []

        for i in range( len(algos) ):

            startT   = time.process_time()
            sol_algo = algos[i]( graph )
            endT     = time.process_time()
            elapT    = endT - startT

            case_running_times.append( elapT )

            minDist      = distance(sol, graph)
            minDist_algo = distance(sol_algo, graph)
            correctness  = True if minDist == minDist_algo else False

            if  names[i] != 'TSP-Approximation': # TSP algorithms

                print(
                    f'algorithm:    {names[i]}',
                    f'correctness:  {correctness}',
                    f'runningTime:  {elapT:.10f}',
                    f'distance:     {distance(sol_algo, graph)}',
                    sep = '\n',
                    end = '\n\n'                
                )
            
            else: # TSP Approximation
                
                print(
                    f'algorithm:    {names[i]}',
                    f'runningTime:  {elapT:.10f}',
                    f'distance:     {distance(sol_algo, graph)}',
                    f'ratio:        {float(minDist) / float(minDist_algo)}',
                    sep = '\n',
                    end = '\n\n'                
                )
        
        running_times.append( case_running_times )
        count += 1


    if if_plt:

        running_times = list(zip(*running_times))  # Transpose for easier plotting
        plt.figure(figsize=(10, 6))
        for i in range(len(algos)):
            plt.plot(nodes_numbers, running_times[i], label=names[i], marker='o')

        plt.xlabel('Nodes Number')
        plt.ylabel('Running Time (seconds)')
        plt.title('Running Time Comparison of TSP Algorithms')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()        