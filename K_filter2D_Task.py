import time
from comtypes.safearray import numpy as np
from numpy.core._multiarray_umath import matmul

from F_Matrix import create_f_matrix


def transpose_matrix(f_matrix):
    return [[f_matrix[j][i] for j in range(len(f_matrix))] for i in range(len(f_matrix[0]))]


def main():
    sleep_time = 0
    stdPos = 2
    stdVel = 1.5
    stdSensor = 0.5
    varPos = stdPos ** 2
    varVel = stdVel ** 2
    varSensor = stdSensor ** 2
    pMatrix = [[varPos, 0],
               [0, varVel]]
    hMatrix = [[0.3048,
                0]]
    rMatrix = [[varSensor]]
    state_vector = [[8],
                    [5]]  # [X, Y, X', Y'
    print('Old State Vector:')
    for line in state_vector:
        print(line)
    #   print(np.matrix(state_vector).size, 'x', np.matrix(state_vector[0]).size)
    f_matrix = create_f_matrix(state_vector)
    ft_matrix = transpose_matrix(f_matrix)
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
    pMatrix = matmul(matmul(f_matrix, pMatrix), ft_matrix)  # new predicted p matrix
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
    KG = matmul(matmul(pMatrix, transpose_matrix(hMatrix)),
                np.linalg.inv(matmul(matmul(hMatrix, pMatrix), transpose_matrix(hMatrix)) + rMatrix))
    print('\nKG is:')
    for line in KG:
        print(line)
    time.sleep(sleep_time)
    sensor_state_vector = [[43],
                           [5]]
    # state_vector = state_vector + matmul(KG, (sensor_state_vector - matmul(hMatrix, state_vector)))
    # print('\nNew Updated State Vector:')
    # for line in state_vector:
    #     print(line)


if __name__ == '__main__':
    main()
