from polarized_communities.algorithms.subroutines.commons import *
from polarized_communities.utilities.time_measure import ExecutionTime
from polarized_communities.utilities.print_console import print_end_algorithm
import numpy as np
import math

def sorted_eigensign(signed_graph):
    # start of the algorithm
    execution_time = ExecutionTime()

    # initialize the solution as empty
    #solution_x = None
    #solution_objective_function = np.finfo(float).min
    solution_threshold = None

    # obtain the adjacency matrix
    a = signed_graph.get_adjacency_matrix()

    # get the eigenvector corresponding to the maximum eigenvalue
    maximum_eigenvector = np.squeeze(eigsh(a, k=1, which='LA')[1])

    # Creazione del vettore di coppie
    index_value_pairs = [(index, abs(value)) for index, value in enumerate(maximum_eigenvector)]

    # Ordina in senso decrescente rispetto al valore assoluto
    sorted_pairs = sorted(index_value_pairs, key=lambda y: y[1], reverse=True)

    # Lunghezza di sorted_pairs
    length = len(sorted_pairs)

    # Creazione di un array di zeri della stessa lunghezza di sorted_pairs
    solution_f = np.zeros(length)

    # Creazione di un vettore che tenga conto se un elemento viene aggiunto o meno
    vett_add = np.full(length, np.nan)
    i=0
    cont0cons=0
    for (indice, valore) in sorted_pairs:
        if cont0cons>20:
            while(i<length):
                vett_add[i]=False
                i+=1
            break
        # Iterazione su sorted_pairs e modifica dell'array di zeri in base alla condizione
        calcolo_prec = evaluate_objective_function(signed_graph, solution_f)
        solution_f[indice] = np.sign(maximum_eigenvector[indice])
        if i==0:
            if evaluate_objective_function(signed_graph, solution_f)> -math.inf:
                vett_add[i] = True
                cont0cons=0
            else:
                vett_add[i] = False
                solution_f[indice]=0
                cont0cons+=1
        else:
            if evaluate_objective_function(signed_graph, solution_f)>calcolo_prec:
                vett_add[i] = True
                cont0cons=0
            else:
                vett_add[i] = False
                solution_f[indice]=0
                cont0cons+=1
        i+=1
        #x = np.array([np.sign(element) if np.abs(element) >= threshold else 0 for element in maximum_eigenvector])

        # update the solution if needed
        #objective_function = evaluate_objective_function(signed_graph, x)
        #if objective_function > solution_objective_function:
        #    solution_x = x
        #    solution_objective_function = objective_function
        #    solution_threshold = threshold

    # build the solution
    solution = build_solution(solution_f)

    # end of the algorithm
    execution_time.end_algorithm()

    # print algorithm's results
    print_end_algorithm(execution_time.execution_time_seconds, solution_f, signed_graph, threshold=solution_threshold)
    print ('vett_add:              '+ str(vett_add))
    print ('vett_add_length:       '+str(len(vett_add)))
    # return the solution
    return solution, solution_f