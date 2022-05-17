import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def get_transition_matrix_all_users(data, num_of_states):
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
    num_of_values = transition_matrix_1.sum()
    for i in range(num_of_states):
        transition_matrix_1[i] /= transitions_count[i]
    return transition_matrix_1, transitions_count/num_of_values


def simulation(start_state, transit_matrix, steps):
    state = start_state
    T = transit_matrix
    data = []
    for i in range(1, steps + 1):
        state_1 = None
        state = next_state(T[state])
        if state == 0:
            state_1 = 'ZZ'
        elif state == 1:
            state_1 = 'Z'
        elif state == 2:
            state_1 = 'NZ'
        elif state == 3:
            state_1 = 'OD'

        data.append(state_1)
    data.sort(reverse=True)
    return data


def next_state(weights):
    choice = np.random.random() * sum(weights)
    for i, w in enumerate(weights):
        choice -= w
        if choice < 0:
            return i


if __name__ == '__main__':
    data = pd.read_csv('userSatisfactionStates.csv', index_col=0)
    transition_matrix, state_prob = get_transition_matrix_all_users(data, 4)
    first_state = next_state(state_prob)
    data = simulation(first_state, transition_matrix, 5000)

    plt.figure()
    n, bins, patches = plt.hist(data, 50,  histtype='bar')
    plt.grid(True)
    plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
