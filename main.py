import pandas as pd
import numpy as np


def print_hi(data, num_of_states):
    #  ZZ,Z,NZ,OD
    #ZZ
    #Z
    #NZ
    #OD
    transition_matrix_1 = np.zeros([num_of_states, num_of_states])
    transitions_count = np.zeros(num_of_states)
    num_of_users = data.shape[1]
    for id in range(1, num_of_users + 1):
        transitions = data[f'uID_{id}'].to_numpy()
        for i in range(1, len(transitions) - 1):
            if transitions[i] == 'ZZ':
                if transitions[i+1] == 'ZZ':
                    transition_matrix_1[0, 0] = transition_matrix_1[0, 0] + 1
                elif transitions[i+1] == 'Z':
                    transition_matrix_1[0, 1] = transition_matrix_1[0, 1] + 1
                elif transitions[i+1] == 'NZ':
                    transition_matrix_1[0, 2] = transition_matrix_1[0, 2] + 1
                elif transitions[i+1] == 'OD':
                    transition_matrix_1[0, 3] = transition_matrix_1[0, 3] + 1
                transitions_count[0] += 1
            elif transitions[i] == 'Z':
                if transitions[i+1] == 'ZZ':
                    transition_matrix_1[1, 0] = transition_matrix_1[1, 0] + 1
                elif transitions[i+1] == 'Z':
                    transition_matrix_1[1, 1] = transition_matrix_1[1, 1] + 1
                elif transitions[i+1] == 'NZ':
                    transition_matrix_1[1, 2] = transition_matrix_1[1, 2] + 1
                elif transitions[i+1] == 'OD':
                    transition_matrix_1[1, 3] = transition_matrix_1[1, 3] + 1
                transitions_count[1] += 1
            elif transitions[i] == 'NZ':
                if transitions[i+1] == 'ZZ':
                    transition_matrix_1[2, 0] = transition_matrix_1[2, 0] + 1
                elif transitions[i+1] == 'Z':
                    transition_matrix_1[2, 1] = transition_matrix_1[2, 1] + 1
                elif transitions[i+1] == 'NZ':
                    transition_matrix_1[2, 2] = transition_matrix_1[2, 2] + 1
                elif transitions[i+1] == 'OD':
                    transition_matrix_1[2, 3] = transition_matrix_1[2, 3] + 1
                transitions_count[2] += 1
            elif transitions[i] == 'OD':
                if transitions[i+1] == 'ZZ':
                    transition_matrix_1[3, 0] = transition_matrix_1[3, 0] + 1
                elif transitions[i+1] == 'Z':
                    transition_matrix_1[3, 1] = transition_matrix_1[3, 1] + 1
                elif transitions[i+1] == 'NZ':
                    transition_matrix_1[3, 2] = transition_matrix_1[3, 2] + 1
                elif transitions[i+1] == 'OD':
                    transition_matrix_1[3, 3] = transition_matrix_1[3, 3] + 1
                transitions_count[3] += 1
    for i in range(num_of_states):
        transition_matrix_1[i] /= transitions_count[i]
    return transition_matrix_1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = pd.read_csv('userSatisfactionStates.csv', index_col=0)
    trnsition_matrix = print_hi(data, 4)
    x=1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
