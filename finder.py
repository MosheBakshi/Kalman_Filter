import math
import sympy
from sympy import *


def compute_gaussian(mu, variance, value_check_prob):
    return (1 / (math.sqrt(2 * math.pi * variance))) * math.exp(-0.5 * (value_check_prob - mu) ** 2 / (variance))


def predict(mu1, var1, mu2, var2):
    x = Symbol('x')
    q = []
    mu3 = (mu1 * var2 + mu2 * var1) / (var1 + var2)
    var3 = (var1 * var2) / (var1 + var2)
    q.append(mu3)
    q.append(var3)
    return q


def update(mean1, var1, mean2, var2):
    new_gauss = [mean1 + mean2, math.sqrt(var1 ** 2 + var2 ** 2)]
    return new_gauss
