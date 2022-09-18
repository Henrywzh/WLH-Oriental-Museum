import pytesseract as pt
import cv2
import re

def ocr(img):
    text = pt.image_to_string(img)
    return text

def amount(content, find):
    l = re.findall(find, content)
    num = []

    for i in l:
        i = i[2:]
        i = int(i.replace(',', '').replace('.', ''))
        num.append(i)
    return num

def price(content, exchangeRate, find):
    li = re.findall(find, content)
    priceList = []

    for i in li:
        i = i.replace(',', '').replace('R', '')
        i = i[1:]
        if i[-2:] == ' 4' or i[-2:] == ' 5':
            i = i[0:-2]
        i = int(i.replace(' ','').replace('.',''))
        i = round(i/exchangeRate)
        priceList.append(i)

    return priceList

def rate(content):
    data = re.findall('[0-9]+[.,][0-9][0-9]%', content)
    l = []
    for i in data:
        l.append(i.replace(',', '.'))
    return [float(i[:-1]) for i in l]

def transaction(n, p):
    return [round(float(n[i]) * float(p[i]) / 100) for i in range(len(n))]

def main():
    pic = ['/Users/henry/Desktop/2017.png', '/Users/henry/Desktop/2018.png',
           '/Users/henry/Desktop/2019.png', '/Users/henry/Desktop/2020.png',]

    exchangeRate = [7.03, 6.62, 6.91, 1]

    find1 = ['¥[^ ]+|¥ [^ ]+', '¥[^ ]+|¥ [^ ]+', '¥[^ ]+',
             '\$.{12}|\$.{11}|\$.{10}|\$.{9}',]

    find2 = ['[a-zA-Z)\]] [0-9][^ a-zA-Z%]+', '[a-zA-Z)\]] [0-9][^ a-zA-Z%]+',
             '[a-zA-Z)\]] [0-9][^ a-zA-Z%]+', '[a-zA-Z)] [0-9,]+']

    allAmount = []
    allTransaction = []
    allRate = []
    allPrice = []

    for i in range(len(pic)):
        img = cv2.imread(pic[i])
        myOCR = ocr(img)
        transactionRate = rate(myOCR)
        totalPrice = price(myOCR, exchangeRate[i], find1[i])
        totalAmount = amount(myOCR, find2[i])

        if i == 0:
            totalPrice.insert(40, 24239972)

        if i == 1:
            totalPrice.insert(18, 58002205)

            totalAmount.insert(4, 4321)
            totalAmount.insert(18, 5052)
            totalAmount[33] = 111
            totalAmount.remove(8877)
            totalAmount.remove(77)
            totalAmount.insert(32, 2954)
            totalAmount.insert(41, 536)

            transactionRate.insert(4, 74.82)
            transactionRate.insert(18, 87.07)
            transactionRate.insert(43, 77.47)

        elif i == 2:
            totalAmount.remove(6805)
            totalAmount[-19] = 41
            totalAmount.insert(34, 414)
            totalAmount[-2] = 7110

            transactionRate.insert(13, 71.72)

        elif i == 3:
            totalAmount[10] = 3173
            totalAmount[20] = 2043
            totalAmount[27] = 7021

        totalTransaction = transaction(totalAmount, transactionRate)

        for i in range(len(totalAmount)):
            allAmount.append(totalAmount[i])
            allTransaction.append(totalTransaction[i])
            allRate.append(transactionRate[i])
            allPrice.append(totalPrice[i])

    data = {
        'Total Amount': allAmount,
        'Total Transaction': allTransaction,
        'Transaction rate': allRate,
        'Total Price': allPrice
    }

    return data


# ----
import pandas as pd

df = pd.DataFrame(main())
print(df)
print(df.corr().to_string())

# ----
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.metrics import r2_score

fig, ax = plt.subplots(1,1, figsize=(15,8))

x = df['Total Amount']
y = df['Total Transaction']

train_x = x[:160]
train_y = y[:160]
test_x = x[160:]
test_y = y[160:]

slope, intercept, r, p, std_err = stats.linregress(train_x, train_y)

def pred(x):
    return slope * x + intercept

mymodel1 = list(map(pred, train_x))
mymodel2 = list(map(pred, test_x))

r2 = r2_score(train_y, mymodel1)
r2New = r2_score(test_y, mymodel2)

check = int(input('Enter the value: '))

print(r2, r2New)
print(pred(check))

ax.scatter(train_x, train_y)
ax.scatter(test_x, test_y)
ax.plot(train_x, mymodel1)
ax.vlines(check, 0, pred(check), color='gold')
ax.hlines(pred(check), 0, check, color='gold')
plt.show()
