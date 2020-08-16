import time
from comtypes.safearray import numpy as np
from numpy.core._multiarray_umath import matmul

from F_Matrix import create_f_matrix


def transpose_matrix(f_matrix):
    """
    :param f_matrix:
    :return: matrix - transposed
    """
    return [[f_matrix[j][i] for j in range(len(f_matrix))] for i in range(len(f_matrix[0]))]


def predict_vector(state_vector, f_matrix):
    """
    :param state_vector:
    :param f_matrix:
    :return: vector - just predicted not updated
    """
    return matmul(f_matrix, state_vector)  # New state vector prediction


def predict_p_matrix(f_matrix, pMatrix):
    """
    :param f_matrix:
    :param pMatrix:
    :return: matrix - just predicted not updated
    """
    return matmul(matmul(f_matrix, pMatrix), transpose_matrix(f_matrix))  # new predicted p matrix


def create_kg(pMatrix, hMatrix, rMatrix):
    """
    :param pMatrix:
    :param hMatrix:
    :param rMatrix:
    :return: scalar or vector or matrix - Kalman Gain
    """
    return matmul(matmul(pMatrix, transpose_matrix(hMatrix)),  # calculate Kalman Gain
                  np.linalg.inv(matmul(matmul(hMatrix, pMatrix), transpose_matrix(hMatrix)) + rMatrix))


def update_state_vector(state_vector, KG, sensor_vector, hMatrix):
    """
    :param state_vector:
    :param KG:
    :param sensor_vector:
    :param hMatrix:
    :return: vector - updated
    """
    return state_vector + matmul(KG, (sensor_vector - matmul(hMatrix, state_vector)))


def update_p_matrix(pMatrix, KG, hMatrix):
    """
    :param pMatrix:
    :param KG:
    :param hMatrix:
    :return: matrix - p matrix updated
    """
    return pMatrix - matmul(matmul(KG, hMatrix), pMatrix)


def calculate_p_x(state_vector, pMatrix, hMatrix, rMatrix, sensor_vector, sleep_time):
    """
    :param state_vector:
    :param pMatrix:
    :param hMatrix:
    :param rMatrix:
    :param sensor_vector:
    :param sleep_time:
    :return: list of new updated state vector and updated p matrix
    """
    # START OF PREDICTION:
    print('Old State Vector:')
    for line in state_vector:
        print(line)
    time.sleep(sleep_time)
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
    #     END OF PREDICTION
    #     START OF UPDATE
    KG = create_kg(pMatrix, hMatrix, rMatrix)
    state_vector = update_state_vector(state_vector, KG, sensor_vector, hMatrix)
    pMatrix = update_p_matrix(pMatrix, KG, hMatrix)
    print('\nKG is:')       # print KG calculated
    for line in KG:
        print(line)
    time.sleep(sleep_time)
    return [state_vector, pMatrix]


def main():
    sleep_time = 0
    # Parameters:
    stdPos = 2
    stdVel = 1.5
    stdSensorPos = 0.5
    stdSensorVel = 4
    varPos = stdPos ** 2
    varVel = stdVel ** 2
    varSensorPos = stdSensorPos ** 2
    varSensorVel = stdSensorVel ** 2
    # Vectors and Matrices:
    state_vector = [[8],        # state vector
                    [5]]
    pMatrix = [[varPos, 0],     # pMatrix
               [0, varVel]]
    hMatrix = [[3.2808, 0],     # hMatrix
               [0, 1]]
    sensor_vector = [[43],      # sensor vector [43 feet, 4 vel]
                     [4]]
    rMatrix = [[varSensorPos, 0],       # rMatrix
               [0, varSensorVel]]
    state_vector, pMatrix = calculate_p_x(state_vector, pMatrix, hMatrix, rMatrix, sensor_vector, sleep_time)
    print('\nNew Updated State Vector:')        # print updated State Vector
    for line in state_vector:
        print(line)
    time.sleep(sleep_time)
    print('\nNew Updated P Matrix:')        # print updated P Matrix
    for line in pMatrix:
        print(line)
    time.sleep(sleep_time)


if __name__ == '__main__':
    main()
