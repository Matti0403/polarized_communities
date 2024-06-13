import numpy as np

from polarized_communities.algorithms.subroutines.commons import evaluate_objective_function


def print_input(dataset, algorithm):
    print('------------- Input -------------')
    print('dataset:               ' + dataset)
    print('algorithm:             ' + algorithm)

def print_end_algorithm(runtime, x, signed_graph, beta=np.nan, threshold=np.nan):
    print('------------- Output ------------')

    # parameters
    print('tau:                   ' + str(threshold))
    print('multiplicative factor: ' + str(beta))

    # performance information
    print('runtime:               ' + str(runtime))

    # quality of the solution
    print('polarity:              ' + str(evaluate_objective_function(signed_graph, x)))

    # print the nodes of the two communities
    community_p1 = {node for node, element in enumerate(x) if element == 1}
    countS1=0
    for nodeS1 in community_p1:
        countS1+=1
    community_m1 = {node for node, element in enumerate(x) if element == -1}
    countS2=0
    for nodes2 in community_m1:
        countS2+=1
    print('S_1:                   ' + str(str(community_p1).replace('set([', '').replace('])', '')))

    print('S_2:                   ' + str(str(community_m1).replace('set([', '').replace('])', '')))

    print('S_1 length: ' + str(countS1))
    print('S_2 length: ' + str(countS2))

    with open('output.txt', 'a') as f:
        f.write(f' , {str(evaluate_objective_function(signed_graph, x))} , {runtime} , S1:{str(countS1)} , S2:{str(countS2)}\n')