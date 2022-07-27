import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow import keras

def RSI(close):
    gain = sum([close[i] - close[i-1] for i in range(1, len(close)) if close[i] > close[i-1]])
    loss = sum([close[i] - close[i-1] for i in range(1, len(close)) if close[i] < close[i-1]]) * -1
    eqn = 1 - 1/(1 + gain/loss)
    return eqn

def ROC(old, new):
    eqn = (new - old) / old
    return eqn

def WilliamsR(close, high, low):
    highestHigh = max(high)
    recentClose = close[-1]
    lowestLow = min(low)
    eqn = -1 * (highestHigh - recentClose) / (highestHigh - lowestLow)
    return eqn

def WMA(close):
    total = len(close) * (len(close) + 1) / 2
    eqn = sum([close[i] * (i + 1) for i in range(len(close))]) / total
    return eqn

def EMA(close):
    alpha = 2 / (1 + len(close))
    up = sum([close[i] * (1 - alpha)**i for i in range(len(close))])
    down = sum([(1 - alpha)**i for i in range(len(close))])
    eqn = up / down
    return eqn

def SMA(close):
    eqn = sum(close) / len(close)
    return eqn

def CCI(close, high, low):
    price = [(close[i] + high[i] + low[i]) / 3 for i in range(len(close))]
    ma = sum(price) / len(close)
    dev = sum([abs(i - ma) for i in price]) / len(close)
    eqn = (price[-1] - ma) / (0.015 * dev)
    return eqn

def CMO(close):
    gain = sum([close[i] - close[i-1] for i in range(1, len(close)) if close[i] > close[i-1]])
    loss = sum([close[i] - close[i-1] for i in range(1, len(close)) if close[i] < close[i-1]]) * -1
    eqn = (gain - loss) / (gain + loss)
    return eqn

def CMF(close, high, low, volume):
    up = sum([((close[i] - low[i]) - (high[i] - close[i])) / (high[i] - low[i]) * volume[i] for i in range(len(close))])
    down = sum(volume)
    eqn = up / down
    return eqn

def Trade(close, high, low, volume):
    price = (close + high + low) / 3
    eqn = price * volume
    return eqn

def data(df):
    open = np.array(df['Open'])
    high = np.array(df['High'])
    low = np.array(df['Low'])
    close = np.array(df['Price'])
    volume = np.array(df['Vol.'])

    rsi = []
    cmo = []
    williamsR = []
    wma = []
    ema = []
    sma = []
    cci = []
    roc = []
    cmf = []
    trade = [Trade(close[i], high[i], low[i], volume[i]) for i in range(len(close))]

    for i in range(len(close) - 14):
        rsi.append(RSI(close[i:i+15]))
        cmo.append(CMO(close[i:i+15]))

    for i in range(len(close) - 13):
        williamsR.append(WilliamsR(close[i:i+14], high[i:i+14], low[i:i+14]))
        wma.append(WMA(close[i:i+14]))
        sma.append(SMA(close[i:i+14]))
        cci.append(CCI(close[i:i+14], high[i:i+14], low[i:i+14]))
        cmf.append(CMF(close[i:i+14], high[i:i+14], low[i:i+14], volume[i:i+14]))

    for i in range(len(close) - 7):
        ema.append(EMA(close[i:i+8]))

    for i in range(len(close) - 1):
        roc.append(ROC(close[i], close[i+1]))

    open = open[14:]
    high = high[14:]
    low = low[14:]
    close = close[14:]
    volume = volume[14:]
    trade = np.array(trade[14:])
    sma = np.array(sma[1:])
    wma = np.array(wma[1:])
    ema = np.array(ema[7:])
    williamsR = np.array(williamsR[1:])
    cmo = np.array(cmo)
    rsi = np.array(rsi)
    cci = np.array(cci[1:])
    roc = np.array(roc[13:])
    cmf = np.array(cmf[1:])
    X = pd.DataFrame({'open': open, 'high':high, 'low':low, 'close':close, 'volume':volume, 'trade':trade, 'sma':sma, 'wma':wma, 'ema':ema, 'williamsR':williamsR, 'cmo':cmo, 'rsi':rsi, 'cci':cci, 'roc':roc, 'cmf':cmf})
    Y = close[1:]
    trueY = np.array([Y[i] < Y[i+1] for i in range(len(Y) - 1)])
    X.drop(len(X) - 1, inplace = True)
    X['newClose'] = Y

    return X, Y, trueY

