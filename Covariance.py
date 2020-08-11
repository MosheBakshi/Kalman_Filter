def covariance(mean1, mean2, values_1, values_2):
    """
    :param values_2:
    :param values_1:
    :param mean1:
    :param mean2:
    :return: new calculated covariance
    """
    new_cov = 0
    for i in range(len(values_1)):
        new_cov += (mean1 - values_1[i])*(mean2 - values_2[i])
    return "%.2f" % (new_cov/len(values_1))


def main():
    values1 = [60, 88, 50, 100, 95]
    values2 = [73, 80, 47, 92, 88]
    mean1 = sum(values1)/len(values1)
    mean2 = sum(values2)/len(values2)
    list_of_mean = [covariance(mean1, mean1, values1, values1), covariance(mean2, mean2, values2, values2)]
    cov = covariance(mean1, mean2, values1, values2)
    sig_matrix = [[None, None], [None, None]]
    for i in range(0, len(sig_matrix)):
        for j in range(0, len(sig_matrix[i])):
            if i == j:
                sig_matrix[i][j] = list_of_mean[j]
            else:
                sig_matrix[i][j] = cov
    for line in sig_matrix:
        print(line)


if __name__ == '__main__':
    main()