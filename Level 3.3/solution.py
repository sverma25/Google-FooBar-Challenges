def answer(n):
    # your code here
    staircases = [[0 for cols in range(n)] for rows in range(n + 1)]

    # Initializing with 1, as no staircase can be built with n <3
    for i in range(3):
        for j in range(i, n):
            staircases[i][j] = 1

    # Using partitions, we increment each with 1 as shown
    for row in range(3, n + 1):
        for col in range(2, n):
            if row >= col:
                staircases[row][col] = staircases[row - col][col - 1]

            staircases[row][col] += staircases[row][col - 1]

    # Print the solution
    return staircases[n][n - 1]

if __name__ == "__main__":
    print(answer(4))
    print(answer(5))
    print(answer(200))
