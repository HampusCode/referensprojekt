import numpy as np


def calculateRewards(rewardMatrix, comparisonMatrix, valueMatrix, discountFactor, convergenceThreshold):
    (rows, cols) = valueMatrix.shape
    changeValue = 1
    while changeValue > convergenceThreshold:
        for i in range(rows):
            for j in range(cols):
                stateReward = 0.0
                maxReward = 0.0
                for dir in [(j, i+1), (j+1, i), (j, i-1), (j-1, i)]:
                    (x, y) = dir
                    if (0 <= x < rows) and (0 <= y < cols):
                        expectedReward = (0.8 * valueMatrix[x, y] + 0.2 * valueMatrix[j, i]) * discountFactor
                        stateReward = rewardMatrix[x, y] + expectedReward
                        maxReward = max(maxReward, stateReward)

                valueMatrix[i, j] = maxReward

        changeValue = sum(abs(valueMatrix - comparisonMatrix).flatten())
        comparisonMatrix = np.copy(valueMatrix)
    return valueMatrix

rewardMatrix = np.array([[0, 0, 0], [0, 10, 0], [0, 0, 0]], dtype=float)
comparisonMatrix = np.zeros((3, 3), dtype=float)
valueMatrix = np.zeros((3, 3), dtype=float)
discountFactor = 0.9
convergenceThreshold = 0.01

resultMatrix = calculateRewards(rewardMatrix, comparisonMatrix, valueMatrix, discountFactor, convergenceThreshold)

with np.nditer(resultMatrix, flags=['multi_index']) as it:
    while not it.finished:
        print(f"{resultMatrix[it.multi_index]:.2f}", end=' ')
        if it.multi_index[1] == resultMatrix.shape[1] - 1:
            print()
        it.iternext()
