from random import random
import math

radius = 2


def estimate_pi(num_random_tests):
    pi_counter = 0
    rsquared = radius ** 2
    for _ in range(num_random_tests):
        x_rand = random() * radius
        y_rand = random() * radius
        if (x_rand ** 2) + (y_rand ** 2) < rsquared:
            pi_counter += 1

    return 4 * pi_counter / num_random_tests


assert math.isclose(round(estimate_pi(100000000), 3), 3.141, rel_tol=1e-09, abs_tol=0.0)
