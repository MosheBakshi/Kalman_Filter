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
        new_cov += (mean1 - values_1[i]) * (mean2 - values_2[i])
    return "%.2f" % (new_cov / len(values_1))


def mean(values):
    return sum(values) / len(values)


def main():
    values1 = [60, 88, 50, 100, 95]
    values2 = [73, 80, 47, 92, 88]
    values3 = [80, 70, 50, 90, 87]
    list_of_values = [values1, values2, values3]
    list_of_means = [mean(values1), mean(values2), mean(values3)]
    sig_matrix = []
    for i in range(0, len(list_of_values)):
        print("Mean of values ", (i+1), " :", list_of_means[i])
        q = []
        for j in range(0, len(list_of_values)):
            q.append(covariance(list_of_means[i], list_of_means[j], list_of_values[i], list_of_values[j]))
        sig_matrix.append(q)
    for line in sig_matrix:
        print(line)


if __name__ == '__main__':
    main()
