import time
from numpy.core._multiarray_umath import matmul


def create_f_matrix(state_vector):
    """
    :param state_vector
    :return: f_matrix
    """
    f_matrix = []
    for i in range(0, len(state_vector)):
        q = []
        for j in range(0, len(state_vector)):
            if i == j:
                q.append(1)
            elif j - i == len(state_vector) / 2:
                q.append(1)  # float("%.2f" % (state_vector[0][i] / state_vector[0][j]))
            else:
                q.append(0)
        f_matrix.append(q)
    return f_matrix


def main():
    state_vector = [[8],
                    [5],
                    [1],
                    [2]]  # [X, Y, X', Y']
    for line in state_vector:
        print(line)
    f_matrix = create_f_matrix(state_vector)
    state_vector = matmul(f_matrix, state_vector)
    print('\nF Matrix:')     # print F Matrix
    for line in f_matrix:
        print(line)


if __name__ == '__main__':
    main()
