import cvxpy as cp
import doctest


def egalitarian_allocation(valuations: list[list[float]]):
    """
              Examples:
                  >>> egalitarian_allocation(valuations=[[11, 11, 22, 33, 44], [11, 22, 44, 55, 66], [11, 33, 22, 11, 66]])
                  Player 0 gets items  0, 4, with utility 55
                  Player 1 gets items  3, with utility 55
                  Player 2 gets items  1, 2, with utility 55

                  >>> egalitarian_allocation(valuations=[[11, 11, 55], [22, 22, 33], [33, 44, 0]])
                  Player 0 gets items  2, with utility 55
                  Player 1 gets items  0, with utility 22
                  Player 2 gets items  1, with utility 44

                  >>> egalitarian_allocation(valuations=[[10, 20, 30], [10, 20, 30], [35, 50, 5]])
                  Player 0 gets items  1, with utility 20
                  Player 1 gets items  2, with utility 30
                  Player 2 gets items  0, with utility 35

                  >>> egalitarian_allocation(valuations=[[40, 20, 30, 10], [10, 60, 10, 30], [20, 30, 70, 60], [50, 10, 40, 80]])
                  Player 0 gets items  0, with utility 40
                  Player 1 gets items  1, with utility 60
                  Player 2 gets items  2, with utility 70
                  Player 3 gets items  3, with utility 80
              """

    # Determine the number of players and objects
    num_of_players = len(valuations)
    num_of_objects = len(valuations[0])

    # Declare decision variables
    variables = cp.Variable((num_of_players, num_of_objects), boolean=True)
    utility_for_player = [0] * num_of_players

    # Calculate utility for each player
    for i in range(num_of_players):
        utility = sum(variables[i, j] * valuations[i][j] for j in range(num_of_objects))
        utility_for_player[i] = utility

    # Declare optimization variables
    min_utility = cp.Variable()
    constraints = [min_utility <= utility_for_player[i] for i in range(num_of_players)]

    # Add constraints to ensure each object is allocated to exactly one player
    for j in range(num_of_objects):
        constraint = sum(variables[i][j] for i in range(num_of_players)) == 1
        constraints.append(constraint)

    # Formulate the optimization problem
    obj = cp.Maximize(min_utility)
    prob = cp.Problem(obj, constraints)

    # Solve the optimization problem
    prob.solve()

    # print the result
    for i in range(num_of_players):
        print(f"Player {i} gets items ", end=" ")
        for j in range(num_of_objects):
            if variables[i][j].value > 0.5:
                print(j, end=", ")
        print(f"with utility {int(utility_for_player[i].value)}")


if __name__ == "__main__":
    doctest.testmod()

    # egalitarian_allocation([[11, 11, 22, 33, 44], [11, 22, 44, 55, 66], [11, 33, 22, 11, 66]])
    #
    # egalitarian_allocation([[11, 11, 55], [22, 22, 33], [33, 44, 0]])
    #
    # egalitarian_allocation([[10, 20, 30], [10, 20, 30], [35, 50, 5]])
    #
    # egalitarian_allocation([[40, 20, 30, 10], [10, 60, 10, 30], [20, 30, 70, 60], [50, 10, 40, 80]])
