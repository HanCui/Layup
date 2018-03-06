import pandas as pd
import numpy as np

def returns():
    returnmatrix = np.random.rand(100, 100)
    return returnmatrix

def randommatrices(number):
    volume = np.random.rand(100,100)
    volumeData = pd.DataFrame(data = volume)

    mcap = np.random.rand(100, 100)
    mcapData = pd.DataFrame(data = mcap)

    prices = np.random.rand(100, 100)
    priceData = pd.DataFrame(data = prices)

    if (number == 0):
        return volumeData
    elif (number == 1):
        return mcapData
    else:
        return priceData

def rank(number):
    volume = randommatrices(0)
    volumeRank = volume.rank(axis = 1)
    volumeRank = volumeRank.as_matrix()

    mcap = randommatrices(1)
    medianMcap = mcap.median(axis = 1)
    medianMcap = medianMcap.as_matrix()

    if (number == 0):
        return volumeRank
    else:
        return medianMcap

def modifiedReturns(date):
    volumeRank = rank(0)
    medianMcap = rank(1)

    mcap = randommatrices(1)
    mcap = mcap.as_matrix()
    prices = randommatrices(2)
    prices = prices.as_matrix()

    numRow = mcap.shape[0]
    numCol = mcap.shape[1]
    returnMatrix = np.zeros([10, 20])
    actualReturnMatrix = returns()
    index = np.argsort(volumeRank)
    count = np.zeros([numCol])

    for row in range(date, date + 10):
        col = numCol - 1
        counter = 0
        while (col >= 0 and counter < 20):
            indice = index[row, col]
            if (prices[row, indice] >= 0.25 and mcap[row, indice] >= medianMcap[row]):
                counter += 1
                count[indice] += 1
            col -= 1

    position = np.argsort(count)
    best = position[80:100]
    counter = 0

    for col in range(0, numCol):
        if (np.isin(col, best)):
            for row in range(date, date + 10):
                returnMatrix[row - date, counter] = actualReturnMatrix[row, col]
            counter += 1
    return returnMatrix

def beta(date):
    returns = modifiedReturns(date)
    total = np.sum(returns, axis = 1)
    indexReturns = total / 20

    beta = pd.rolling
    print beta

beta(0)





