import time
from comtypes.safearray import numpy as np
from numpy.core._multiarray_umath import matmul

from F_Matrix import create_f_matrix


def main():
    sleep_time = 0
    stdPos = 2
    stdVel = 1.5
    varPos = stdPos ** 2
    varVel = stdVel ** 2
    pMatrix = [[varPos, 0],
               [0, varVel]]
    hMatrix = [[0.3048,
                0]]
    state_vector = [[8],
                    [5]]  # [X, Y, X', Y']
    print('Old State Vector:')
    for line in state_vector:
        print(line)
    #   print(np.matrix(state_vector).size, 'x', np.matrix(state_vector[0]).size)
    f_matrix = create_f_matrix(state_vector)
    ft_matrix = [[f_matrix[j][i] for j in range(len(f_matrix))] for i in range(len(f_matrix[0]))]
    state_vector = matmul(f_matrix, state_vector)
    print('\nF Matrix:')  # print F Matrix
    for line in f_matrix:
        print(line)
    time.sleep(sleep_time)
    print('\nFT Matrix:')  # print F transpose Matrix
    for line in ft_matrix:
        print(line)
    time.sleep(sleep_time)
    print('\nOld P Matrix:')  # print Old P Matrix
    for line in pMatrix:
        print(line)
    time.sleep(sleep_time)
    pMatrix = matmul(matmul(f_matrix, pMatrix), ft_matrix)
    np.set_printoptions(formatter={'float_kind': "{:.2f}".format})  # format of printing floating point in matrix
    print('\nNew P Matrix:')  # print New P Matrix
    for line in pMatrix:
        print(line)
    time.sleep(sleep_time)
    print('\nNew State Vector:')  # print New State Vector
    for line in state_vector:
        print(line)
    time.sleep(sleep_time)
    #   print(np.matrix(state_vector).size, 'x', np.matrix(state_vector[0]).size)

    #                                            END OF PREDICTION
    #                                            START OF UPDATE
    mean_vector = matmul(hMatrix, state_vector)
    sense_pMatrix = matmul(matmul(hMatrix, pMatrix), np.matrix(hMatrix).transpose())
    print('\nNew State Vector Expected:')
    for line in mean_vector:
        print(line)
    print('\nNew Expected P Matrix:')
    for line in sense_pMatrix:
        print(line)
    time.sleep(sleep_time)


if __name__ == '__main__':
    main()