import cvxpy
import doctest


def continuous_objects(valuations: list[list[float]]):

    # Declare the variables and utility
    num_of_players = len(valuations)
    num_of_resources = len(valuations[0])
    variables = []
    utility_for_player = []

    # Calculation of the utility for all player
    for i in range(num_of_players):
        utility = 0
        for j in range(num_of_resources):
            variables.append(cvxpy.Variable(num_of_players))  # fractions of all the resources by number of player
            utility += variables[j][i] * valuations[i][j]  # Calculation of the utility for player i
        utility_for_player.append(utility)  # insert  utility for player i to utility list

    min_utility = cvxpy.Variable()

    # list all the constraints for the maximize function
    fixed_constraints = \
        [variables[i][j] >= 0 for i in range(num_of_resources) for j in range(num_of_players)] + \
        [variables[i][j] <= 1 for i in range(num_of_resources) for j in range(num_of_players)] + \
        [utility_for_player[i] >= min_utility for i in range(num_of_players)] + \
        [sum(variables[i]) == 1 for i in range(num_of_resources)]

    # solve the equation
    prob = cvxpy.Problem(cvxpy.Maximize(min_utility), constraints=fixed_constraints)
    prob.solve(solver=cvxpy.ECOS)

    # # print the result
    # for i in range(num_of_players):
    #     print(f"player {i} receives ", end=" ")
    #     for j in range(num_of_resources):
    #         if j == 0:
    #             print(f"{abs(round(variables[j][i].value * 100, 2))}% of resource {j}", end="")
    #         else:
    #             print(f" and {abs(round(variables[j][i].value * 100, 2))}% of resource {j}", end="")
    #     print()


if __name__ == "__main__":
    doctest.testmod()
