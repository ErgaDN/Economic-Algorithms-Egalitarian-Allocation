import random
import time
import matplotlib.pyplot as plt
from continuous_objects import continuous_objects
from egalitarian_allocation import egalitarian_allocation


def generate_random_numbers(i):
    random_numbers = random.sample(range(1, 100), i)
    return random_numbers


if __name__ == "__main__":
    num_of_objects = [i for i in range(10, 40)]
    start_idx = num_of_objects[0]

    individual_objects_timer_ms = [0] * len(num_of_objects)
    continuous_objects_timer_ms = [0] * len(num_of_objects)

    for i in num_of_objects:
        valuations_A = generate_random_numbers(i)
        valuations_B = generate_random_numbers(i)

        start = time.time()
        egalitarian_allocation([valuations_A, valuations_B])
        end = time.time()
        individual_objects_timer_ms[i - start_idx] = round((end - start) * 1000, 2)

        start = time.time()
        continuous_objects([valuations_A, valuations_B])
        end = time.time()
        continuous_objects_timer_ms[i - start_idx] = round((end - start) * 1000, 2)

    plt.plot(num_of_objects, individual_objects_timer_ms, 'g', label='Individual Objects')
    plt.plot(num_of_objects, continuous_objects_timer_ms, label='Continuous Objects')
    plt.ylabel('time in ms')
    plt.xlabel('number of objects')
    plt.legend()
    plt.show()

