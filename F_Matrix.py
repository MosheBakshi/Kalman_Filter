# from pandas import np


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
                q.append('1')
            elif j - i == len(state_vector) / 2:
                q.append("%.0f" % (state_vector[0] / state_vector[1]))
            else:
                q.append('0')
        f_matrix.append(q)
    return f_matrix


def main():
    state_vector = [1, 1, 1, 1]
    f_matrix = create_f_matrix(state_vector)
    # print(f_matrix, '\n')
    for line in f_matrix:
        print(line)
    # multed_mat = [[]*len(f_matrix[1])]*len(state_vector)
    # for i in range(len(state_vector)):
    #     # iterate through columns of Y
    #     for j in range(len(f_matrix[1])):
    #         # iterate through rows of Y
    #         for k in range(len(f_matrix[1])):
    #             multed_mat[i][j] += state_vector[i][k] * f_matrix[k][j]
    # for line in multed_mat:
    #     print(line)


if __name__ == '__main__':
    main()
