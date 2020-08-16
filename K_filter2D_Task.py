import time
from comtypes.safearray import numpy as np
from numpy.core._multiarray_umath import matmul

from F_Matrix import create_f_matrix


def transpose_matrix(f_matrix):
    return [[f_matrix[j][i] for j in range(len(f_matrix))] for i in range(len(f_matrix[0]))]


def predict_vector(state_vector, f_matrix):
    return matmul(f_matrix, state_vector)  # New state vector prediction


def predict_p_matrix(f_matrix, pMatrix):
    return matmul(matmul(f_matrix, pMatrix), transpose_matrix(f_matrix))  # new predicted p matrix


def create_kg(pMatrix, hMatrix, rMatrix):
    return matmul(matmul(pMatrix, transpose_matrix(hMatrix)),  # calculate Kalman Gain
           np.linalg.inv(matmul(matmul(hMatrix, pMatrix), transpose_matrix(hMatrix)) + rMatrix))


def update_state_vector(state_vector, KG, sensor_pos, hMatrix):
    return state_vector + matmul(KG, (sensor_pos - matmul(hMatrix, state_vector)))


def update_p_matrix(pMatrix, KG, hMatrix):
    return pMatrix - matmul(matmul(KG, hMatrix), pMatrix)


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
    hMatrix = [[3.2808, 0]]
    # hMatrix_reverse = [[0.3048, 0]]
    sensor_pos = [[43]]
    rMatrix = [[varSensor]]
    state_vector = [[8],
                    [5]]  # [X, Y, X', Y'
    print('Old State Vector:')
    for line in state_vector:
        print(line)
    time.sleep(sleep_time)
    #   print(np.matrix(state_vector).size, 'x', np.matrix(state_vector[0]).size)
    print('\nOld P Matrix:')  # print Old P Matrix
    for line in pMatrix:
        print(line)
    time.sleep(sleep_time)
    f_matrix = create_f_matrix(state_vector)
    state_vector = predict_vector(state_vector, f_matrix)
    pMatrix = predict_p_matrix(f_matrix, pMatrix)
    np.set_printoptions(formatter={'float_kind': "{:.2f}".format})  # format of printing floating point in matrix
    print('\nF Matrix:')  # print F Matrix
    for line in f_matrix:
        print(line)
    time.sleep(sleep_time)
    print('\nNew P Matrix:')  # print New P Matrix
    for line in pMatrix:
        print(line)
    time.sleep(sleep_time)
    print('\nNew State Vector:')  # print New State Vector
    for line in state_vector:
        print(line)
    time.sleep(sleep_time)
    #                                            END OF PREDICTION
    #                                            START OF UPDATE
    KG = create_kg(pMatrix, hMatrix, rMatrix)
    state_vector = update_state_vector(state_vector, KG, sensor_pos, hMatrix)
    pMatrix = update_p_matrix(pMatrix, KG, hMatrix)
    print('\nKG is:')
    for line in KG:
        print(line)
    time.sleep(sleep_time)
    print('\nNew Updated State Vector:')
    for line in state_vector:
        print(line)
    time.sleep(sleep_time)
    print('\nNew Updated P Matrix:')
    for line in pMatrix:
        print(line)
    time.sleep(sleep_time)


if __name__ == '__main__':
    main()
