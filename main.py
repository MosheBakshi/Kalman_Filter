##
# Main function of the Python program.
#
##

from finder import compute_gaussian, predict, update
# import numpy as np
import math


def main():
    # we print a heading ComputeGausianand make it bigger using HTML formatting
    likelihood = compute_gaussian(100, 15, 125)
    print(likelihood)
    print(compute_gaussian(10, 1.2, 10))
    l3 = predict(5, 0, 15, 2)
    print("mu3: {0:8.5f}, variance3: {1:8.5f}".format(l3[0], l3[1]))
    print("{0:8.5f},{1:8.5f}".format(update(3, 4.5, 9, 1.3)[0], update(3, 4.5, 9, 1.3)[1]))
    # answer is [12.0, 5.8]
    print("{0:8.5f},{1:8.5f}".format(update(3, 4.5, 9, 0)[0], update(3, 4.5, 9, 0)[1]))
    # answer is [12.0, 4.5]


if __name__ == '__main__':
    main()
