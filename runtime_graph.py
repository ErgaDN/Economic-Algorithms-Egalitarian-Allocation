import random
import time
import matplotlib.pyplot as plt
from continuous_objects import continuous_objects
from egalitarian_allocation import egalitarian_allocation


def generate_random_numbers(i):
    """
    Generates a list of unique random integers within the range from 1 to 99.

    Parameters:
        i (int): The size of the generated list.

    Returns:
        list: A list of unique random integers.
    """
    random_numbers = random.sample(range(1, 100), i)
    return random_numbers


if __name__ == "__main__":
    # Generate a range of numbers representing the number of objects
    num_of_objects = [i for i in range(10, 40)]
    start_idx = num_of_objects[0]

    # Initialize lists to store execution times for each function
    individual_objects_timer_ms = [0] * len(num_of_objects)
    continuous_objects_timer_ms = [0] * len(num_of_objects)

    # Loop through different numbers of objects and measure execution time
    for i in num_of_objects:
        # Generate random valuations for two players
        valuations_A = generate_random_numbers(i)
        valuations_B = generate_random_numbers(i)

        # Measure execution time for distribution of individual objects
        start = time.time()
        egalitarian_allocation([valuations_A, valuations_B])
        end = time.time()
        individual_objects_timer_ms[i - start_idx] = round((end - start) * 1000, 2)

        # Measure execution time for distribution of continuous objects
        start = time.time()
        continuous_objects([valuations_A, valuations_B])
        end = time.time()
        continuous_objects_timer_ms[i - start_idx] = round((end - start) * 1000, 2)

    # Plot the execution times
    plt.plot(num_of_objects, individual_objects_timer_ms, 'g', label='Individual Objects')
    plt.plot(num_of_objects, continuous_objects_timer_ms, label='Continuous Objects')
    plt.ylabel('time in ms')
    plt.xlabel('number of objects')
    plt.title('Execution time vs Resource amount')
    plt.legend()
    plt.show()