def multipleRegression(df):
    y = np.array(df['newClose'])
    x = np.array([np.array([1 for i in df['open']]), np.array(df['sma']), np.array(df['wma']), np.array(df['ema']), np.array(df['cci']), np.array(df['rsi'])])
    c = np.linalg.inv(x.dot(x.transpose()))
    b = c.dot(x).dot(y)

    print('Stock Price Model:')
    print(f'y = {b[0]} + {b[1]}x1 + {b[2]}x2 + {b[3]}x3+ {b[4]}x4 + {b[5]}x5')

    return b

def r2(l, predY):
    meanY = sum([i for i in l])/len(l)
    actualY = list(l)
    rSquared = 1 - (sum([(actualY[i] - predY[i])**2 for i in range(len(predY))]))/(sum([(actualY[i] - meanY)**2 for i in range(len(predY))]))
    return rSquared

def modelTest(train, test):
    b = multipleRegression(train)
    predY = round(b[0] + b[1]*test['sma'] + b[2]*test['wma'] + b[3]*test['ema']+ b[4]*test['cci'] + b[5]*test['rsi'], 3)
    actualY = np.array(test['newClose'])
    r2Score = r2(actualY, predY)
    predY = np.array(predY)
    print(f'R-squared score: {r2Score}')

    return test.index, predY, actualY

def LSTM_Model_Online(trainDf, testDf):
    close_prices = trainDf['Price']

    x_train = []
    y_train = []

    for i in range(60, len(trainDf)):
        x_train.append(close_prices[i-60:i])
        y_train.append(close_prices[i])

    x_train, y_train = np.array(x_train), np.array(y_train)
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

    # --

    close_prices = testDf['Price']

    x_test = []
    y_test = []

    for i in range(60, len(testDf)):
        x_test.append(close_prices[i-60:i])
        y_test.append(close_prices[i])

    x_test = np.array(x_test)
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

    model = keras.Sequential([
        keras.layers.LSTM(100, return_sequences=True, input_shape=(x_train.shape[1], 1)),
        keras.layers.LSTM(100, return_sequences=False),
        keras.layers.Dense(25),
        keras.layers.Dense(1)
    ])

    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(x_train, y_train, batch_size= 10, epochs=4)

    predictions = model.predict(x_test)

    print('LSTM Model:')
    print('R-squared score: ', r2(y_test, predictions)[0])

    return [i+45 for i in range(len(close_prices[60:]))], list(predictions)

def graphs(index1, pred1, actual, index2, pred2):
    plt.title('Test Data Comparison')
    plt.xlabel('Day')
    plt.ylabel('Close Price/$')
    plt.plot(index1, actual, label='Actual price')
    plt.plot(index1, pred1, label='Own model')
    plt.plot(index2, pred2, label='LSTM Model')
    plt.legend(loc='upper left')
    plt.show()

if __name__ == '__main__':
    trainDf = pd.read_csv('/Users/henry/Desktop/sothebyTrain.csv')
    testDf = pd.read_csv('/Users/henry/Desktop/sothebyTest.csv')

    trainX, trainY, _ = data(trainDf)
    testX, testY, _ = data(testDf)
    index2, pred2 = LSTM_Model_Online(trainDf, testDf)
    index1, pred1, actual = modelTest(trainX, testX)
    graphs(index1, pred1, actual, index2, pred2)
